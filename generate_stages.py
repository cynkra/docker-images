#!/usr/bin/env python3
"""
Generate fine-grained stages.yml with individual jobs for each Docker image.

This script analyzes Dockerfile dependencies and creates a version of stages.yml
where each image has its own job, properly ordered by dependencies.
"""

from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional
from collections import defaultdict, deque
import yaml


class DockerImageAnalyzer:
    """Analyzes Docker images and their dependencies."""

    def __init__(self, root_dir: str):
        self.root_dir = Path(root_dir)
        self.registry = "ghcr.io"
        self.repo_name = "${{ github.repository }}"

    def format_yaml_output(self, config: dict) -> str:
        """Format YAML output with custom spacing and formatting."""
        lines = []

        # Header
        lines.append(f"name: {config['name']}")
        lines.append("")

        # On section
        lines.append("on:")
        on_config = config['on']
        if 'push' in on_config:
            lines.append("  push:")
            lines.append("    branches:")
            for branch in on_config['push']['branches']:
                lines.append(f"      - {branch}")
        if 'workflow_dispatch' in on_config:
            lines.append("  workflow_dispatch: null")
        if 'schedule' in on_config:
            lines.append("  schedule:")
            for schedule in on_config['schedule']:
                lines.append(f"    - cron: {schedule['cron']}")
        lines.append("")

        # Env section
        lines.append("env:")
        for key, value in config['env'].items():
            lines.append(f"  {key}: {value}")
        lines.append("")

        # Jobs section
        lines.append("jobs:")

        job_names = list(config['jobs'].keys())
        for i, job_name in enumerate(job_names):
            job = config['jobs'][job_name]
            if i > 0:  # Add empty line between jobs (but not after "jobs:")
                lines.append("")
            lines.append(f"  {job_name}:")

            # needs first if it exists
            if 'needs' in job:
                lines.append("    needs:")
                for need in job['needs']:
                    lines.append(f"      - {need}")

            # then other fields
            lines.append(f"    uses: {job['uses']}")
            lines.append("    with:")
            lines.append(f"      image: {job['with']['image']}")
            lines.append("    secrets:")
            for key, value in job['secrets'].items():
                lines.append(f"      {key}: {value}")

        return "\n".join(lines)


    def find_dockerfiles(self) -> Dict[str, Path]:
        """Find all Dockerfiles and their corresponding image names."""
        dockerfiles = {}

        # Find all Dockerfiles recursively
        for dockerfile in self.root_dir.rglob("Dockerfile"):
            # Skip .git and other hidden directories
            if any(part.startswith('.') for part in dockerfile.parts):
                continue

            # Generate image name from directory path
            image_name = self.path_to_image_name(dockerfile.parent)
            dockerfiles[image_name] = dockerfile

        return dockerfiles

    def find_dockerfiles_with_paths(self) -> Dict[str, Tuple[Path, str]]:
        """Find all Dockerfiles with their paths and directory paths for workflow."""
        dockerfiles = {}

        # Find all Dockerfiles recursively
        for dockerfile in self.root_dir.rglob("Dockerfile"):
            # Skip .git and other hidden directories
            if any(part.startswith('.') for part in dockerfile.parts):
                continue

            # Generate image name from directory path
            image_name = self.path_to_image_name(dockerfile.parent)
            dir_path = self.path_to_directory_path(dockerfile.parent)
            dockerfiles[image_name] = (dockerfile, dir_path)

        return dockerfiles

    def path_to_image_name(self, path: Path) -> str:
        """Convert a directory path to an image name."""
        # Get relative path from root
        rel_path = path.relative_to(self.root_dir)

        # Convert path segments to image name with dashes
        # e.g., rig-ubuntu/duckdb/dev -> rig-ubuntu-duckdb-dev
        return str(rel_path).replace('/', '-')

    def path_to_directory_path(self, path: Path) -> str:
        """Convert a directory path to the image directory path for workflow."""
        # Get relative path from root for use in workflow
        rel_path = path.relative_to(self.root_dir)
        return str(rel_path)

    def extract_base_image(self, dockerfile_path: Path) -> Optional[str]:
        """Extract the base image from a Dockerfile."""
        try:
            with open(dockerfile_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('FROM '):
                        # Extract the image name from FROM statement
                        from_parts = line.split()
                        if len(from_parts) >= 2:
                            base_image = from_parts[1]
                            return base_image
        except (IOError, OSError) as e:
            print(f"Error reading {dockerfile_path}: {e}")

        return None

    def normalize_image_name(self, image_name: str) -> Optional[str]:
        """
        Normalize image name to extract the local image name if it's from our registry.
        Returns None if it's an external image.
        """
        if not image_name:
            return None

        # Check if it's from our registry
        registry_prefix = f"{self.registry}/cynkra/docker-images/"

        if image_name.startswith(registry_prefix):
            # Extract the image name after the registry prefix
            local_name = image_name[len(registry_prefix):]
            # Remove :latest or other tags
            if ':' in local_name:
                local_name = local_name.split(':')[0]
            return local_name

        # If it's not from our registry, it's an external dependency
        return None

    def image_name_to_path(self, image_name: str) -> Optional[Path]:
        """Convert an image name back to its directory path."""
        # Handle legacy flat names and new nested names
        path_str = image_name.replace('-', '/')

        # Try the converted path first
        candidate_path = self.root_dir / path_str
        if (candidate_path / "Dockerfile").exists():
            return candidate_path

        # Fall back to checking all known dockerfiles
        dockerfiles = self.find_dockerfiles()
        for name, dockerfile_path in dockerfiles.items():
            if name == image_name:
                return dockerfile_path.parent

        return None

    def build_dependency_graph(self) -> Tuple[Dict[str, Set[str]], Dict[str, str]]:
        """
        Build a dependency graph of Docker images.

        Returns:
            dependencies: Dict mapping image -> set of images it depends on
            base_images: Dict mapping image -> its base image (for reference)
        """
        dockerfiles = self.find_dockerfiles()
        dependencies = defaultdict(set)
        base_images = {}

        for image_name, dockerfile_path in dockerfiles.items():
            base_image = self.extract_base_image(dockerfile_path)
            base_images[image_name] = base_image

            if base_image:
                local_dep = self.normalize_image_name(base_image)
                if local_dep and local_dep in dockerfiles:
                    dependencies[image_name].add(local_dep)

        return dict(dependencies), base_images

    def topological_sort(self, dependencies: Dict[str, Set[str]]) -> List[List[str]]:
        """
        Perform topological sort to determine build order.
        Returns list of stages, where each stage contains images that can be built in parallel.
        """
        # Calculate in-degrees
        in_degree = defaultdict(int)
        all_images = set(dependencies.keys())

        # Add all images that are dependencies but might not be in the keys
        for deps in dependencies.values():
            all_images.update(deps)

        # Only include images that we actually have Dockerfiles for
        dockerfiles = self.find_dockerfiles()
        all_images = {img for img in all_images if img in dockerfiles}

        # Calculate in-degrees
        for image in all_images:
            in_degree[image] = 0

        for image, deps in dependencies.items():
            if image in all_images:
                for dep in deps:
                    if dep in all_images:
                        in_degree[image] += 1

        # Topological sort using Kahn's algorithm
        stages = []
        queue = deque([img for img in all_images if in_degree[img] == 0])

        while queue:
            current_stage = []
            stage_size = len(queue)

            # Process all nodes with in-degree 0 in the current stage
            for _ in range(stage_size):
                image = queue.popleft()
                current_stage.append(image)

                # Reduce in-degree of dependent images
                for dependent, deps in dependencies.items():
                    if image in deps and dependent in all_images:
                        in_degree[dependent] -= 1
                        if in_degree[dependent] == 0:
                            queue.append(dependent)

            if current_stage:
                stages.append(sorted(current_stage))

        return stages

    def read_original_stages(self) -> dict:
        """Read the original stages.yml file."""
        stages_file = self.root_dir / ".github" / "workflows" / "stages.yml"

        try:
            with open(stages_file, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except (IOError, OSError) as e:
            print(f"Error reading original stages.yml: {e}")
            return {}

    def generate_fine_grained_stages(self) -> dict:
        """Generate the fine-grained stages configuration."""
        dependencies, _ = self.build_dependency_graph()

        # Get all images from Dockerfiles (source of truth) with their directory paths
        dockerfiles_with_paths = self.find_dockerfiles_with_paths()
        all_images = set(dockerfiles_with_paths.keys())

        # Create new configuration
        config = {
            'name': 'Create and publish a Docker image',
            'on': {
                'push': {'branches': ['main', 'dev']},
                'workflow_dispatch': None,
                'schedule': [{'cron': '0 0 * * *'}]
            },
            'env': {
                'REGISTRY': 'ghcr.io',
                'REPO_NAME': '${{ github.repository }}'
            },
            'jobs': {}
        }

        # Create a mapping from image name to job name (keep dashes, no suffix)
        def to_job_name(image: str) -> str:
            return image

        # Generate jobs for each image
        for image in sorted(all_images):
            job_name = to_job_name(image)
            _, dir_path = dockerfiles_with_paths[image]

            job_config = {}

            # Add specific dependencies for this image first (if any)
            image_deps = dependencies.get(image, set())
            if image_deps:
                job_config['needs'] = [to_job_name(dep) for dep in sorted(image_deps)]

            # Then add the rest of the job configuration
            # Use the directory path as the image parameter
            job_config.update({
                'uses': 'cynkra/docker-images/.github/workflows/publish.yml@main',
                'with': {'image': dir_path},
                'secrets': {
                    'DOCKERHUB_USERNAME': '${{ secrets.DOCKERHUB_USERNAME }}',
                    'DOCKERHUB_TOKEN': '${{ secrets.DOCKERHUB_TOKEN }}'
                }
            })

            config['jobs'][job_name] = job_config

        return config

    def print_dependency_info(self):
        """Print dependency information for debugging."""
        dependencies, base_images = self.build_dependency_graph()
        stages = self.topological_sort(dependencies)

        print("=== Docker Image Dependencies ===")
        print()

        print("Dependencies (image -> depends on):")
        for image, deps in sorted(dependencies.items()):
            if deps:
                print(f"  {image} -> {', '.join(sorted(deps))}")
            else:
                print(f"  {image} -> (no local dependencies)")

        print()
        print("Base images (for reference):")
        for image, base in sorted(base_images.items()):
            local_dep = self.normalize_image_name(base) if base else None
            if local_dep:
                print(f"  {image} <- {base} (local: {local_dep})")
            else:
                print(f"  {image} <- {base} (external)")

        print()
        print("Build stages:")
        for i, stage in enumerate(stages, 1):
            print(f"  Stage {i}: {', '.join(stage)}")

        print()


    def generate_comprehensive_analysis(self) -> str:
        """Generate a comprehensive analysis report."""
        dependencies, base_images = self.build_dependency_graph()
        stages = self.topological_sort(dependencies)
        dockerfiles = self.find_dockerfiles()

        report = []
        report.append("# Docker Image Dependency Analysis Report")
        report.append("")

        # Summary
        report.append("## Summary\n")
        report.append(f"- Total Dockerfiles found: {len(dockerfiles)}")
        report.append(f"- Images with local dependencies: {len([img for img in dependencies if dependencies[img]])}")
        report.append(f"- Build stages required: {len(stages)}")
        report.append("")

        # Dependency Tree
        report.append("## Dependency Tree\n")
        report.append("```text")
        for image in sorted(dockerfiles.keys()):
            base = base_images.get(image, "unknown")
            local_dep = self.normalize_image_name(base) if base else None

            if local_dep:
                report.append(f"✓ {image} ← {local_dep} ← {base}")
            else:
                report.append(f"✓ {image} ← {base} (external)")
        report.append("```")
        report.append("")

        # Build Order
        report.append("## Build Order (Topological Sort)\n")
        for i, stage in enumerate(stages, 1):
            report.append(f"### Stage {i}\n")
            for img in stage:
                report.append(f"- {img}")
            report.append("")
        report.append("")

        # External Dependencies
        external_deps = set()
        for image, base in base_images.items():
            local_dep = self.normalize_image_name(base) if base else None
            if not local_dep and base:
                external_deps.add(base)

        if external_deps:
            report.append("## External Dependencies\n")
            for dep in sorted(external_deps):
                images_using = [img for img, base in base_images.items()
                              if base == dep]
                report.append(f"- `{dep}` used by: {', '.join(images_using)}")
            report.append("")

        return "\n".join(report)


def main():
    """Main function."""
    script_dir = Path(__file__).parent
    analyzer = DockerImageAnalyzer(str(script_dir))

    print("Analyzing Docker image dependencies...")
    analyzer.print_dependency_info()

    print("Generating stages.yml...")
    config = analyzer.generate_fine_grained_stages()

    # Write to file
    output_file = script_dir / ".github" / "workflows" / "stages.yml"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(analyzer.format_yaml_output(config))

    print(f"Stages configuration written to: {output_file}")

    # Generate analysis report
    print("Generating analysis report...")
    analysis_report = analyzer.generate_comprehensive_analysis()

    analysis_file = script_dir / "DOCKER_DEPENDENCY_ANALYSIS.md"
    with open(analysis_file, 'w', encoding='utf-8') as f:
        f.write(analysis_report)

    print(f"Analysis report written to: {analysis_file}")


if __name__ == "__main__":
    main()

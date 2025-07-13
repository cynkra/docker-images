# Makefile for Docker Image Dependency Management

.PHONY: stages analysis clean help

# Default target
help:
	@echo "Available targets:"
	@echo "  stages   - Generate stages.yml from Dockerfiles"
	@echo "  analysis - Generate dependency analysis report"
	@echo "  clean    - Remove generated files"
	@echo "  help     - Show this help message"

# Generate stages.yml file
stages:
	@echo "Generating stages.yml from Dockerfiles..."
	python3 generate_stages.py

# Generate only the analysis report
analysis:
	@echo "Generating dependency analysis..."
	python3 -c "from generate_stages import DockerImageAnalyzer; import pathlib; analyzer = DockerImageAnalyzer('.'); report = analyzer.generate_comprehensive_analysis(); pathlib.Path('DOCKER_DEPENDENCY_ANALYSIS.md').write_text(report, encoding='utf-8'); print('Analysis written to DOCKER_DEPENDENCY_ANALYSIS.md')"

# Clean generated files
clean:
	@echo "Cleaning generated files..."
	rm -f .github/workflows/stages.yml
	rm -f DOCKER_DEPENDENCY_ANALYSIS.md
	rm -f stages-fine-grained.yml

# Validate generated YAML
validate: stages
	@echo "Validating generated YAML..."
	python3 -c "import yaml; yaml.safe_load(open('.github/workflows/stages.yml')); print('✓ YAML syntax is valid')"

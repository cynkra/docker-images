# Generated from github-docker/Makefile.j2, do not edit by hand
# Run 'make root-makefile' from github-docker to regenerate this file
# Makefile for Docker Image Dependency Management
# Delegates to ../github-docker for all code generation.

GITHUB_DOCKER := ../github-docker
PYTHON := $(GITHUB_DOCKER)/.venv/bin/python3
GENERATOR := $(PYTHON) $(GITHUB_DOCKER)/generate_stages.py --root .

.PHONY: stages analysis clean help update-from check-from generate-makefiles pr-build-script publish-yml pr-failure-comment-yml root-makefile

.NOTPARALLEL:

all: stages analysis update-from generate-makefiles pr-build-script

# Default target
help:
	@echo "Available targets:"
	@echo "  stages                  - Generate push.yml + stages.yml (PR) + build-pr-images.sh"
	@echo "  analysis                - Generate dependency analysis report"
	@echo "  update-from             - Update FROM instructions in Dockerfiles according to hierarchy"
	@echo "  check-from              - Check what FROM instructions would be updated (dry run)"
	@echo "  generate-makefiles      - Generate Makefiles alongside each Dockerfile"
	@echo "  pr-build-script         - Generate .github/build-pr-images.sh (no-push PR build)"
	@echo "  publish-yml             - Render publish.yml from template"
	@echo "  pr-failure-comment-yml  - Render pr-failure-comment.yml from template"
	@echo "  root-makefile           - Render this Makefile from template"
	@echo "  clean                   - Remove generated files"
	@echo "  help                    - Show this help message"

$(GITHUB_DOCKER)/.venv/pyvenv.cfg:
	$(MAKE) -C $(GITHUB_DOCKER) .venv/pyvenv.cfg

# Generate the workflows: push.yml (build+push, generated), stages.yml (PR,
# static copy) and .github/build-pr-images.sh, plus the analysis report.
stages: $(GITHUB_DOCKER)/.venv/pyvenv.cfg
	@echo "Generating push.yml + stages.yml + build-pr-images.sh from Dockerfiles..."
	@$(GENERATOR)

# Generate only the analysis report
analysis: $(GITHUB_DOCKER)/.venv/pyvenv.cfg
	@echo "Generating dependency analysis..."
	@$(GENERATOR) --analysis-only

# Clean generated files
clean:
	@echo "Cleaning generated files..."
	rm -f .github/workflows/stages.yml
	rm -f .github/workflows/push.yml
	rm -f .github/build-pr-images.sh
	rm -f DOCKER_DEPENDENCY_ANALYSIS.md

# Validate generated YAML
validate: stages
	@echo "Validating generated YAML..."
	@$(PYTHON) -c "import yaml; yaml.safe_load(open('.github/workflows/stages.yml')); yaml.safe_load(open('.github/workflows/push.yml')); print('✓ YAML syntax is valid')"

# Update FROM instructions in Dockerfiles according to directory hierarchy
update-from: $(GITHUB_DOCKER)/.venv/pyvenv.cfg
	@echo "Updating FROM instructions in Dockerfiles..."
	@$(GENERATOR) --update-from

# Check what FROM instructions would be updated (dry run)
check-from: $(GITHUB_DOCKER)/.venv/pyvenv.cfg
	@echo "Checking FROM instructions in Dockerfiles..."
	@$(GENERATOR) --update-from --dry-run

# Generate Makefiles alongside each Dockerfile
generate-makefiles: $(GITHUB_DOCKER)/.venv/pyvenv.cfg
	@echo "Generating Makefiles for all Dockerfiles..."
	@$(GENERATOR) --generate-makefiles

# Generate .github/build-pr-images.py (no-push PR build of changed images)
pr-build-script: $(GITHUB_DOCKER)/.venv/pyvenv.cfg
	@echo "Generating PR build script..."
	@$(GENERATOR) --generate-pr-build-script

# Render publish.yml.j2 template
publish-yml: $(GITHUB_DOCKER)/.venv/pyvenv.cfg
	@echo "Rendering publish.yml..."
	@$(GENERATOR) --generate-publish-yml

# Render pr-failure-comment.yml.j2 template
pr-failure-comment-yml: $(GITHUB_DOCKER)/.venv/pyvenv.cfg
	@echo "Rendering pr-failure-comment.yml..."
	@$(GENERATOR) --generate-pr-failure-comment-yml

# Render Makefile.j2 template (regenerate this file)
root-makefile: $(GITHUB_DOCKER)/.venv/pyvenv.cfg
	@echo "Rendering Makefile from template..."
	@$(GENERATOR) --generate-root-makefile

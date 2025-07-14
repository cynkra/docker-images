# Makefile for Docker Image Dependency Management

.PHONY: stages analysis clean help update-from check-from

all: stages analysis

# Default target
help:
	@echo "Available targets:"
	@echo "  stages     - Generate stages.yml from Dockerfiles"
	@echo "  analysis   - Generate dependency analysis report"
	@echo "  update-from - Update FROM instructions in Dockerfiles according to hierarchy"
	@echo "  check-from  - Check what FROM instructions would be updated (dry run)"
	@echo "  clean      - Remove generated files"
	@echo "  help       - Show this help message"

.venv:
	@echo "Creating Python virtual environment"
	@python3.11 -m venv .venv
	@touch requirements.txt
	@echo "To activate the virtual environment, run 'source .venv/bin/activate'"

.venv/pyvenv.cfg: requirements.txt .venv
	@echo "Installing requirements"
	@source .venv/bin/activate && pip install -r $<
	@touch $@


# Generate stages.yml file
stages: .venv/pyvenv.cfg
	@echo "Generating stages.yml from Dockerfiles..."
	@source .venv/bin/activate && python3 generate_stages.py

# Generate only the analysis report
analysis: .venv/pyvenv.cfg
	@echo "Generating dependency analysis..."
	@source .venv/bin/activate && python3 -c "from generate_stages import DockerImageAnalyzer; import pathlib; analyzer = DockerImageAnalyzer('.'); report = analyzer.generate_comprehensive_analysis(); pathlib.Path('DOCKER_DEPENDENCY_ANALYSIS.md').write_text(report, encoding='utf-8'); print('Analysis written to DOCKER_DEPENDENCY_ANALYSIS.md')"

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

# Update FROM instructions in Dockerfiles according to directory hierarchy
update-from: .venv/pyvenv.cfg
	@echo "Updating FROM instructions in Dockerfiles..."
	@source .venv/bin/activate && python3 generate_stages.py --update-from

# Check what FROM instructions would be updated (dry run)
check-from: .venv/pyvenv.cfg
	@echo "Checking FROM instructions in Dockerfiles..."
	@source .venv/bin/activate && python3 generate_stages.py --update-from --dry-run

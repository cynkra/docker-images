# Makefile for Docker image: tofutf
# Generated automatically - do not edit manually

.PHONY: build pull pull-parent run run-root clean help

# Default target
help:
	@echo "Available targets for tofutf:"
	@echo "  build      - Build the Docker image"
	@echo "  pull       - Pull the Docker image from registry"
	@echo "  pull-parent - Pull the parent image this image depends on"
	@echo "  run        - Run interactive bash as regular user"
	@echo "  run-root   - Run interactive bash as root user"
	@echo "  clean      - Remove the Docker image"
	@echo "  help       - Show this help message"

# Build the Docker image
build:
	@echo "Building Docker image: ghcr.io/cynkra/docker-images/tofutf:latest"
	docker build -t ghcr.io/cynkra/docker-images/tofutf:latest .

# Pull the Docker image from registry
pull:
	@echo "Pulling Docker image: ghcr.io/cynkra/docker-images/tofutf:latest"
	docker pull ghcr.io/cynkra/docker-images/tofutf:latest

# Pull the parent image this image depends on
pull-parent:
	@echo "Pulling parent image: ghcr.io/tofutf/tofutf/tofutfd:v0.10.0-4-g1de178b7"
	docker pull ghcr.io/tofutf/tofutf/tofutfd:v0.10.0-4-g1de178b7

# Run interactive bash as regular user
run:
	@echo "Starting interactive bash session in ghcr.io/cynkra/docker-images/tofutf:latest"
	docker run --rm -it ghcr.io/cynkra/docker-images/tofutf:latest /bin/bash

# Run interactive bash as root user
run-root:
	@echo "Starting interactive bash session as root in ghcr.io/cynkra/docker-images/tofutf:latest"
	docker run --rm -it --user root ghcr.io/cynkra/docker-images/tofutf:latest /bin/bash

# Remove the Docker image
clean:
	@echo "Removing Docker image: ghcr.io/cynkra/docker-images/tofutf:latest"
	docker rmi ghcr.io/cynkra/docker-images/tofutf:latest || true

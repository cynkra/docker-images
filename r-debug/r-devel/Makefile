# Makefile for Docker image: r-debug-r-devel
# Generated automatically - do not edit manually

.PHONY: build pull pull-parent run run-root clean help

# Default target
help:
	@echo "Available targets for r-debug-r-devel:"
	@echo "  build      - Build the Docker image"
	@echo "  pull       - Pull the Docker image from registry"
	@echo "  pull-parent - Pull the parent image this image depends on"
	@echo "  run        - Run interactive bash as regular user"
	@echo "  run-root   - Run interactive bash as root user"
	@echo "  clean      - Remove the Docker image"
	@echo "  help       - Show this help message"

# Build the Docker image
build:
	@echo "Building Docker image: ghcr.io/cynkra/docker-images/r-debug-r-devel:latest"
	@echo "Creating date file for cache invalidation..."
	@date > date.txt
	@docker build -t ghcr.io/cynkra/docker-images/r-debug-r-devel:latest .
	@echo "Build completed: ghcr.io/cynkra/docker-images/r-debug-r-devel:latest"

# Pull the Docker image from registry
pull:
	@echo "Pulling Docker image: ghcr.io/cynkra/docker-images/r-debug-r-devel:latest"
	@docker pull ghcr.io/cynkra/docker-images/r-debug-r-devel:latest

# Pull the parent image
pull-parent:
	@echo "Pulling parent image: ubuntu:22.04"
	@docker pull ubuntu:22.04

# Run interactive bash as regular user
run:
	@echo "Running interactive container with ghcr.io/cynkra/docker-images/r-debug-r-devel:latest"
	@docker run --rm -it ghcr.io/cynkra/docker-images/r-debug-r-devel:latest /bin/bash

# Run interactive bash as root user
run-root:
	@echo "Running interactive container as root with ghcr.io/cynkra/docker-images/r-debug-r-devel:latest"
	@docker run --rm -it --user root ghcr.io/cynkra/docker-images/r-debug-r-devel:latest /bin/bash

# Remove the Docker image
clean:
	@echo "Removing Docker image: ghcr.io/cynkra/docker-images/r-debug-r-devel:latest"
	@docker rmi ghcr.io/cynkra/docker-images/r-debug-r-devel:latest || true

# Build dependencies (for automated builds)
.build-deps:

# Makefile for Docker image: rig-debian
# Generated automatically - do not edit manually

.PHONY: build pull pull-parent run run-root clean help

# Default target
help:
	@echo "Available targets for rig-debian:"
	@echo "  build      - Build the Docker image"
	@echo "  pull       - Pull the Docker image from registry"
	@echo "  pull-parent - Pull the parent image this image depends on"
	@echo "  run        - Run interactive bash as regular user"
	@echo "  run-root   - Run interactive bash as root user"
	@echo "  clean      - Remove the Docker image"
	@echo "  help       - Show this help message"

# Build the Docker image
build:
	@echo "Building Docker image: ghcr.io/cynkra/docker-images/rig-debian:latest"
	@echo "Creating date file for cache invalidation..."
	@date -Idate > date.txt
	@trap 'rm -f date.txt' EXIT; docker build -t ghcr.io/cynkra/docker-images/rig-debian:latest .

# Pull the Docker image from registry
pull:
	@echo "Pulling Docker image: ghcr.io/cynkra/docker-images/rig-debian:latest"
	docker pull ghcr.io/cynkra/docker-images/rig-debian:latest

# Pull the parent image this image depends on
pull-parent:
	@echo "Pulling parent image: debian:bookworm"
	docker pull debian:bookworm

# Run interactive bash as regular user
run:
	@echo "Starting interactive bash session in ghcr.io/cynkra/docker-images/rig-debian:latest"
	docker run --rm -it ghcr.io/cynkra/docker-images/rig-debian:latest /bin/bash

# Run interactive bash as root user
run-root:
	@echo "Starting interactive bash session as root in ghcr.io/cynkra/docker-images/rig-debian:latest"
	docker run --rm -it --user root ghcr.io/cynkra/docker-images/rig-debian:latest /bin/bash

# Remove the Docker image
clean:
	@echo "Removing Docker image: ghcr.io/cynkra/docker-images/rig-debian:latest"
	docker rmi ghcr.io/cynkra/docker-images/rig-debian:latest || true

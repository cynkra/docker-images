# Makefile for Docker image: rig-ubuntu-duckdb4
# Generated automatically - do not edit manually

.PHONY: build run run-root clean help

# Default target
help:
	@echo "Available targets for rig-ubuntu-duckdb4:"
	@echo "  build      - Build the Docker image"
	@echo "  run        - Run interactive bash as regular user"
	@echo "  run-root   - Run interactive bash as root user"
	@echo "  clean      - Remove the Docker image"
	@echo "  help       - Show this help message"

# Build the Docker image
build:
	@echo "Building Docker image: ghcr.io/cynkra/docker-images/rig-ubuntu-duckdb4:latest"
	docker build -t ghcr.io/cynkra/docker-images/rig-ubuntu-duckdb4:latest .

# Run interactive bash as regular user
run: build
	@echo "Starting interactive bash session in ghcr.io/cynkra/docker-images/rig-ubuntu-duckdb4:latest"
	docker run --rm -it ghcr.io/cynkra/docker-images/rig-ubuntu-duckdb4:latest /bin/bash

# Run interactive bash as root user
run-root: build
	@echo "Starting interactive bash session as root in ghcr.io/cynkra/docker-images/rig-ubuntu-duckdb4:latest"
	docker run --rm -it --user root ghcr.io/cynkra/docker-images/rig-ubuntu-duckdb4:latest /bin/bash

# Remove the Docker image
clean:
	@echo "Removing Docker image: ghcr.io/cynkra/docker-images/rig-ubuntu-duckdb4:latest"
	docker rmi ghcr.io/cynkra/docker-images/rig-ubuntu-duckdb4:latest || true

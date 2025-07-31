# Makefile for Docker image: sops-age
# Generated automatically - do not edit manually

.PHONY: build run run-root clean help

# Default target
help:
	@echo "Available targets for sops-age:"
	@echo "  build      - Build the Docker image"
	@echo "  run        - Run interactive bash as regular user"
	@echo "  run-root   - Run interactive bash as root user"
	@echo "  clean      - Remove the Docker image"
	@echo "  help       - Show this help message"

# Build the Docker image
build:
	@echo "Building Docker image: ghcr.io/cynkra/docker-images/sops-age:latest"
	docker build -t ghcr.io/cynkra/docker-images/sops-age:latest .

# Run interactive bash as regular user
run: build
	@echo "Starting interactive bash session in ghcr.io/cynkra/docker-images/sops-age:latest"
	docker run --rm -it ghcr.io/cynkra/docker-images/sops-age:latest /bin/bash

# Run interactive bash as root user
run-root: build
	@echo "Starting interactive bash session as root in ghcr.io/cynkra/docker-images/sops-age:latest"
	docker run --rm -it --user root ghcr.io/cynkra/docker-images/sops-age:latest /bin/bash

# Remove the Docker image
clean:
	@echo "Removing Docker image: ghcr.io/cynkra/docker-images/sops-age:latest"
	docker rmi ghcr.io/cynkra/docker-images/sops-age:latest || true

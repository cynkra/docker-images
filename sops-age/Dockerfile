# Use a lightweight Alpine-based image
FROM alpine:latest

# Install required packages
RUN apk add --no-cache \
    git \
    curl \
    bash \
    jq \
    age \
    sops

# Set default working directory
WORKDIR /repo

# Set entrypoint for running SOPS, Age, or Git commands
ENTRYPOINT ["/bin/sh"]

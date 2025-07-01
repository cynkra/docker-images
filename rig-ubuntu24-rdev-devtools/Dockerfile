FROM ghcr.io/cynkra/docker-images/rig-ubuntu24-rdev:latest

# Install common development tools
RUN apt-get update && apt-get install -y \
    git \
    vim \
    nano \
    htop \
    tree \
    wget \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install R development packages
RUN R-devel -q -e 'pak::pak(c("devtools", "usethis", "languageserver"))'

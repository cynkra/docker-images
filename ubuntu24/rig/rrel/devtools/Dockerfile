FROM ghcr.io/cynkra/docker-images/ubuntu24-rig-rrel:latest

# Install common development tools
RUN \
  apt-get update && \
  apt-get install -y git vim nano htop tree wget ca-certificates wget gpg gnupg gnupg2 && \
  update-alternatives --set editor /usr/bin/vim.basic && \
  rm -rf /var/lib/apt/lists/* && \
  true

# Install R development packages and clean up
RUN \
  R -q -e 'pak::pak(c("devtools", "usethis", "languageserver"))' && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true


FROM ghcr.io/cynkra/docker-images/ubuntu24-rig-rdev:latest

# Install common development tools
RUN \
  apt-get update && \
  apt-get install -y git vim htop tree wget ca-certificates wget gpg gnupg gnupg2 && \
  update-alternatives --set editor /usr/bin/vim.basic && \
  rm -rf /var/lib/apt/lists/* && \
  true

USER ubuntu

WORKDIR /home/ubuntu

RUN \
  mkdir .R && \
  echo 'MAKEFLAGS=-j4' > .R/Makevars && \
  touch .hushlogin && \
  true

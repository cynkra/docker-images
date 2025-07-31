FROM ghcr.io/cynkra/docker-images/ubuntu24:latest

# Install system packages, configure locale, install rig, and set up R configuration
RUN \
  apt-get update && \
  apt-get install -y --no-install-recommends curl sudo ccache && \
  /usr/sbin/update-ccache-symlinks && \
  \
  curl -Ls https://github.com/r-lib/rig/releases/download/v0.7.1/rig-linux-0.7.1.tar.gz | sudo tar xz -C /usr/local && \
  \
  mkdir /root/.R && \
  echo 'MAKEFLAGS=-j4' > /root/.R/Makevars && \
  \
  ( echo '#/bin/sh'; echo 'set -e'; echo 'rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*' ) > /usr/local/bin/apt-cleanup.sh && \
  chmod +x /usr/local/bin/apt-cleanup.sh && \
  \
  apt-cleanup.sh && \
  true

WORKDIR /root/workspace

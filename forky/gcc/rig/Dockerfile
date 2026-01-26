FROM ghcr.io/cynkra/docker-images/forky-gcc:latest

ARG TARGETARCH=arm64

# Install system packages and R via apt (rig doesn't support Trixie yet)
RUN \
  apt-get update && \
  apt-get install -y --no-install-recommends curl sudo ccache ca-certificates r-base r-base-dev && \
  /usr/sbin/update-ccache-symlinks && \
  \
  # TODO: Use rig when Trixie is supported
  # if [ "$TARGETARCH" = "arm64" ]; then \
  #   RIG_ARCH="rig-linux-arm64"; \
  # else \
  #   RIG_ARCH="rig-linux"; \
  # fi && \
  # curl -Ls https://github.com/r-lib/rig/releases/download/v0.7.1/${RIG_ARCH}-0.7.1.tar.gz | sudo tar xz -C /usr/local && \
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

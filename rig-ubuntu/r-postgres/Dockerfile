# arch: amd64

FROM ghcr.io/cynkra/docker-images/rig-ubuntu:latest

# Install system dependencies, set up workspace, and install R packages
RUN \
  apt-get update && \
  apt-get install -y gnupg lsb-release time postgresql-client && \
  mkdir -p /root/workspace && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true


COPY DESCRIPTION /root/workspace

RUN \
  R -q -e 'pak::pak(dependencies = c("soft", "Config/Needs/build"))' && \
  true


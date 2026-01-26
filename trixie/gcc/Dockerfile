FROM ghcr.io/cynkra/docker-images/trixie:latest

ARG TARGETARCH=arm64

# Install GCC (latest available in Trixie), configure alternatives, and set compiler flags
RUN \
  apt-get update && \
  apt-get install -y gcc g++ cpp build-essential && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true

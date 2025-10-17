# arch: amd64

FROM ghcr.io/cynkra/docker-images/rig-ubuntu:latest

# Install system dependencies and R packages, then clean up
RUN \
  apt-get update && \
  apt-get install -y python3 && \
  apt-get install -y ninja-build && \
  apt-get install -y cmake && \
  R -q -e 'pak::pak(c("duckplyr", "cpp11", "decor", "devtools"), dependencies = TRUE)' && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true && \
  true


ENV DUCKDB_R_DEBUG 1

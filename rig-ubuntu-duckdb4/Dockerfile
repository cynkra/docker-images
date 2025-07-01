FROM ghcr.io/cynkra/docker-images/rig-ubuntu:latest

# Install system dependencies, R 4.1, and R packages, then clean up
RUN \
  apt-get update && \
  apt-get install -y \ python3  ninja-build  cmake && \
  rig add 4.1 && \
  R-4.1.3 -q -e 'pak::pak(c("duckdb", "cpp11", "decor", "devtools"), dependencies = TRUE)' && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true


ENV DUCKDB_R_DEBUG 1

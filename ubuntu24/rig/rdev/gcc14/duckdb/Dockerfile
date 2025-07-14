FROM ghcr.io/cynkra/docker-images/ubuntu24-rig-rdev-gcc14:latest

# Install system dependencies and R packages, then clean up
RUN \
  apt-get update && \
  apt-get install -y python3  ninja-build  cmake && \
  R-devel -q -e 'pak::pak(c("DBI", "cpp11"))' && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true


ENV DUCKDB_R_DEBUG 1

FROM ghcr.io/cynkra/docker-images/trixie-gcc-rig-rdev:latest

# Install system dependencies, R packages, clone duckdb, and build it
RUN \
  apt-get update && \
  apt-get install -y git python3 ninja-build cmake && \
  R-devel -q -e 'pak::pak(c("DBI", "cpp11"))' && \
  git clone --depth 1 https://github.com/duckdb/duckdb.git /root/duckdb && \
  cd /root/duckdb/tools/rpkg && \
  R-devel CMD INSTALL . && \
  cd /root && \
  rm -rf /root/duckdb && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true

ENV DUCKDB_R_DEBUG 1

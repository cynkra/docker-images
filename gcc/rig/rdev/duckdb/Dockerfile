FROM ghcr.io/cynkra/docker-images/gcc-latest-rig-rdev:latest

# Install system dependencies, R packages, clone duckdb, and build it
RUN \
  apt-get update && \
  apt-get install -y git python3 ninja-build cmake && \
  R -q -e 'install.packages(c("DBI", "cpp11"), repos="https://cloud.r-project.org")' && \
  git clone --depth 1 https://github.com/duckdb/duckdb-r.git /root/duckdb && \
  cd /root/duckdb && \
  R CMD INSTALL . && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true

ENV DUCKDB_R_DEBUG 1

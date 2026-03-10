# R-devel with duckdb compiled from source and duckplyr
# Clones and compiles duckdb using all available cores, with duckplyr and suggested packages
#
# Usage:
#   docker run --rm -ti --name rd-duckdb cynkra/r-debug-duckdb
#   RD # to start R-devel with duckdb

FROM ghcr.io/cynkra/docker-images/r-debug:latest

LABEL maintainer="cynkra <team@cynkra.com>"
LABEL org.opencontainers.image.source="https://github.com/cynkra/docker-images"

RUN \
    apt-get update && \
    RD -q -e 'pak::pak("DBI")' && \
    mkdir -p /clone && \
    cd /clone && \
    git clone https://github.com/duckdb/duckdb-r.git && \
    cd duckdb-r && \
    MAKEFLAGS=-j$(nproc) RD CMD INSTALL . --no-byte-compile && \
    RD -q -e 'pak::pak("duckplyr", dependencies = TRUE)' && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/* && \
    rm -rf /var/tmp/* && \
    true

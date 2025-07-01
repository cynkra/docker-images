FROM ghcr.io/cynkra/docker-images/rig-ubuntu-duckdb:latest

COPY date.txt /date.txt

# Clone and install development versions of duckdb-r and duckplyr, then clean up
RUN \
  mkdir -p /clone && \
  cd /clone && \
  git clone https://github.com/duckdb/duckdb-r.git && \
  cd duckdb-r && \
  UserNM=true MAKEFLAGS=-j2 R CMD INSTALL . --no-byte-compile && \
  cd .. && \
  git clone https://github.com/tidyverse/duckplyr.git && \
  cd duckplyr && \
  UserNM=true R CMD INSTALL . --no-byte-compile && \
  cd / && \
  rm -rf /clone && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true


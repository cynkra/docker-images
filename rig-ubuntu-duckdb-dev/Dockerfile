FROM ghcr.io/cynkra/docker-images/rig-ubuntu-duckdb:latest

RUN R -q -e 'pak::pak(c("tidyverse/duckplyr", "duckdb/duckdb-r"))'

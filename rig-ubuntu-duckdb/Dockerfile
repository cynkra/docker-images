FROM ghcr.io/cynkra/docker-images/rig-ubuntu:latest

RUN apt-get install -y python3 ninja-build cmake

RUN R -q -e 'pak::pak(c("duckplyr", "cpp11", "decor", "devtools"), dependencies = TRUE)'

ENV DUCKDB_R_DEBUG 1

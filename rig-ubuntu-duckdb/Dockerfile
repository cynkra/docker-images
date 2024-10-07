FROM ghcr.io/cynkra/docker-images/rig-ubuntu:latest

RUN apt-get install -y python3

RUN R -q -e 'pak::pak(c("duckdb", "cpp11", "decor", "devtools"), dependencies = TRUE)'

RUN apt-get install -y ninja-build

RUN apt-get install -y cmake

ENV DUCKDB_R_DEBUG 1

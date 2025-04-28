FROM ghcr.io/cynkra/docker-images/rig-ubuntu:latest

RUN apt-get install -y python3 ninja-build cmake

RUN rig add 4.1

RUN R-4.1.3 -q -e 'pak::pak(c("duckdb", "cpp11", "decor", "devtools"), dependencies = TRUE)'

ENV DUCKDB_R_DEBUG 1

FROM ghcr.io/cynkra/docker-images/rig-ubuntu24-gcc14:latest

RUN apt-get install -y python3 ninja-build cmake

RUN R-devel -q -e 'pak::pak(c("DBI", "cpp11"))'

ENV DUCKDB_R_DEBUG 1

FROM ghcr.io/cynkra/docker-images/rig-ubuntu:latest

RUN apt-get install -y gnupg lsb-release time

RUN R       -q -e 'pak::pak(c("DBI", "RMariaDB", "RPostgres", "RSQLite", "dm", "duckdb", "odbc", "adbi", "cpp11", "devtools", "decor", "plogr", "reprex"), dependencies = TRUE)'

RUN R-devel -q -e 'pak::pak(c("DBI", "RMariaDB", "RPostgres", "RSQLite", "dm", "duckdb", "odbc", "adbi", "cpp11", "devtools", "decor", "plogr", "reprex"), dependencies = TRUE)'

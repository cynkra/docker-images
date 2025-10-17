# arch: amd64

FROM ghcr.io/cynkra/docker-images/rig-ubuntu:latest

# Install system dependencies and R packages for both R versions, then clean up
RUN \
  apt-get update && \
  apt-get install -y gnupg lsb-release time && \
  R       -q -e 'pak::pak(c("DBI", "RMariaDB", "RPostgres", "RSQLite", "dm", "duckdb", "odbc", "adbi", "cpp11", "devtools", "decor", "plogr", "reprex"), dependencies = TRUE)' && \
  R-devel -q -e 'pak::pak(c("DBI", "RMariaDB", "RPostgres", "RSQLite", "dm", "duckdb", "odbc", "adbi", "cpp11", "devtools", "decor", "plogr", "reprex"), dependencies = TRUE)' && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true


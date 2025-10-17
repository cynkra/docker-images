# arch: amd64

FROM ghcr.io/cynkra/docker-images/rig-ubuntu:latest

COPY DESCRIPTION /root/workspace

# Install R packages, system dependencies and ODBC driver, then clean up
RUN \
  mkdir -p /root/workspace && \
  R -q -e 'pak::pak()' && \
  apt-get update && \
  apt-get install -y gnupg lsb-release time && \
  curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
  curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
  apt-get update && \
  ACCEPT_EULA=Y apt-get install -y msodbcsql18 && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true


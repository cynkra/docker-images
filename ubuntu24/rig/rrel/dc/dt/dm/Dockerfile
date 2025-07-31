FROM ghcr.io/cynkra/docker-images/ubuntu24-rig-rrel-dc-dt:latest

USER root

# https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver16&tabs=ubuntu18-install%2Calpine17-install%2Cdebian8-install%2Credhat7-13-install%2Crhel7-offline
RUN \
  curl -sSL -O https://packages.microsoft.com/config/ubuntu/$(grep VERSION_ID /etc/os-release | cut -d '"' -f 2)/packages-microsoft-prod.deb && \
  dpkg -i packages-microsoft-prod.deb && \
  rm packages-microsoft-prod.deb && \
  \
  apt-get update && \
  ACCEPT_EULA=Y apt-get install -y --no-install-recommends msodbcsql18 && \
  ACCEPT_EULA=Y apt-get install -y mssql-tools18 && \
  ln -s /opt/mssql-tools18/bin/* /usr/local/bin/ && \
  cd /opt/microsoft/msodbcsql18/lib64 && \
  ln -s libmsodbcsql-18.*.so.* libmsodbcsql-18.so && \
  ln -s libmsodbcsql-18.*.so.* libmsodbcsql.so && \
  cd - && \
  \
  apt-get install -y unixodbc-dev && \
  \
  ( echo "[ODBC Driver 18 for SQL Server]"; \
    echo "Description=Microsoft ODBC Driver 18 for SQL Server"; \
    echo "Driver=/opt/microsoft/msodbcsql18/lib64/libmsodbcsql-18.so"; \
    echo "UsageCount=1" ) > /etc/odbcinst.ini && \
  ( echo "[mssql-test]"; \
    echo "Description=Test connection to Microsoft SQL Server"; \
    echo "Driver=ODBC Driver 18 for SQL Server"; \
    echo "Server=localhost"; \
    echo "Port=1433" ) > /etc/odbc.ini && \
  \
  apt-cleanup.sh && \
  true

USER ubuntu

# The parts above are okay to be a little older
COPY date.txt /date.txt

RUN \
  PKG_SYSREQS=true R -q -e 'pak::pak("cynkra/dm", dependencies = TRUE)' && \
  sudo apt-cleanup.sh && \
  rm -rf ~/.cache && \
  true

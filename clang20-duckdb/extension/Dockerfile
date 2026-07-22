# arch: amd64

FROM ghcr.io/cynkra/docker-images/clang20-duckdb:latest

COPY date.txt /date.txt

# Attempt to install and load the DuckDB `spatial` extension on top of a duckdb
# R package that was compiled from source with clang, reproducing the REPREX in
# duckdb/duckdb-r#1107.
#
# INSTALL and LOAD must run in the SAME R session: duckdb caches downloaded
# extensions in a per-session temp directory, so a LOAD in a fresh session can't
# see an extension INSTALLed by a previous one ("Extension not found"). PRAGMA
# version / platform are printed first for diagnostics (the issue thread asked
# for both). The whole attempt is guarded so the expected crash (or any other
# failure) is captured in the build log without turning CI red; `docker run` the
# image (default CMD) to reproduce it directly.
RUN { R -q -e 'library(duckdb); con <- dbConnect(duckdb()); print(dbGetQuery(con, "PRAGMA version")); print(dbGetQuery(con, "PRAGMA platform")); print(dbExecute(con, "INSTALL spatial")); dbExecute(con, "LOAD spatial")' || echo "INSTALL/LOAD spatial failed (exit $?) -- see duckdb/duckdb-r#1107"; } && \
    rm -rf /tmp/* && \
    rm -rf /var/tmp/* && \
    true

CMD ["R", "-q", "-e", "library(duckdb); con <- dbConnect(duckdb()); dbExecute(con, 'INSTALL spatial'); dbExecute(con, 'LOAD spatial')"]

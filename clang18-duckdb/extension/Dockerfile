# arch: amd64

FROM ghcr.io/cynkra/docker-images/clang18-duckdb:latest

COPY date.txt /date.txt

# Attempt to install and load the DuckDB `spatial` extension on top of a
# duckdb R package that was compiled from source with clang.
#
# This reproduces duckdb/duckdb-r#1107: `INSTALL` downloads the prebuilt
# extension binary and succeeds, but `LOAD` segfaults R because the prebuilt
# extension is ABI-incompatible with a clang-built duckdb-r. PRAGMA version /
# platform are printed first for diagnostics (see the issue thread). Both steps
# are guarded so the expected crash is captured in the build log without turning
# CI red; `docker run` the image (default CMD) to reproduce the crash directly.
RUN { R -q -e 'library(duckdb); con <- dbConnect(duckdb()); print(dbGetQuery(con, "PRAGMA version")); print(dbGetQuery(con, "PRAGMA platform")); print(dbExecute(con, "INSTALL spatial"))' || echo "INSTALL spatial failed (exit $?) -- see duckdb/duckdb-r#1107"; } && \
    { R -q -e 'library(duckdb); con <- dbConnect(duckdb()); dbExecute(con, "LOAD spatial")' || echo "LOAD spatial failed (exit $?) -- see duckdb/duckdb-r#1107"; } && \
    rm -rf /tmp/* && \
    rm -rf /var/tmp/* && \
    true

CMD ["R", "-q", "-e", "library(duckdb); con <- dbConnect(duckdb()); dbExecute(con, 'INSTALL spatial'); dbExecute(con, 'LOAD spatial')"]

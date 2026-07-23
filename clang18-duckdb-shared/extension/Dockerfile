# arch: amd64

FROM ghcr.io/cynkra/docker-images/clang18-duckdb-shared:latest

COPY date.txt /date.txt

# Same extension attempt as clang18-duckdb/extension, but the parent duckdb R
# package is linked against the SHARED libduckdb (the official engine) rather
# than a clang-compiled vendored engine. The question for duckdb/duckdb-r#1107:
# does the prebuilt `spatial` extension now LOAD cleanly, or still segfault?
#
# INSTALL and LOAD run in the SAME R session (duckdb caches extensions per
# session). PRAGMA version / platform are printed first. The attempt is guarded
# so either outcome (clean load or crash) is captured without turning CI red;
# `docker run` the image (default CMD) to see it directly.
RUN { R -q -e 'library(duckdb); con <- dbConnect(duckdb()); print(dbGetQuery(con, "PRAGMA version")); print(dbGetQuery(con, "PRAGMA platform")); print(dbExecute(con, "INSTALL spatial")); dbExecute(con, "LOAD spatial"); cat("LOAD spatial: OK\n")' || echo "INSTALL/LOAD spatial failed (exit $?) -- see duckdb/duckdb-r#1107"; } && \
    rm -rf /tmp/* && \
    rm -rf /var/tmp/* && \
    true

CMD ["R", "-q", "-e", "library(duckdb); con <- dbConnect(duckdb()); dbExecute(con, 'INSTALL spatial'); dbExecute(con, 'LOAD spatial')"]

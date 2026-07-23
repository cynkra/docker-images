# arch: amd64

FROM ghcr.io/cynkra/docker-images/clang18-duckdb:latest

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
#
# Then run the FULL duckdb R package test suite against this same installed
# (clang-compiled) duckdb, to surface any crash/failure beyond the spatial LOAD.
# The duckdb-r source is cloned at the tag matching the installed version and the
# tests run with the package's internal namespace (env = asNamespace("duckdb")),
# mirroring what test_check() does under R CMD check; test dependencies are
# pulled as Posit P3M binaries (fast, no clang recompile). Optional Suggests that
# are absent just skip their tests. This step is guarded too -- a failing or
# crashing test is an informative result for these reproduction images, not a
# reason to turn CI red.
RUN { R -q -e 'library(duckdb); con <- dbConnect(duckdb()); print(dbGetQuery(con, "PRAGMA version")); print(dbGetQuery(con, "PRAGMA platform")); print(dbExecute(con, "INSTALL spatial")); dbExecute(con, "LOAD spatial")' || echo "INSTALL/LOAD spatial failed (exit $?) -- see duckdb/duckdb-r#1107"; } ; \
    { \
      DUCKDB_VER="$(R -q -e 'cat(as.character(packageVersion("duckdb")))' | tail -n1)"; \
      CODENAME="$(. /etc/os-release && echo "$VERSION_CODENAME")"; \
      P3M_URL="https://packagemanager.posit.co/cran/__linux__/${CODENAME}/latest"; \
      echo "=== running full duckdb ${DUCKDB_VER} test suite (distro ${CODENAME}) ==="; \
      { git clone --depth 1 --branch "v${DUCKDB_VER}" https://github.com/duckdb/duckdb-r /tmp/duckdb-r-tests || \
        git clone --depth 1 https://github.com/duckdb/duckdb-r /tmp/duckdb-r-tests; } && \
      R -q -e "options(HTTPUserAgent = sprintf('R/%s R (%s)', getRversion(), paste(getRversion(), R.version[['platform']], R.version[['arch']], R.version[['os']]))); options(repos = c(P3M = '${P3M_URL}', CRAN = 'https://cloud.r-project.org')); install.packages(c('testthat', 'DBItest', 'withr', 'rlang', 'bit64', 'tibble', 'vctrs', 'clock', 'callr', 'dplyr', 'dbplyr', 'nanoarrow'))" && \
      ( cd /tmp/duckdb-r-tests && DUCKDB_R_RUN_TESTS=true R -q -e 'library(duckdb); testthat::test_dir("tests/testthat", package = "duckdb", env = asNamespace("duckdb"), stop_on_failure = FALSE, reporter = "summary")' ); \
      echo "=== duckdb test suite finished (exit $?) ==="; \
    } || echo "duckdb test suite step errored (exit $?)" ; \
    rm -rf /tmp/* && \
    rm -rf /var/tmp/* && \
    true

CMD ["R", "-q", "-e", "library(duckdb); con <- dbConnect(duckdb()); dbExecute(con, 'INSTALL spatial'); dbExecute(con, 'LOAD spatial')"]

# arch: amd64

FROM ghcr.io/cynkra/docker-images/clang20-duckdb-shared:latest

COPY date.txt /date.txt

# Same extension attempt as clang20-duckdb/extension, but the parent duckdb R
# package is linked against the SHARED libduckdb (the official engine) rather
# than a clang-compiled vendored engine. The question for duckdb/duckdb-r#1107:
# does the prebuilt `spatial` extension now LOAD cleanly, or still segfault?
#
# INSTALL and LOAD run in the SAME R session (duckdb caches extensions per
# session). PRAGMA version / platform are printed first. The attempt is guarded
# so either outcome (clean load or crash) is captured without turning CI red;
# `docker run` the image (default CMD) to see it directly.
#
# Then run the FULL duckdb R package test suite against this same installed
# (shared-libduckdb-linked) duckdb, to surface any crash/failure beyond the
# spatial LOAD. The parent image installed duckdb with `--install-tests`, so this
# uses the sanctioned `testthat::test_package("duckdb")` runner (which sets up the
# proper test environment itself). Test dependencies are pulled as Posit P3M
# binaries (fast, no clang recompile); NOT_CRAN / DUCKDB_R_RUN_TESTS opt the
# suite in; absent optional Suggests just skip their tests. This step is guarded
# too -- a failing or crashing test is an informative result for these
# reproduction images, not a reason to turn CI red.
RUN { R -q -e 'library(duckdb); con <- dbConnect(duckdb()); print(dbGetQuery(con, "PRAGMA version")); print(dbGetQuery(con, "PRAGMA platform")); print(dbExecute(con, "INSTALL spatial")); dbExecute(con, "LOAD spatial"); cat("LOAD spatial: OK\n")' || echo "INSTALL/LOAD spatial failed (exit $?) -- see duckdb/duckdb-r#1107"; } ; \
    { \
      CODENAME="$(. /etc/os-release && echo "$VERSION_CODENAME")"; \
      P3M_URL="https://packagemanager.posit.co/cran/__linux__/${CODENAME}/latest"; \
      echo "=== running full duckdb test suite (distro ${CODENAME}) ==="; \
      R -q -e "options(HTTPUserAgent = sprintf('R/%s R (%s)', getRversion(), paste(getRversion(), R.version[['platform']], R.version[['arch']], R.version[['os']]))); options(repos = c(P3M = '${P3M_URL}', CRAN = 'https://cloud.r-project.org')); install.packages(c('testthat', 'DBItest', 'withr', 'rlang', 'bit64', 'tibble', 'vctrs', 'clock', 'callr', 'dplyr', 'dbplyr', 'nanoarrow'))" && \
      NOT_CRAN=true DUCKDB_R_RUN_TESTS=true R -q -e 'testthat::test_package("duckdb", reporter = "summary", stop_on_failure = FALSE)' ; \
      echo "=== duckdb test suite finished (exit $?) ==="; \
    } || echo "duckdb test suite step errored (exit $?)" ; \
    rm -rf /tmp/* && \
    rm -rf /var/tmp/* && \
    true

CMD ["R", "-q", "-e", "library(duckdb); con <- dbConnect(duckdb()); dbExecute(con, 'INSTALL spatial'); dbExecute(con, 'LOAD spatial')"]

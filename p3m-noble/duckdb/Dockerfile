# arch: amd64, arm64

# duckdb binary package + extensions on the P3M Ubuntu 24.04 (Noble) base image.
#
# Installs the duckdb R package from the P3M binary repository configured in
# the parent image, then INSTALLs and LOADs every extension listed in
# duckdb-extensions.txt (part of the build context). Doing this at build time
# verifies each extension is available as a prebuilt binary for this OS/arch
# (the build fails otherwise) and pre-caches the extensions into the image at
# $DUCKDB_EXTENSION_DIRECTORY so downstream consumers can load them offline.

FROM ghcr.io/cynkra/docker-images/p3m-noble:latest

ARG TARGETARCH

# Bake the extension cache into the image (honoured at build and run time).
ENV DUCKDB_EXTENSION_DIRECTORY=/opt/duckdb/extensions

COPY date.txt /date.txt

COPY duckdb-extensions.txt /duckdb-extensions.txt

# Install the duckdb binary package, then install + load every listed
# extension, then clean up.
RUN \
  R -q -e 'install.packages("duckdb"); if (!requireNamespace("duckdb", quietly = TRUE)) stop("duckdb failed to install")' && \
  R -q -e 'lines <- trimws(readLines("/duckdb-extensions.txt")); exts <- lines[nzchar(lines) & !startsWith(lines, "#")]; library(DBI); library(duckdb); con <- dbConnect(duckdb()); for (e in exts) { message("== INSTALL/LOAD ", e, " =="); dbExecute(con, paste("INSTALL", e)); dbExecute(con, paste("LOAD", e)) }; dbDisconnect(con, shutdown = TRUE); cat(sprintf("OK: duckdb %s + %d extensions\n", packageVersion("duckdb"), length(exts)))' && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true

WORKDIR /root/workspace

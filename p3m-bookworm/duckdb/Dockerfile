# arch: amd64

# duckdb package + extensions on the P3M Debian 12 (Bookworm) base image.
#
# Unlike the rig-based P3M images, the bookworm base builds R from source, and
# P3M ships no duckdb *binary* for its R build - so install.packages() falls
# back to a source build. The base image carries no compiler, so we install a
# C++ toolchain here, build duckdb, INSTALL + LOAD every extension listed in
# duckdb-extensions.txt (part of the build context), then purge the toolchain
# to keep the image slim. Installing + loading verifies each extension is
# available as a prebuilt binary for this OS/arch (the build fails otherwise)
# and pre-caches them into the image at $DUCKDB_EXTENSION_DIRECTORY.

FROM ghcr.io/cynkra/docker-images/p3m-bookworm:latest

ARG TARGETARCH

# Bake the extension cache into the image (honoured at build and run time).
ENV DUCKDB_EXTENSION_DIRECTORY=/opt/duckdb/extensions

COPY date.txt /date.txt

COPY duckdb-extensions.txt /duckdb-extensions.txt

# Install a C++ toolchain, build + install the duckdb package (from source),
# install + load every listed extension, then purge the toolchain and clean up.
# xz-utils is required because duckdb's vendored sources ship xz-compressed
# (configure runs `tar xJf duckdb.tar.xz`). MAKEFLAGS is set explicitly so
# configure skips its optional setup-makeflags.R helper (absent here) and to
# cap parallelism so the compile does not exhaust memory.
RUN \
  apt-get update && \
  apt-get install -y --no-install-recommends g++ make xz-utils && \
  MAKEFLAGS="-j2" R -q -e 'install.packages("duckdb"); if (!requireNamespace("duckdb", quietly = TRUE)) stop("duckdb failed to install")' && \
  R -q -e 'lines <- trimws(readLines("/duckdb-extensions.txt")); exts <- lines[nzchar(lines) & !startsWith(lines, "#")]; library(DBI); library(duckdb); con <- dbConnect(duckdb()); for (e in exts) { message("== INSTALL/LOAD ", e, " =="); dbExecute(con, paste("INSTALL", e)); dbExecute(con, paste("LOAD", e)) }; dbDisconnect(con, shutdown = TRUE); cat(sprintf("OK: duckdb %s + %d extensions\n", packageVersion("duckdb"), length(exts)))' && \
  apt-get purge -y --auto-remove g++ make xz-utils && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true

WORKDIR /root/workspace

# arch: amd64

FROM rhub/clang18

# Like clang18-duckdb, but instead of compiling DuckDB's vendored engine into
# the R package, LINK the package against a SHARED libduckdb of the same version
# -- using duckdb-r's own `DUCKDB_R_USE_SYSTEM_LIB` mechanism, exactly as its
# CI/CD does (`scripts/install-libduckdb.sh` in .github/workflows/custom/
# before-install). Only the thin R glue is clang-built here; the DuckDB engine is
# the official prebuilt libduckdb. This tests whether a matching shared engine
# avoids the prebuilt-extension segfault in duckdb/duckdb-r#1107.
#
# Same R 4.5 pin + clang wiring as clang18-duckdb (see CLAUDE.md §10 for the why):
# the base ships R-devel (4.6) whose cpp11 path duckdb can't compile, and plain
# `R` must be pinned to R 4.5 ahead of R-devel on PATH.
ENV R_MAKEVARS_USER="/root/.R/Makevars"
ENV PATH="/opt/R/pinned/bin:/usr/local/clang/bin:${PATH}"
ENV LD_LIBRARY_PATH="/usr/local/clang/lib:/usr/local/lib"
ENV PKG_CONFIG_PATH="/usr/local/clang/lib/pkgconfig"
ENV MAKEFLAGS="-j4"

# duckdb-r tag v1.5.4.9901 vendors DuckDB v1.5.5, whose prebuilt libduckdb is
# published, so install-libduckdb.sh downloads a real shared library (not a dev
# fallback). Pin R 4.5, install the matching libduckdb, then INSTALL the duckdb R
# package with DUCKDB_R_USE_SYSTEM_LIB=1 so it links the shared engine. Hard-fail
# if libduckdb is missing (we must exercise the shared-lib path, never fall back
# to a source build) or if duckdb does not install/load.
RUN rig add 4.5 --without-pak --without-p3m && \
    RVER="$(rig list --plain | grep -E '^4\.5\.' | sort -V | tail -n1)" && \
    echo "Pinning R $RVER" && test -n "$RVER" && \
    ln -sfn "/opt/R/$RVER" /opt/R/pinned && \
    rig default "$RVER" && \
    apt-get update && apt-get install -y --no-install-recommends unzip binutils curl ca-certificates && \
    git clone --depth 1 --branch v1.5.4.9901 https://github.com/duckdb/duckdb-r.git /tmp/duckdb-r && \
    cd /tmp/duckdb-r && \
    scripts/install-libduckdb.sh --prefix /usr/local && \
    test -f /usr/local/lib/libduckdb.so && \
    R -q -e 'options(repos = c(CRAN = "https://cloud.r-project.org")); install.packages("DBI")' && \
    DUCKDB_R_USE_SYSTEM_LIB=1 R CMD INSTALL . && \
    R -q -e 'stopifnot(getRversion() >= "4.5.0", getRversion() < "4.6.0"); if (!requireNamespace("duckdb", quietly = TRUE)) stop("duckdb failed to install")' && \
    cd / && rm -rf /tmp/duckdb-r && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/* && \
    rm -rf /var/tmp/* && \
    true

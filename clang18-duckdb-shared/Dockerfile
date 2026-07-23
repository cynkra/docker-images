# arch: amd64

FROM rhub/clang18

# Like clang18-duckdb, but instead of compiling DuckDB's vendored engine into
# the R package, LINK the package against a SHARED libduckdb of the same version
# -- using duckdb-r's own `DUCKDB_R_USE_SYSTEM_LIB` mechanism, exactly as its
# CI/CD does (`scripts/install-libduckdb.sh`). Only the thin R glue is compiled
# here; the DuckDB engine is the official prebuilt libduckdb. This tests whether
# a matching shared engine avoids the prebuilt-extension segfault in
# duckdb/duckdb-r#1107.
#
# IMPORTANT -- build the glue with **libstdc++**, not libc++. The official
# libduckdb is a libstdc++ build (its symbols carry the `[abi:cxx11]` tag, e.g.
# `duckdb::BaseScalarFunction::ToString[abi:cxx11]()`); a libc++ glue references
# the un-tagged name and fails to load with `undefined symbol:
# _ZNK6duckdb18BaseScalarFunction8ToStringEv`. So we sed the base image's clang
# Makevars from `-stdlib=libc++` to `-stdlib=libstdc++` (version-agnostic; also
# covers clang20) and install g++ for the libstdc++ headers. It is still clang;
# only the C++ runtime matches the shared engine (which the shared-lib link
# requires). Same R 4.5 pin as clang18-duckdb (base R-devel can't compile cpp11).
ENV R_MAKEVARS_USER="/root/.R/Makevars.sysduckdb"
ENV PATH="/opt/R/pinned/bin:/usr/local/clang/bin:${PATH}"
ENV LD_LIBRARY_PATH="/usr/local/lib"
ENV MAKEFLAGS="-j4"

# duckdb-r tag v1.5.4.9901 vendors DuckDB v1.5.5, whose prebuilt libduckdb is
# published, so install-libduckdb.sh downloads a real shared library (not a dev
# fallback). Pin R 4.5, install the matching libduckdb, switch the glue to
# libstdc++, then INSTALL duckdb with DUCKDB_R_USE_SYSTEM_LIB=1 so it links the
# shared engine. Hard-fail if libduckdb is missing (must exercise the shared-lib
# path, never fall back to a source build) or if duckdb does not load.
RUN rig add 4.5 --without-pak --without-p3m && \
    RVER="$(rig list --plain | grep -E '^4\.5\.' | sort -V | tail -n1)" && \
    echo "Pinning R $RVER" && test -n "$RVER" && \
    ln -sfn "/opt/R/$RVER" /opt/R/pinned && \
    rig default "$RVER" && \
    apt-get update && apt-get install -y --no-install-recommends unzip binutils curl ca-certificates g++ && \
    sed 's/-stdlib=libc++/-stdlib=libstdc++/g' /root/.R/Makevars > /root/.R/Makevars.sysduckdb && \
    git clone --depth 1 --branch v1.5.4.9901 https://github.com/duckdb/duckdb-r.git /tmp/duckdb-r && \
    cd /tmp/duckdb-r && \
    scripts/install-libduckdb.sh --prefix /usr/local && \
    test -f /usr/local/lib/libduckdb.so && \
    R -q -e 'options(repos = c(CRAN = "https://cloud.r-project.org")); install.packages("DBI")' && \
    # --install-tests keeps the package's testthat suite so the /extension
    # grand-child can run it via the sanctioned test_package().
    DUCKDB_R_USE_SYSTEM_LIB=1 R CMD INSTALL --install-tests . && \
    R -q -e 'stopifnot(getRversion() >= "4.5.0", getRversion() < "4.6.0"); library(duckdb); cat("duckdb loaded OK against shared libduckdb\n")' && \
    cd / && rm -rf /tmp/duckdb-r && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/* && \
    rm -rf /var/tmp/* && \
    true

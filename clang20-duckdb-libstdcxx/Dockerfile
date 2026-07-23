# arch: amd64

FROM rhub/clang20

# Third variant for duckdb/duckdb-r#1107. Like clang20-duckdb, this compiles
# DuckDB's *vendored* engine into the R package from source with clang -- but
# with **libstdc++** instead of the rhub base's default **libc++**. It isolates
# the C++ standard library as the single variable:
#   * clang20-duckdb          -- source compile, libc++      (reproduces the crash)
#   * clang20-duckdb-libstdcxx -- source compile, libstdc++  (this image)
#   * clang20-duckdb-shared    -- shared official libduckdb, libstdc++ glue
# i.e. does switching *only* the stdlib to libstdc++ avoid the prebuilt-extension
# segfault, without resorting to the shared engine?
#
# The stdlib switch is a SITE-level `~/.R/Makevars` (via R_MAKEVARS_USER), NOT a
# package-local setting: a hardcoded `-stdlib=libstdc++` in duckdb's own Makevars
# would be non-portable and rejected by CRAN (it breaks libc++-only platforms
# such as macOS and risks ABI mismatches with an R/toolchain built the other
# way). We sed the base image's clang Makevars from `-stdlib=libc++` to
# `-stdlib=libstdc++` into Makevars.libstdcxx (the same file the shared image
# uses) and install g++ for the libstdc++ headers. It is still clang; only the
# C++ runtime changes. Same R 4.5 pin as clang20-duckdb (base R-devel can't
# compile cpp11).
ENV R_MAKEVARS_USER="/root/.R/Makevars.libstdcxx"
ENV PATH="/opt/R/pinned/bin:/usr/local/clang/bin:${PATH}"
ENV LD_LIBRARY_PATH="/usr/local/clang/lib"
ENV PKG_CONFIG_PATH="/usr/local/clang/lib/pkgconfig"
# duckdb's configure only runs its (here-broken) MAKEFLAGS probe when MAKEFLAGS
# is unset; setting it skips the probe and compiles in parallel (minutes, not ~30).
ENV MAKEFLAGS="-j4"

# Install R 4.5, pin it as the active R, switch the clang toolchain to libstdc++,
# then compile *only* the duckdb R package from source (installing extensions is
# the job of clang20-duckdb-libstdcxx/extension). `--install-tests` keeps the
# package's testthat suite so the /extension grand-child can run it via the
# sanctioned test_package(). The getRversion() assertion fails loudly if the
# active R is not 4.5, and requireNamespace() makes a failed install a hard
# build failure.
RUN rig add 4.5 --without-pak --without-p3m && \
    RVER="$(rig list --plain | grep -E '^4\.5\.' | sort -V | tail -n1)" && \
    echo "Pinning R $RVER" && test -n "$RVER" && \
    ln -sfn "/opt/R/$RVER" /opt/R/pinned && \
    rig default "$RVER" && \
    apt-get update && apt-get install -y --no-install-recommends g++ && \
    sed 's/-stdlib=libc++/-stdlib=libstdc++/g' /root/.R/Makevars > /root/.R/Makevars.libstdcxx && \
    R --version | head -n1 && \
    R -q -e 'stopifnot(getRversion() >= "4.5.0", getRversion() < "4.6.0"); options(repos = c(CRAN = "https://cloud.r-project.org")); install.packages("duckdb", type = "source", INSTALL_opts = "--install-tests"); if (!requireNamespace("duckdb", quietly = TRUE)) stop("duckdb failed to install")' && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/* && \
    rm -rf /var/tmp/* && \
    true

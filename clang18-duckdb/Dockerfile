# arch: amd64

FROM rhub/clang18

# The rhub/clang18 base ships R-devel (4.6). duckdb's vendored cpp11 calls
# R_getRegisteredNamespace() guarded by `R_VERSION >= 4.6.0`, but this R-devel
# build does not declare that symbol, so duckdb fails to compile. Install R 4.5
# (release) via rig: cpp11 then takes its pre-4.6 code path (R_NamespaceRegistry
# / R_getVar, both present in R 4.5) and duckdb builds. See duckdb/duckdb-r#1107.
#
# `rig default` alone is NOT enough: on this base the `R` command resolves to
# R-devel regardless of the default link, so we pin R 4.5 with our own symlink
# (/opt/R/pinned) placed FIRST on PATH so plain `R` is R 4.5 in this image and
# every child. clang stays wired via /root/.R/Makevars (CC/CXX); the base only
# exported clang's bin/lib paths through the *devel* R's Renviron/Rprofile, which
# a different R version does not inherit, so re-declare them here (LD_LIBRARY_PATH
# is needed at runtime to load the clang/libc++-built duckdb).
ENV R_MAKEVARS_USER="/root/.R/Makevars"
ENV PATH="/opt/R/pinned/bin:/usr/local/clang/bin:${PATH}"
ENV LD_LIBRARY_PATH="/usr/local/clang/lib"
ENV PKG_CONFIG_PATH="/usr/local/clang/lib/pkgconfig"
# duckdb's configure only runs its (here-broken) MAKEFLAGS probe when MAKEFLAGS
# is unset; setting it skips the probe and compiles in parallel (minutes, not ~30).
ENV MAKEFLAGS="-j4"

# Install R 4.5, pin it as the active R, then compile *only* the duckdb R package
# from source (installing extensions is the job of clang18-duckdb/extension).
# The getRversion() assertion fails loudly if the active R is not 4.5, and the
# requireNamespace() check makes a failed duckdb install a hard build failure.
# `--install-tests` keeps the package's testthat suite in the installed package
# so the /extension grand-child can run it via the sanctioned test_package().
RUN rig add 4.5 --without-pak --without-p3m && \
    RVER="$(rig list --plain | grep -E '^4\.5\.' | sort -V | tail -n1)" && \
    echo "Pinning R $RVER" && test -n "$RVER" && \
    ln -sfn "/opt/R/$RVER" /opt/R/pinned && \
    rig default "$RVER" && \
    R --version | head -n1 && \
    R -q -e 'stopifnot(getRversion() >= "4.5.0", getRversion() < "4.6.0"); options(repos = c(CRAN = "https://cloud.r-project.org")); install.packages("duckdb", type = "source", INSTALL_opts = "--install-tests"); if (!requireNamespace("duckdb", quietly = TRUE)) stop("duckdb failed to install")' && \
    rm -rf /tmp/* && \
    rm -rf /var/tmp/* && \
    true

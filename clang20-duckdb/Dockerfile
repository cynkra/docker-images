# arch: amd64

FROM rhub/clang20

# The rhub/clang20 base ships R-devel (4.6). duckdb's vendored cpp11 calls
# R_getRegisteredNamespace() guarded by `R_VERSION >= 4.6.0`, but this R-devel
# build does not declare that symbol, so duckdb fails to compile. Install R 4.5
# (release) via rig and make it the default: cpp11 then takes its pre-4.6 code
# path (R_NamespaceRegistry / R_getVar, both present in R 4.5) and duckdb builds.
# See duckdb/duckdb-r#1107.
#
# clang stays wired via /root/.R/Makevars (CC/CXX). The base image exported
# clang's bin/lib paths only through the *devel* R's Renviron/Rprofile, which a
# different R version does not inherit, so re-declare them here so R 4.5 both
# compiles and loads duckdb with the clang/libc++ toolchain.
ENV R_MAKEVARS_USER="/root/.R/Makevars"
ENV PATH="/usr/local/clang/bin:${PATH}"
ENV LD_LIBRARY_PATH="/usr/local/clang/lib"
ENV PKG_CONFIG_PATH="/usr/local/clang/lib/pkgconfig"

# Install R 4.5, then compile *only* the duckdb R package from source (installing
# extensions is the job of the child clang20-duckdb/extension image).
# install.packages() only warns and exits 0 on a failed build, so the explicit
# requireNamespace() check turns a failed duckdb install into a hard failure.
RUN rig add 4.5 --without-pak --without-p3m && \
    rig default "$(rig list --plain | grep '^4\.5' | sort -V | tail -n1)" && \
    R -q -e 'options(repos = c(CRAN = "https://cloud.r-project.org")); install.packages("duckdb", type = "source"); if (!requireNamespace("duckdb", quietly = TRUE)) stop("duckdb failed to install")' && \
    rm -rf /tmp/* && \
    rm -rf /var/tmp/* && \
    true

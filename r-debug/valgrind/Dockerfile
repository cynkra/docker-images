# R-devel with valgrind level 2 instrumentation
# For memory debugging using valgrind
#
# Usage:
#   docker run --rm -ti --name rd-valgrind cynkra/r-debug-valgrind
#   RDvalgrind # to start R-devel with valgrind instrumentation

FROM ghcr.io/cynkra/docker-images/r-debug-r-devel:latest

LABEL maintainer="cynkra <team@cynkra.com>"
LABEL org.opencontainers.image.source="https://github.com/cynkra/docker-images"

# RDvalgrind: Install R-devel with valgrind level 2 instrumentation
RUN \
    /tmp/buildR.sh valgrind && \
    true

RUN \
    RDvalgrind -q -e 'install.packages("pak", repos = sprintf("https://r-lib.github.io/p/pak/stable/%s/%s/%s", .Platform$pkgType, R.Version()$os, R.Version()$arch))' && \
    true

RUN \
    RDvalgrind -q -e 'pak::pkg_install(c("devtools", "Rcpp", "cpp11", "decor", "roxygen2", "testthat", "memoise", "rmarkdown"))' && \
    true

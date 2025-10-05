# R-devel with strict barrier checking
# For ensuring R objects are protected properly
#
# Usage:
#   docker run --rm -ti --name rd-strictbarrier cynkra/r-debug-strictbarrier
#   RDstrictbarrier # to start R-devel with strict barrier checking

FROM ghcr.io/cynkra/docker-images/r-debug-r-devel:latest

LABEL maintainer="cynkra <team@cynkra.com>"
LABEL org.opencontainers.image.source="https://github.com/cynkra/docker-images"

# RDstrictbarrier: Make sure that R objects are protected properly.
RUN \
    /tmp/buildR.sh strictbarrier && \
    true

RUN \
    RDstrictbarrier -q -e 'install.packages("pak", repos = sprintf("https://r-lib.github.io/p/pak/stable/%s/%s/%s", .Platform$pkgType, R.Version()$os, R.Version()$arch))' && \
    true

RUN \
    RDstrictbarrier -q -e 'pak::pkg_install(c("devtools", "Rcpp", "cpp11", "decor", "roxygen2", "testthat", "memoise", "rmarkdown"))' && \
    true

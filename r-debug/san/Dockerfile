# R-devel with Address Sanitizer and Undefined Behavior Sanitizer (GCC)
# For detecting memory errors and undefined behavior
#
# Usage:
#   docker run --rm -ti --name rd-san cynkra/r-debug-san
#   RDsan # to start R-devel with sanitizers

FROM ghcr.io/cynkra/docker-images/r-debug-r-devel:latest

LABEL maintainer="cynkra <team@cynkra.com>"
LABEL org.opencontainers.image.source="https://github.com/cynkra/docker-images"

RUN \
    /tmp/buildR.sh san && \
    true

RUN \
    RDsan -q -e 'install.packages("pak", repos = sprintf("https://r-lib.github.io/p/pak/stable/%s/%s/%s", .Platform$pkgType, R.Version()$os, R.Version()$arch))' && \
    true

RUN \
    RDsan -q -e 'pak::pkg_install(c("devtools", "Rcpp", "cpp11", "decor", "roxygen2", "testthat", "memoise", "rmarkdown"))' && \
    true

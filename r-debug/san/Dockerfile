# R-devel with Address Sanitizer and Undefined Behavior Sanitizer (GCC)
# For detecting memory errors and undefined behavior
#
# Usage:
#   docker run --rm -ti --name rd-san cynkra/r-debug-san
#   RDsan # to start R-devel with sanitizers

FROM ghcr.io/cynkra/docker-images/r-debug-valgrind:latest

LABEL maintainer="cynkra <team@cynkra.com>"
LABEL org.opencontainers.image.source="https://github.com/cynkra/docker-images"

RUN /tmp/buildR.sh san
RUN RDsan -q -e 'install.packages("pak", repos = "https://r-lib.github.io/p/pak/dev")'
RUN RDsan -q -e 'pak::pkg_install(c("devtools", "Rcpp", "cpp11", "decor", "roxygen2", "testthat", "memoise", "rmarkdown"))'

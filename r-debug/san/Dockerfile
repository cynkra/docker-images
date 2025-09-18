# R-devel with Address Sanitizer and Undefined Behavior Sanitizer (GCC)
# For detecting memory errors and undefined behavior
#
# Usage:
#   docker run --rm -ti --name rd-san cynkra/r-debug-san
#   RDsan # to start R-devel with sanitizers

FROM cynkra/r-debug-valgrind

LABEL maintainer="cynkra <team@cynkra.com>"
LABEL org.opencontainers.image.source="https://github.com/cynkra/docker-images"

RUN /tmp/buildR.sh san && \
    rm -rf /tmp/* && \
    rm -rf /var/tmp/* && \
    true

RUN RDsan -q -e 'pak::pak("pak")' && \
    RDsan -q -e 'pak::pak(c("devtools", "Rcpp", "cpp11", "decor", "roxygen2", "testthat", "memoise", "rmarkdown"))' && \
    true

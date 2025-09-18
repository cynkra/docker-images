# R-devel with strict barrier checking
# For ensuring R objects are protected properly
#
# Usage:
#   docker run --rm -ti --name rd-strictbarrier cynkra/r-debug-strictbarrier
#   RDstrictbarrier # to start R-devel with strict barrier checking

FROM ghcr.io/cynkra/docker-images/cynkra/r-debug-csan

LABEL maintainer="cynkra <team@cynkra.com>"
LABEL org.opencontainers.image.source="https://github.com/cynkra/docker-images"

# RDstrictbarrier: Make sure that R objects are protected properly.
RUN /tmp/buildR.sh strictbarrier && \
    rm -rf /tmp/* && \
    rm -rf /var/tmp/* && \
    true

RUN RDstrictbarrier -q -e 'pak::pak("pak")' && \
    RDstrictbarrier -q -e 'pak::pak(c("devtools", "Rcpp", "cpp11", "decor", "roxygen2", "testthat", "memoise", "rmarkdown"))' && \
    true

# R-devel with thread checking
# Ensures that R's memory management functions are called only from the main R thread
#
# Usage:
#   docker run --rm -ti --name rd-threadcheck cynkra/r-debug-threadcheck
#   RDthreadcheck # to start R-devel with thread checking

FROM ghcr.io/cynkra/docker-images/cynkra/r-debug-strictbarrier

LABEL maintainer="cynkra <team@cynkra.com>"
LABEL org.opencontainers.image.source="https://github.com/cynkra/docker-images"

COPY assertthread.patch /tmp/

# RDthreadcheck: Make sure that R's memory management functions are called
# only from the main R thread.
RUN /tmp/buildR.sh threadcheck && \
    rm -rf /tmp/* && \
    rm -rf /var/tmp/* && \
    true

RUN RDthreadcheck -q -e 'pak::pak("pak")' && \
    RDthreadcheck -q -e 'pak::pak(c("devtools", "Rcpp", "cpp11", "decor", "roxygen2", "testthat", "memoise", "rmarkdown"))' && \
    true

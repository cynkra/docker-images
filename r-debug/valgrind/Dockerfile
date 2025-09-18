# R-devel with valgrind level 2 instrumentation
# For memory debugging using valgrind
#
# Usage:
#   docker run --rm -ti --name rd-valgrind cynkra/r-debug-valgrind
#   RDvalgrind # to start R-devel with valgrind instrumentation

FROM cynkra/r-debug-r-devel

LABEL maintainer="cynkra <team@cynkra.com>"
LABEL org.opencontainers.image.source="https://github.com/cynkra/docker-images"

# RDvalgrind: Install R-devel with valgrind level 2 instrumentation
RUN /tmp/buildR.sh valgrind && \
    rm -rf /tmp/* && \
    rm -rf /var/tmp/* && \
    true

RUN RDvalgrind -q -e 'pak::pak("pak")' && \
    RDvalgrind -q -e 'pak::pak(c("devtools", "Rcpp", "cpp11", "decor", "roxygen2", "testthat", "memoise", "rmarkdown"))' && \
    true

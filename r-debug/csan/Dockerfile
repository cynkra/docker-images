# R-devel with Address Sanitizer and Undefined Behavior Sanitizer (Clang)
# For detecting memory errors and undefined behavior using Clang
#
# Usage:
#   docker run --rm -ti --name rd-csan cynkra/r-debug-csan
#   RDcsan # to start R-devel with clang sanitizers

FROM ghcr.io/cynkra/docker-images/r-debug-san:latest

LABEL maintainer="cynkra <team@cynkra.com>"
LABEL org.opencontainers.image.source="https://github.com/cynkra/docker-images"

RUN /tmp/buildR.sh csan && \
    # Modify the RDcsan script to increase stack size with `ulimit -Ss 131072`;
    # otherwise we get these messages during package compilation:
    # Error: compilation failed -  C stack usage  8042720 is too close to the limit at NULL
    sed -i 's/^#!\/bin\/bash/#!\/bin\/bash\nulimit -Ss 131072/' /usr/local/bin/RDcsan && \
    # Increase stack size in .bashrc, so that it is picked up by RDscriptcsan.
    echo "\nulimit -Ss 131072" >> $HOME/.bashrc && \
    rm -rf /tmp/* && \
    rm -rf /var/tmp/* && \
    true

RUN RDcsan -q -e 'pak::pak("pak")' && \
    RDcsan -q -e 'pak::pak(c("devtools", "Rcpp", "cpp11", "decor", "roxygen2", "testthat", "memoise", "rmarkdown"))' && \
    true

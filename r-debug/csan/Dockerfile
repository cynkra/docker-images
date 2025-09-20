# R-devel with Address Sanitizer and Undefined Behavior Sanitizer (Clang)
# For detecting memory errors and undefined behavior using Clang
#
# Usage:
#   docker run --rm -ti --name rd-csan cynkra/r-debug-csan
#   RDcsan # to start R-devel with clang sanitizers

FROM ghcr.io/cynkra/docker-images/r-debug-r-devel:latest

LABEL maintainer="cynkra <team@cynkra.com>"
LABEL org.opencontainers.image.source="https://github.com/cynkra/docker-images"

RUN /tmp/buildR.sh csan

# Modify the RDcsan script to increase stack size with `ulimit -Ss 131072`;
# otherwise we get these messages during package compilation:
# Error: compilation failed -  C stack usage  8042720 is too close to the limit at NULL
RUN sed -i 's/^#!\/bin\/bash/#!\/bin\/bash\nulimit -Ss 131072/' /usr/local/bin/RDcsan
# Increase stack size in .bashrc, so that it is picked up by RDscriptcsan.
RUN echo "\nulimit -Ss 131072" >> $HOME/.bashrc

RUN RDcsan -q -e 'install.packages("pak", repos = "https://r-lib.github.io/p/pak/dev")'
RUN RDcsan -q -e 'pak::pkg_install(c("devtools", "Rcpp", "cpp11", "decor", "roxygen2", "testthat", "memoise", "rmarkdown"))'

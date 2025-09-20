# R-devel with thread checking
# Ensures that R's memory management functions are called only from the main R thread
#
# Usage:
#   docker run --rm -ti --name rd-threadcheck cynkra/r-debug-threadcheck
#   RDthreadcheck # to start R-devel with thread checking

FROM ghcr.io/cynkra/docker-images/r-debug-r-devel:latest

LABEL maintainer="cynkra <team@cynkra.com>"
LABEL org.opencontainers.image.source="https://github.com/cynkra/docker-images"

# RDthreadcheck: Make sure that R's memory management functions are called
# only from the main R thread.
RUN /tmp/buildR.sh threadcheck
RUN RDthreadcheck -q -e 'install.packages("pak", repos = "https://r-lib.github.io/p/pak/dev")'
RUN RDthreadcheck -q -e 'pak::pkg_install(c("devtools", "Rcpp", "cpp11", "decor", "roxygen2", "testthat", "memoise", "rmarkdown"))'

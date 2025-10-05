FROM ghcr.io/cynkra/docker-images/r-debug-san:latest

COPY date.txt /date.txt

# Install system dependencies and rigraph for all R debug variants, then clean up
RUN \
  apt-get update && \
  apt-get install -y libglpk-dev  libgmp-dev  libarpack2-dev && \
  RDsan -q -e 'pak::pak("igraph/rigraph", dependencies = TRUE, upgrade = TRUE)' && \
  ln -s /usr/lib/x86_64-linux-gnu/libgfortran.so.5.0.0 /usr/lib/libgfortran.so && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true

ENV ASAN_OPTIONS=detect_leaks=1:detect_odr_violation=0:color=always:detect_stack_use_after_return=1
ENV TESTTHAT_PARALLEL=false

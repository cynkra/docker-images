FROM ghcr.io/cynkra/docker-images/rig-ubuntu:latest

RUN \
  R -q -e 'pak::pak(c("r-lib/revdepcheck"), dependencies = TRUE)' && \
  true


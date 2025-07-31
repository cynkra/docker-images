FROM ghcr.io/cynkra/docker-images/ubuntu24-rig-rrel-devtools:latest

RUN R -q -e 'pak::pak("cynkra/dm")' && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true

FROM ghcr.io/cynkra/docker-images/ubuntu24-rig-rrel-dc:latest

# Install R development packages and clean up
RUN \
  R-devel -q -e 'pak::pak(c("devtools", "usethis", "languageserver"))' && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true

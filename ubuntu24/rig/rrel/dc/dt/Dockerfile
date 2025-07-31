FROM ghcr.io/cynkra/docker-images/ubuntu24-rig-rrel-dc:latest

# Install R development packages and clean up
RUN \
  rig system add-pak && \
  PKG_SYSREQS=true R -q -e 'pak::pak(c("devtools", "usethis", "languageserver"))' && \
  apt-cleanup.sh && \
  rm -rf ~/.cache && \
  true

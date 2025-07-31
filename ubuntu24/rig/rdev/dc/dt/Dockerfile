FROM ghcr.io/cynkra/docker-images/ubuntu24-rig-rdev-dc:latest

# Install R development packages and clean up
RUN \
  rig system add-pak && \
  PKG_SYSREQS=true R-devel -q -e 'pak::pak(c("devtools", "usethis", "languageserver"))' && \
  sudo apt-cleanup.sh && \
  rm -rf ~/.cache && \
  true

FROM ghcr.io/cynkra/docker-images/ubuntu24-rig-rrel-dc-dt:latest

RUN \
  PKG_SYSREQS=true R -q -e 'pak::pak("cynkra/dm")' && \
  sudo apt-cleanup.sh && \
  rm -rf ~/.cache && \
  true

FROM ghcr.io/cynkra/docker-images/ubuntu24-rig-rrel-dc-dt:latest

COPY date.txt /date.txt

RUN \
  PKG_SYSREQS=true R -q -e 'pak::pak("cynkra/dm")' && \
  sudo apt-cleanup.sh && \
  rm -rf ~/.cache && \
  true

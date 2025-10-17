FROM ghcr.io/cynkra/docker-images/ubuntu24-rig-rrel-dc-dt:latest

# The parts above are okay to be a little older
COPY date.txt /date.txt

RUN \
  PKG_SYSREQS=true R -q -e 'pak::pak("r-lib/pkgcache", dependencies = TRUE)' && \
  sudo apt-cleanup.sh && \
  rm -rf ~/.cache && \
  true

FROM ghcr.io/cynkra/docker-images/ubuntu24:latest

# Install system packages, configure locale, install rig, and set up R configuration
RUN \
  echo "ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true" | debconf-set-selections && \
  apt update && \
  apt-get install -y ttf-mscorefonts-installer && \
  true

WORKDIR /root/workspace

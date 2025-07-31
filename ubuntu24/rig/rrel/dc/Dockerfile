FROM ghcr.io/cynkra/docker-images/ubuntu24-rig-rrel:latest

# Copy dust binary from the build stage
COPY --from=ghcr.io/cynkra/docker-images/dust:latest /dust /usr/local/bin/dust

# Install common development tools and configure sudo for ubuntu user
RUN \
  chmod +x /usr/local/bin/dust && \
  apt-get update && \
  apt-get install -y git vim htop tree wget ca-certificates wget gpg gnupg gnupg2 silversearcher-ag fd-find sudo && \
  update-alternatives --set editor /usr/bin/vim.basic && \
  echo 'ubuntu ALL=(root) NOPASSWD: /usr/bin/apt-get install *, /usr/bin/apt-get update' > /etc/sudoers.d/ubuntu-apt && \
  chmod 440 /etc/sudoers.d/ubuntu-apt && \
  rm -rf /var/lib/apt/lists/* && \
  true

USER ubuntu

WORKDIR /home/ubuntu

RUN \
  mkdir .R && \
  echo 'MAKEFLAGS=-j4' > .R/Makevars && \
  touch .hushlogin && \
  true

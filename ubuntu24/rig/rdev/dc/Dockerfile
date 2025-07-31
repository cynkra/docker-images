FROM ghcr.io/cynkra/docker-images/ubuntu24-rig-rdev:latest

# Copy dust binary from the build stage
COPY --from=ghcr.io/cynkra/docker-images/dust:latest /dust /usr/local/bin/dust

# Install common development tools and configure sudo for ubuntu user
RUN \
  chmod +x /usr/local/bin/dust && \
  \
  apt-get update && \
  apt-get install -y --no-install-recommends git less vim-tiny htop tree wget ca-certificates wget gpg gnupg gnupg2 silversearcher-ag fd-find sudo && \
  update-alternatives --set editor /usr/bin/vim.tiny && \
  \
  curl -LsSf https://github.com/posit-dev/air/releases/latest/download/air-installer.sh | sh && \
  mv /root/.local/bin/air /usr/local/bin/ && \
  \
  apt-cleanup.sh && \
  \
  echo 'ubuntu ALL=(root) NOPASSWD: /bin/sh -c apt-get -y update, /bin/sh -c apt-get -y install *, /usr/bin/apt-get update, /usr/local/bin/apt-cleanup.sh' > /etc/sudoers.d/ubuntu-apt && \
  chmod 440 /etc/sudoers.d/ubuntu-apt && \
  true

USER ubuntu

WORKDIR /home/ubuntu

ENV TESTTHAT_CPUS=4

# FIXME: Bring back .Rprofile when getOption("repos") issue is understood
RUN \
  mkdir .R && \
  echo 'MAKEFLAGS=-j4' > .R/Makevars && \
  touch .hushlogin && \
  curl -s https://raw.githubusercontent.com/krlmlr/scriptlets/main/bootstrap | sh && \
  rm .Rprofile && \
  true

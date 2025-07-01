FROM rockylinux:8

RUN \
  dnf update -y && \
  true

RUN \
  dnf install -y curl sudo && \
  true

# Set locale
RUN \
  dnf install -y glibc-langpack-en && \
  true

RUN \
  curl -Ls https://github.com/r-lib/rig/releases/download/latest/rig-linux-latest.tar.gz | sudo tar xz -C /usr/local && \
  true

RUN \
  mkdir /root/.R && \
  echo 'MAKEFLAGS=-j4' > /root/.R/Makevars && \
  true

RUN \
  rig add release && \
  rig add devel && \
  true

WORKDIR /root/workspace

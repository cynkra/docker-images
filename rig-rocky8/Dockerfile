# arch: amd64

FROM rockylinux:8

RUN \
  dnf update -y && \
  dnf install -y curl sudo && \
  dnf install -y glibc-langpack-en && \
  true

RUN \
  curl -Ls https://github.com/r-lib/rig/releases/download/latest/rig-linux-latest.tar.gz | tar xz -C /usr/local && \
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

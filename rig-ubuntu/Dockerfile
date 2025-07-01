# Before changing this to 24.04, check if pak install from binary
FROM ubuntu:22.04

COPY date.txt /date.txt

RUN \
  apt-get update && \
  apt-get install -y curl sudo locales ccache && \
  true

# https://stackoverflow.com/a/28406007/946850
RUN \
  sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && \
  locale-gen && \
  true


ENV LANG=en_US.UTF-8

ENV LANGUAGE=en_US:en

ENV LC_ALL=en_US.UTF-8

RUN \
  /usr/sbin/update-ccache-symlinks && \
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

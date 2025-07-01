FROM ubuntu:24.04

COPY date.txt /date.txt

# Install system packages, configure locale, install rig, and set up R configuration
RUN \
  apt-get update && \
  apt-get install -y curl sudo locales ccache && \
  sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && \
  locale-gen && \
  /usr/sbin/update-ccache-symlinks && \
  curl -Ls https://github.com/r-lib/rig/releases/download/v0.7.1/rig-linux-0.7.1.tar.gz | sudo tar xz -C /usr/local && \
  mkdir /root/.R && \
  echo 'MAKEFLAGS=-j4' > /root/.R/Makevars && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true


ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=en_US.UTF-8

WORKDIR /root/workspace

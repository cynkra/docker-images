# arch: amd64

# Debian Trixie (13): Posit's CDN only publishes the latest R release for
# recent Debian versions. Bookworm (12) stopped at R 4.6.0 (rig add release
# then 403s on R 4.6.1), so Trixie is required for `rig add release` to work.
FROM debian:trixie

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

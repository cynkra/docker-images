FROM ubuntu:24.04

COPY date.txt /date.txt

# Install system packages, configure locale, install rig, and set up R configuration
RUN \
  apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y  --no-install-recommends locales && \
  sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && \
  locale-gen && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true

ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=en_US.UTF-8

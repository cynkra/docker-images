FROM gcc:latest

# Install basic system tools and set up locale
RUN \
  apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y --no-install-recommends locales curl sudo ccache ca-certificates && \
  sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && \
  locale-gen && \
  /usr/sbin/update-ccache-symlinks && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true

ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=en_US.UTF-8

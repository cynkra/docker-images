FROM ghcr.io/cynkra/docker-images/alma9:latest

COPY date.txt /date.txt

# Install system packages, configure locale, install rig, and set up R configuration
RUN \
  dnf update -y && \
  dnf install -y sudo ccache && \
  dnf clean all && \
  true

RUN \
  ln -s /usr/bin/ccache /usr/local/bin/gcc && \
  ln -s /usr/bin/ccache /usr/local/bin/g++ && \
  true

RUN \
  if [ "$TARGETARCH" = "arm64" ]; then \
    RIG_ARCH="rig-linux-arm64"; \
  else \
    RIG_ARCH="rig-linux"; \
  fi && \
  curl -Ls https://github.com/r-lib/rig/releases/download/v0.7.1/${RIG_ARCH}-0.7.1.tar.gz | sudo tar xz -C /usr/local && \
  true

RUN \
  mkdir /root/.R && \
  echo 'MAKEFLAGS=-j4' > /root/.R/Makevars && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true

WORKDIR /root/workspace

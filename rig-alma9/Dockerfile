FROM almalinux/9-base

COPY date.txt /date.txt

# Install system packages, configure locale, install rig, and set up R configuration
RUN \
  dnf update -y && \
  dnf install -y epel-release && \
  dnf install -y sudo glibc-langpack-en ccache && \
  dnf clean all && \
  ln -s /usr/bin/ccache /usr/local/bin/gcc && \
  ln -s /usr/bin/ccache /usr/local/bin/g++ && \
  curl -Ls https://github.com/r-lib/rig/releases/download/v0.7.1/rig-linux-0.7.1.tar.gz | tar xz -C /usr/local && \
  mkdir /root/.R && \
  echo 'MAKEFLAGS=-j4' > /root/.R/Makevars && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true


ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=en_US.UTF-8

WORKDIR /root/workspace

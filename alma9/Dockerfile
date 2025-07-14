FROM almalinux/9-base

COPY date.txt /date.txt

# Install system packages, configure locale, install rig, and set up R configuration
RUN \
  dnf update -y && \
  dnf install -y epel-release && \
  dnf install -y glibc-langpack-en && \
  dnf clean all && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true

ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=en_US.UTF-8

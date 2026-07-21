# arch: amd64
# push-on-pr: true

# Named build-stage image for p3m-bookworm.
#
# This is the "explicit build stage" of the pipeline: it compiles the current R
# release from source and installs it into a self-contained prefix
# (/opt/R/current). The p3m-bookworm image then copies that prefix in and adds
# the P3M binary-repo configuration. Keeping the compile in its own pipeline
# node (rather than a multi-stage Dockerfile) makes the build step an explicit,
# cacheable image that other images can reuse.

FROM debian:bookworm

COPY date.txt /date.txt

# Enable Debian source repositories, pull R's official build dependencies
# (authoritative and Debian-maintained), then configure + compile + install the
# current R release. The source tree and tarball are removed so that only the
# install prefix is carried forward.
RUN \
  if [ -f /etc/apt/sources.list.d/debian.sources ]; then \
    sed -i 's/^Types: deb$/Types: deb deb-src/' /etc/apt/sources.list.d/debian.sources; \
  else \
    echo 'deb-src http://deb.debian.org/debian bookworm main' >> /etc/apt/sources.list; \
  fi && \
  apt-get update && \
  apt-get install -y --no-install-recommends curl ca-certificates && \
  apt-get build-dep -y r-base && \
  curl -Ls https://cran.r-project.org/src/base/R-latest.tar.gz -o /tmp/R.tar.gz && \
  mkdir -p /tmp/Rsrc && \
  tar -xzf /tmp/R.tar.gz -C /tmp/Rsrc --strip-components=1 && \
  cd /tmp/Rsrc && \
  ./configure --prefix=/opt/R/current --enable-R-shlib --enable-memory-profiling && \
  make -j"$(nproc)" && \
  make install && \
  rm -rf /tmp/Rsrc /tmp/R.tar.gz && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/tmp/* && \
  true

WORKDIR /root/workspace

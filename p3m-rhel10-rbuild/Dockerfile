# arch: amd64, arm64

# Named build-stage image for p3m-rhel10.
#
# This is the "explicit build stage" of the pipeline: it compiles the current R
# release from source on AlmaLinux 10 and installs it into a self-contained
# prefix (/opt/R/current). The p3m-rhel10 image then copies that prefix in and
# adds the P3M binary-repo configuration. Keeping the compile in its own
# pipeline node (rather than a multi-stage Dockerfile) makes the build step an
# explicit, cacheable image that other images can reuse.

FROM almalinux:10

COPY date.txt /date.txt

# Enable the CRB repo (holds several -devel packages R needs), install the build
# toolchain + development libraries (perl is required to build R's man pages),
# then configure + compile + install the current R release. The source tree and
# tarball are removed so that only the install prefix is carried forward.
RUN \
  dnf -y install 'dnf-command(config-manager)' && \
  dnf config-manager --set-enabled crb && \
  dnf -y install \
    gcc gcc-c++ gcc-gfortran make \
    readline-devel zlib-devel bzip2-devel xz-devel pcre2-devel \
    libcurl-devel openssl-devel libicu-devel \
    cairo-devel pango-devel libpng-devel libjpeg-turbo-devel libtiff-devel \
    libX11-devel libXt-devel tcl-devel tk-devel \
    perl tar findutils which && \
  curl -Ls https://cran.r-project.org/src/base/R-latest.tar.gz -o /tmp/R.tar.gz && \
  mkdir -p /tmp/Rsrc && \
  tar -xzf /tmp/R.tar.gz -C /tmp/Rsrc --strip-components=1 && \
  cd /tmp/Rsrc && \
  ./configure --prefix=/opt/R/current --enable-R-shlib --enable-memory-profiling && \
  make -j"$(nproc)" && \
  make install && \
  rm -rf /tmp/Rsrc /tmp/R.tar.gz && \
  dnf clean all && \
  rm -rf /var/cache/dnf/* && \
  rm -rf /var/tmp/* && \
  true

WORKDIR /root/workspace

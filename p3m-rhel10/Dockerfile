# arch: amd64, arm64

# Posit Package Manager (P3M) base image - RHEL 10 (OSS: AlmaLinux 10).
# Unlike the rig-based p3m-* images, R here is COMPILED FROM SOURCE in an
# explicit preparatory build stage and then assembled into the final image.
# The default CRAN repo is set to the P3M Linux binary repository (slug:
# rhel10, x86_64 + arm64). AlmaLinux 10 is the OSS, binary-compatible stand-in
# for RHEL 10.

# ---------------------------------------------------------------------------
# Preparatory stage: build R from source.
# ---------------------------------------------------------------------------
FROM almalinux:10 AS build

# Enable the CRB repo (holds several -devel packages R needs), install the
# build toolchain and development libraries, then configure + compile + install
# the current R release into a self-contained prefix (/opt/R/current).
RUN \
  dnf -y install 'dnf-command(config-manager)' && \
  dnf config-manager --set-enabled crb && \
  dnf -y install \
    gcc gcc-c++ gcc-gfortran make \
    readline-devel zlib-devel bzip2-devel xz-devel pcre2-devel \
    libcurl-devel openssl-devel libicu-devel \
    cairo-devel pango-devel libpng-devel libjpeg-turbo-devel libtiff-devel \
    libX11-devel libXt-devel tcl-devel tk-devel \
    tar findutils which && \
  curl -Ls https://cran.r-project.org/src/base/R-latest.tar.gz -o /tmp/R.tar.gz && \
  mkdir -p /tmp/Rsrc && \
  tar -xzf /tmp/R.tar.gz -C /tmp/Rsrc --strip-components=1 && \
  cd /tmp/Rsrc && \
  ./configure --prefix=/opt/R/current --enable-R-shlib --enable-memory-profiling && \
  make -j"$(nproc)" && \
  make install && \
  true

# ---------------------------------------------------------------------------
# Final stage: assemble the image around the compiled R.
# ---------------------------------------------------------------------------
FROM almalinux:10

ARG TARGETARCH

COPY date.txt /date.txt

# Bring in the compiled R (only the install prefix, not the source tree).
COPY --from=build /opt/R/current /opt/R/current

# Install R's runtime/build libraries (the same -devel set guarantees every
# shared library R links against is present and keeps a working toolchain for
# compiling source-only packages), configure the locale, expose R/Rscript on
# PATH, and write the authoritative P3M binary repo configuration to the
# site-wide Rprofile.
RUN \
  dnf -y install 'dnf-command(config-manager)' && \
  dnf config-manager --set-enabled crb && \
  dnf -y install glibc-langpack-en \
    gcc gcc-c++ gcc-gfortran make \
    readline-devel zlib-devel bzip2-devel xz-devel pcre2-devel \
    libcurl-devel openssl-devel libicu-devel \
    cairo-devel pango-devel libpng-devel libjpeg-turbo-devel libtiff-devel \
    libX11-devel libXt-devel tcl-devel tk-devel && \
  ln -s /opt/R/current/bin/R /usr/local/bin/R && \
  ln -s /opt/R/current/bin/Rscript /usr/local/bin/Rscript && \
  printf '%s\n' \
    '## Posit Public Package Manager (P3M) - Linux binary packages (RHEL 10, slug: rhel10)' \
    'options(HTTPUserAgent = sprintf("R/%s R (%s)", getRversion(), paste(getRversion(), R.version["platform"], R.version["arch"], R.version["os"])))' \
    'options(repos = c(P3M = "https://packagemanager.posit.co/cran/__linux__/rhel10/latest"))' \
    >> "$(R RHOME)/etc/Rprofile.site" && \
  R -q -e 'stopifnot(grepl("__linux__/rhel10", getOption("repos")[["P3M"]])); cat(R.version.string, "\n")' && \
  dnf clean all && \
  rm -rf /var/cache/dnf/* && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true

ENV LANG=en_US.UTF-8

ENV LC_ALL=en_US.UTF-8

WORKDIR /root/workspace

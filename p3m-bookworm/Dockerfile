# arch: amd64

# Posit Package Manager (P3M) base image - Debian 12 (Bookworm).
# Unlike the rig-based p3m-* images, R here is COMPILED FROM SOURCE in an
# explicit preparatory build stage and then assembled into a clean final
# image. The default CRAN repo is set to the P3M Linux binary repository
# (slug: bookworm, x86_64 only).

# ---------------------------------------------------------------------------
# Preparatory stage: build R from source.
# ---------------------------------------------------------------------------
FROM debian:bookworm AS build

# Enable Debian source repositories, pull R's official build dependencies
# (authoritative, Debian-maintained), then configure + compile + install the
# current R release into a self-contained prefix (/opt/R/current).
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
  true

# ---------------------------------------------------------------------------
# Final stage: assemble the image around the compiled R.
# ---------------------------------------------------------------------------
FROM debian:bookworm

ARG TARGETARCH

COPY date.txt /date.txt

# Bring in the compiled R (only the install prefix, not the source tree).
COPY --from=build /opt/R/current /opt/R/current

# Install R's runtime/build libraries (build-dep provides every shared library
# R links against and keeps a working toolchain for compiling source-only
# packages), configure the locale, expose R/Rscript on PATH, and write the
# authoritative P3M binary repo configuration to the site-wide Rprofile.
RUN \
  if [ -f /etc/apt/sources.list.d/debian.sources ]; then \
    sed -i 's/^Types: deb$/Types: deb deb-src/' /etc/apt/sources.list.d/debian.sources; \
  else \
    echo 'deb-src http://deb.debian.org/debian bookworm main' >> /etc/apt/sources.list; \
  fi && \
  apt-get update && \
  apt-get install -y --no-install-recommends ca-certificates locales && \
  apt-get build-dep -y r-base && \
  sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && \
  locale-gen && \
  ln -s /opt/R/current/bin/R /usr/local/bin/R && \
  ln -s /opt/R/current/bin/Rscript /usr/local/bin/Rscript && \
  printf '%s\n' \
    '## Posit Public Package Manager (P3M) - Linux binary packages (slug: bookworm)' \
    'options(HTTPUserAgent = sprintf("R/%s R (%s)", getRversion(), paste(getRversion(), R.version["platform"], R.version["arch"], R.version["os"])))' \
    'options(repos = c(P3M = "https://packagemanager.posit.co/cran/__linux__/bookworm/latest"))' \
    >> "$(R RHOME)/etc/Rprofile.site" && \
  R -q -e 'stopifnot(grepl("__linux__/bookworm", getOption("repos")[["P3M"]])); cat(R.version.string, "\n")' && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true

ENV LANG=en_US.UTF-8

ENV LANGUAGE=en_US:en

ENV LC_ALL=en_US.UTF-8

WORKDIR /root/workspace

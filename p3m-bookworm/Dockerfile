# arch: amd64

# Posit Package Manager (P3M) base image - Debian 12 (Bookworm).
# R is installed via rig and the default CRAN repo is set to the P3M Linux
# binary repository (slug: bookworm). P3M serves bookworm binaries for x86_64
# only.

FROM debian:bookworm

ARG TARGETARCH

COPY date.txt /date.txt

# System dependencies + locale, rig + R (release), and the P3M binary repo
# configuration written to the site-wide Rprofile. rig's own P3M setup is
# disabled (--without-p3m) so our explicit, slug-specific config is the only
# repository configuration and always wins.
RUN \
  apt-get update && \
  apt-get install -y curl ca-certificates locales && \
  sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && \
  locale-gen && \
  RIG_ARCH="$(case "${TARGETARCH}" in amd64) echo x86_64 ;; arm64) echo aarch64 ;; *) echo unsupported ;; esac)" && \
  test "${RIG_ARCH}" != unsupported && \
  curl -Ls "https://github.com/r-lib/rig/releases/download/latest/rig-linux-${RIG_ARCH}-latest.tar.gz" | tar xz -C /usr/local && \
  rig add release --without-p3m && \
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

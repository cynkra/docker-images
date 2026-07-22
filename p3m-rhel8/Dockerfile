# arch: amd64

# Posit Package Manager (P3M) base image - RHEL 8 (OSS: AlmaLinux 8).
# R is installed via rig and the default CRAN repo is set to the P3M Linux
# binary repository. P3M serves RHEL 8 binaries under the "centos8" slug for
# x86_64 only. AlmaLinux 8 is used as the OSS, binary-compatible stand-in for
# RHEL 8.

FROM almalinux:8

ARG TARGETARCH

COPY date.txt /date.txt

# System dependencies + locale, rig + R (release), and the P3M binary repo
# configuration written to the site-wide Rprofile. rig's own P3M setup is
# disabled (--without-p3m) so our explicit, slug-specific config is the only
# repository configuration and always wins.
RUN \
  dnf -y install glibc-langpack-en && \
  RIG_ARCH="$(case "${TARGETARCH}" in amd64) echo x86_64 ;; arm64) echo aarch64 ;; *) echo unsupported ;; esac)" && \
  test "${RIG_ARCH}" != unsupported && \
  curl -Ls "https://github.com/r-lib/rig/releases/download/latest/rig-linux-${RIG_ARCH}-latest.tar.gz" | tar xz -C /usr/local && \
  rig add release --without-p3m && \
  printf '%s\n' \
    '## Posit Public Package Manager (P3M) - Linux binary packages (RHEL 8, slug: centos8)' \
    'options(HTTPUserAgent = sprintf("R/%s R (%s)", getRversion(), paste(getRversion(), R.version["platform"], R.version["arch"], R.version["os"])))' \
    'options(repos = c(P3M = "https://packagemanager.posit.co/cran/__linux__/centos8/latest"))' \
    >> "$(R RHOME)/etc/Rprofile.site" && \
  R -q -e 'stopifnot(grepl("__linux__/centos8", getOption("repos")[["P3M"]])); cat(R.version.string, "\n")' && \
  dnf clean all && \
  rm -rf /var/cache/dnf/* && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true

ENV LANG=en_US.UTF-8

ENV LC_ALL=en_US.UTF-8

WORKDIR /root/workspace

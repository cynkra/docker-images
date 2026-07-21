# arch: amd64, arm64

# Posit Package Manager (P3M) base image - RHEL 9 (OSS: AlmaLinux 9).
# R is installed via rig and the default CRAN repo is set to the P3M Linux
# binary repository (slug: rhel9). P3M serves rhel9 binaries for x86_64 and
# arm64. AlmaLinux 9 is used as the OSS, binary-compatible stand-in for RHEL 9.

FROM almalinux:9

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
    '## Posit Public Package Manager (P3M) - Linux binary packages (RHEL 9, slug: rhel9)' \
    'options(HTTPUserAgent = sprintf("R/%s R (%s)", getRversion(), paste(getRversion(), R.version["platform"], R.version["arch"], R.version["os"])))' \
    'options(repos = c(P3M = "https://packagemanager.posit.co/cran/__linux__/rhel9/latest"))' \
    >> "$(R RHOME)/etc/Rprofile.site" && \
  R -q -e 'stopifnot(grepl("__linux__/rhel9", getOption("repos")[["P3M"]])); cat(R.version.string, "\n")' && \
  dnf clean all && \
  rm -rf /var/cache/dnf/* && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true

ENV LANG=en_US.UTF-8

ENV LC_ALL=en_US.UTF-8

WORKDIR /root/workspace

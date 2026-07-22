# arch: amd64, arm64

# Posit Package Manager (P3M) base image - portable manylinux binaries.
# R is installed via rig and the default CRAN repo is set to the P3M portable
# binary repository (slug: manylinux_2_28). These binaries target glibc 2.28+
# and are therefore usable across most modern Linux distributions, on both
# x86_64 and arm64. AlmaLinux 8 (glibc 2.28) is used as the base because it
# matches the manylinux_2_28 baseline and is available for both architectures.

FROM almalinux:8

ARG TARGETARCH

COPY date.txt /date.txt

# System dependencies + locale, rig + R (release), and the P3M binary repo
# configuration written to the site-wide Rprofile. rig's own P3M setup is
# disabled (--without-p3m) so our explicit, slug-specific config is the only
# repository configuration and always wins. The manylinux_2_28 slug is portable
# and deliberately different from the base distro's native slug.
RUN \
  dnf -y install glibc-langpack-en && \
  RIG_ARCH="$(case "${TARGETARCH}" in amd64) echo x86_64 ;; arm64) echo aarch64 ;; *) echo unsupported ;; esac)" && \
  test "${RIG_ARCH}" != unsupported && \
  curl -Ls "https://github.com/r-lib/rig/releases/download/latest/rig-linux-${RIG_ARCH}-latest.tar.gz" | tar xz -C /usr/local && \
  rig add release --without-p3m && \
  printf '%s\n' \
    '## Posit Public Package Manager (P3M) - portable Linux binary packages (slug: manylinux_2_28)' \
    'options(HTTPUserAgent = sprintf("R/%s R (%s)", getRversion(), paste(getRversion(), R.version["platform"], R.version["arch"], R.version["os"])))' \
    'options(repos = c(P3M = "https://packagemanager.posit.co/cran/__linux__/manylinux_2_28/latest"))' \
    >> "$(R RHOME)/etc/Rprofile.site" && \
  R -q -e 'stopifnot(grepl("__linux__/manylinux_2_28", getOption("repos")[["P3M"]])); cat(R.version.string, "\n")' && \
  dnf clean all && \
  rm -rf /var/cache/dnf/* && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true

ENV LANG=en_US.UTF-8

ENV LC_ALL=en_US.UTF-8

WORKDIR /root/workspace

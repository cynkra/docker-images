# arch: amd64

# Posit Package Manager (P3M) base image - openSUSE Leap 15.6 (OSS stand-in
# for SLES 15 SP6/SP7). R is installed via rig and the default CRAN repo is set
# to the P3M Linux binary repository. P3M serves these binaries under the
# "opensuse156" slug for x86_64 only. openSUSE Leap is the OSS, binary-
# compatible stand-in for the proprietary SLES.

FROM opensuse/leap:15.6

ARG TARGETARCH

COPY date.txt /date.txt

# System dependencies + locale, rig + R (release), and the P3M binary repo
# configuration written to the site-wide Rprofile. rig's own P3M setup is
# disabled (--without-p3m) so our explicit, slug-specific config is the only
# repository configuration and always wins. openSUSE uses zypper and ships
# pre-generated glibc locales (no locale-gen needed).
RUN \
  zypper --non-interactive refresh && \
  zypper --non-interactive install --no-recommends curl tar gzip glibc-locale-base && \
  RIG_ARCH="$(case "${TARGETARCH}" in amd64) echo x86_64 ;; arm64) echo aarch64 ;; *) echo unsupported ;; esac)" && \
  test "${RIG_ARCH}" != unsupported && \
  curl -Ls "https://github.com/r-lib/rig/releases/download/latest/rig-linux-${RIG_ARCH}-latest.tar.gz" | tar xz -C /usr/local && \
  rig add release --without-p3m && \
  printf '%s\n' \
    '## Posit Public Package Manager (P3M) - Linux binary packages (openSUSE 15.6 / SLES 15, slug: opensuse156)' \
    'options(HTTPUserAgent = sprintf("R/%s R (%s)", getRversion(), paste(getRversion(), R.version["platform"], R.version["arch"], R.version["os"])))' \
    'options(repos = c(P3M = "https://packagemanager.posit.co/cran/__linux__/opensuse156/latest"))' \
    >> "$(R RHOME)/etc/Rprofile.site" && \
  R -q -e 'stopifnot(grepl("__linux__/opensuse156", getOption("repos")[["P3M"]])); cat(R.version.string, "\n")' && \
  zypper clean --all && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true

ENV LANG=en_US.UTF-8

ENV LC_ALL=en_US.UTF-8

WORKDIR /root/workspace

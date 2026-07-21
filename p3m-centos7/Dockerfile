# arch: amd64

# Posit Package Manager (P3M) base image - CentOS 7 (RHEL 7 family).
#
# FOR TESTING ONLY. CentOS 7 reached EOL 2024-06-30 and RHEL 7 ELS ended
# 2026-06-30; there is no maintained OSS EL7 base (see README). This image
# exists solely to exercise the P3M "centos7" binary slug (x86_64) and must not
# be used for anything that needs security updates. R is installed via rig and
# the default CRAN repo is set to the P3M centos7 binary repository.

FROM centos:7

ARG TARGETARCH

COPY date.txt /date.txt

# CentOS 7 is EOL: the mirrorlist service is gone, so repoint yum at the
# frozen vault.centos.org archive. Then install rig + R (release) and write the
# authoritative P3M binary repo configuration to the site-wide Rprofile. rig's
# own P3M setup is disabled (--without-p3m) so our explicit config always wins.
RUN \
  sed -i \
    -e 's|^mirrorlist=|#mirrorlist=|g' \
    -e 's|^#\s*baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' \
    /etc/yum.repos.d/CentOS-*.repo && \
  yum -y install curl tar && \
  RIG_ARCH="$(case "${TARGETARCH}" in amd64) echo x86_64 ;; arm64) echo aarch64 ;; *) echo unsupported ;; esac)" && \
  test "${RIG_ARCH}" != unsupported && \
  curl -Ls "https://github.com/r-lib/rig/releases/download/latest/rig-linux-${RIG_ARCH}-latest.tar.gz" | tar xz -C /usr/local && \
  rig add release --without-p3m && \
  printf '%s\n' \
    '## Posit Public Package Manager (P3M) - Linux binary packages (CentOS/RHEL 7, slug: centos7)' \
    'options(HTTPUserAgent = sprintf("R/%s R (%s)", getRversion(), paste(getRversion(), R.version["platform"], R.version["arch"], R.version["os"])))' \
    'options(repos = c(P3M = "https://packagemanager.posit.co/cran/__linux__/centos7/latest"))' \
    >> "$(R RHOME)/etc/Rprofile.site" && \
  R -q -e 'stopifnot(grepl("__linux__/centos7", getOption("repos")[["P3M"]])); cat(R.version.string, "\n")' && \
  yum clean all && \
  rm -rf /var/cache/yum && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true

ENV LANG=en_US.UTF-8

ENV LC_ALL=en_US.UTF-8

WORKDIR /root/workspace

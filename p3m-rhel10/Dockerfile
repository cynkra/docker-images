# arch: amd64, arm64

# Posit Package Manager (P3M) base image - RHEL 10 (OSS: AlmaLinux 10).
# R is compiled from source by the p3m-rhel10-rbuild build-stage image; this
# image copies that R install in, installs only the runtime libraries R links
# against, and sets the default CRAN repo to the P3M Linux binary repository
# (slug: rhel10, x86_64 + arm64). No Java is installed: base R needs it neither
# to build nor to run (Java is only for the optional rJava/Java package
# ecosystem). AlmaLinux 10 is the OSS, binary-compatible stand-in for RHEL 10.

FROM almalinux:10

ARG TARGETARCH

COPY date.txt /date.txt

# Compiled R comes from the named build-stage image, at its arch-specific tag
# (the multi-arch :latest manifest is only published on main).
COPY --from=ghcr.io/cynkra/docker-images/p3m-rhel10-rbuild:latest-${TARGETARCH} /opt/R/current /opt/R/current

# Install R's runtime shared libraries (no compilers, no JDK; CRB enabled for
# libXt/tcl/tk), configure the locale, expose R/Rscript on PATH, and write the
# authoritative P3M binary repo configuration to the site-wide Rprofile.
RUN \
  dnf -y install 'dnf-command(config-manager)' && \
  dnf config-manager --set-enabled crb && \
  dnf -y install glibc-langpack-en \
    readline pcre2 xz-libs bzip2-libs \
    openssl-libs libicu \
    libpng libjpeg-turbo libtiff \
    cairo pango libX11 libXt tcl tk \
    libgfortran libgomp libquadmath && \
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

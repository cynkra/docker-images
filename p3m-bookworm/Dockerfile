# arch: amd64

# Posit Package Manager (P3M) base image - Debian 12 (Bookworm).
# R is compiled from source by the p3m-bookworm-rbuild build-stage image; this
# image copies that R install in, installs only the runtime libraries R links
# against, and sets the default CRAN repo to the P3M Linux binary repository
# (slug: bookworm, x86_64). No Java is installed: base R needs it neither to
# build nor to run (Java is only for the optional rJava/Java package ecosystem).

# Reference the build-stage image as a named FROM stage. R is NOT compiled
# here - it is built in p3m-bookworm-rbuild; this alias only lets us COPY the
# result in. The indirection is required because BuildKit forbids variable
# expansion (the arch-specific tag) directly in `COPY --from=`; a FROM stage
# with an ARG-expanded tag is the documented workaround. The arch-specific tag
# is used because the multi-arch :latest manifest is only published on main.
ARG TARGETARCH
FROM ghcr.io/cynkra/docker-images/p3m-bookworm-rbuild:latest-${TARGETARCH} AS rbuild

FROM debian:bookworm

COPY date.txt /date.txt

# Bring in the compiled R (only the install prefix).
COPY --from=rbuild /opt/R/current /opt/R/current

# Install R's runtime shared libraries (no compilers, no JDK), configure the
# locale, expose R/Rscript on PATH, and write the authoritative P3M binary repo
# configuration to the site-wide Rprofile.
RUN \
  apt-get update && \
  apt-get install -y --no-install-recommends \
    libreadline8 libpcre2-8-0 liblzma5 libbz2-1.0 zlib1g \
    libcurl4 libssl3 libicu72 \
    libpng16-16 libjpeg62-turbo libtiff6 \
    libcairo2 libpango-1.0-0 libpangocairo-1.0-0 \
    libx11-6 libxt6 libtcl8.6 libtk8.6 \
    libgomp1 libgfortran5 libquadmath0 \
    ca-certificates locales tzdata && \
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

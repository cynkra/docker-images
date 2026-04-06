FROM ghcr.io/cynkra/docker-images/ubuntu24:latest

RUN apt-get update -y
RUN apt-get install -y --no-install-recommends \
    git \
    sudo \
    ca-certificates \
    catch2 \
    clang-format \
    r-base \
    r-cran-yaml

RUN echo 'options(repos = c(CRAN = sprintf("https://p3m.dev/cran/latest/bin/linux/noble-%s/%s", R.version["arch"], substr(getRversion(), 1, 3))))' | sudo tee -a /etc/R/Rprofile.site

RUN Rscript -e 'getOption("repos")'

RUN Rscript -e 'install.packages("pak", repos = sprintf("https://r-lib.github.io/p/pak/devel/%s/%s/%s", .Platform$pkgType, R.Version()$os, R.Version()$arch))'

RUN Rscript -e 'pak::ppm_has_binaries()'

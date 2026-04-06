FROM ghcr.io/cynkra/docker-images/ubuntu24-pak:latest

RUN echo 'options(repos = "https://p3m.dev/cran/__linux__/noble/latest", HTTPUserAgent = sprintf("R/%s R (%s)", getRversion(), paste(getRversion(), R.version$platform, R.version$arch, R.version$os)))' | sudo tee -a /etc/R/Rprofile.site

RUN Rscript -e 'pak::pak("rlang")'

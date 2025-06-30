FROM ghcr.io/cynkra/docker-images/rig-ubuntu24-rdev:latest

RUN R-devel -q -e 'pak::pak(c("devtools", "usethis", "languageserver"))'

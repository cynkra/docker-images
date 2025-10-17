# arch: amd64

FROM ghcr.io/cynkra/docker-images/rig-ubuntu:latest

# Install system dependencies and R packages, then clean up
RUN \
  apt-get update && \
  apt-get install -y cmake flex bison libglpk-dev libgmp-dev libarpack2-dev python3-venv && \
  R -q -e 'pak::pak(c("igraph", "cpp11", "devtools"), dependencies = TRUE)' && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true


# Failed with reference to R6: https://github.com/cynkra/rig-ubuntu-igraph/actions/runs/5463120907/jobs/9943407982#step:6:783
# RUN R-devel -q -e 'pak::pak("igraph", dependencies = TRUE)'

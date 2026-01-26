FROM ghcr.io/cynkra/docker-images/trixie-gcc-rig:latest

# Configure --pedantic compile flags (R already installed via apt in parent image)
RUN \
  # TODO: Use rig when Trixie is supported
  # rig add devel && \
  /bin/echo -e "CXX11FLAGS=-Wall -pedantic -g -O2\nCXX14FLAGS=-Wall -pedantic -g -O2\nCXX17FLAGS=-Wall -pedantic -g -O2\nCFLAGS=-Wall -pedantic -g -O2" >> ~/.R/Makevars && \
  true

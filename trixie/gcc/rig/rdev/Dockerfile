FROM ghcr.io/cynkra/docker-images/trixie-gcc-rig:latest

# Install R-devel and configure --pedantic compile flags
RUN \
  rig add devel && \
  /bin/echo -e "CXX11FLAGS=-Wall -pedantic -g -O2\nCXX14FLAGS=-Wall -pedantic -g -O2\nCXX17FLAGS=-Wall -pedantic -g -O2\nCFLAGS=-Wall -pedantic -g -O2" >> ~/.R/Makevars && \
  true

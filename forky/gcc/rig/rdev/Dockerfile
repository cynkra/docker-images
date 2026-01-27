FROM ghcr.io/cynkra/docker-images/forky-gcc-rig:latest

# Configure --pedantic compile flags (R already installed via apt in parent image)
RUN \
  # TODO: Use rig when Trixie is supported
  # rig add devel && \
  /bin/echo -e "CXX11FLAGS=-Wall -pedantic -g -O2 -D_FORTIFY_SOURCE=3 -mtune=native\nCXX14FLAGS=-Wall -pedantic -g -O2 -D_FORTIFY_SOURCE=3 -mtune=native\nCXX17FLAGS=-Wall -pedantic -g -O2 -D_FORTIFY_SOURCE=3 -mtune=native\nCFLAGS=-Wall -pedantic -g -O2 -D_FORTIFY_SOURCE=3 -mtune=native" >> ~/.R/Makevars && \
  true

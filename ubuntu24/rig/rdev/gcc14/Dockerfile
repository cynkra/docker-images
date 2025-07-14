FROM ghcr.io/cynkra/docker-images/ubuntu24-rig-rdev:latest

# Install GCC 14, configure alternatives, and set compiler flags
RUN \
  sed -i 's/noble/oracular/g' /etc/apt/sources.list.d/* && \
  apt-get update && \
  apt-get install -y gcc-14 g++-14 cpp-14 && \
  update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-14 100 && \
  update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-13 50 && \
  update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-14 100 && \
  update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-13 50 && \
  update-alternatives --install /usr/bin/cpp cpp-bin /usr/bin/cpp-14 100 && \
  update-alternatives --install /usr/bin/cpp cpp-bin /usr/bin/cpp-13 50 && \
  /bin/echo -e "CXX11FLAGS=-Wall -pedantic -g -O2\nCXX14FLAGS=-Wall -pedantic -g -O2\nCXX17FLAGS=-Wall -pedantic -g -O2\nCFLAGS=-Wall -pedantic -g -O2" >> ~/.R/Makevars && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  true


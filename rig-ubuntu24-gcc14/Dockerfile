FROM ghcr.io/cynkra/docker-images/rig-ubuntu24:latest

# Get most recent gcc-14 from oracular
RUN sed -i 's/noble/oracular/g' /etc/apt/sources.list.d/*

RUN apt-get update && apt-get install -y gcc-14 g++-14 cpp-14

# https://stackoverflow.com/a/9103299/946850
RUN <<EOF
update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-14 100
update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-13 50
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-14 100
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-13 50
update-alternatives --install /usr/bin/cpp cpp-bin /usr/bin/cpp-14 100
update-alternatives --install /usr/bin/cpp cpp-bin /usr/bin/cpp-13 50
EOF

FROM ghcr.io/cynkra/docker-images/rig-ubuntu24:latest

RUN apt-get install -y gcc-14 g++-14 cpp-14

# https://stackoverflow.com/a/9103299/946850
RUN <<EOF
update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-14 100
update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-13 50
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-14 100
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-13 50
update-alternatives --install /usr/bin/cpp cpp-bin /usr/bin/cpp-14 100
update-alternatives --install /usr/bin/cpp cpp-bin /usr/bin/cpp-13 50
update-alternatives --set g++ /usr/bin/g++-14
update-alternatives --set gcc /usr/bin/gcc-14
update-alternatives --set cpp-bin /usr/bin/cpp-14
EOF

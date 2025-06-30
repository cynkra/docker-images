FROM ghcr.io/cynkra/docker-images/rig-ubuntu24-rdev:latest

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

# echo without /bin/echo adds a verbatim `-e` to the output
# because commands in Dockerfiles are by default
# run in /bin/sh and not /bin/bash and
# the shell builtin echo does not support the `-e` flag
RUN /bin/echo -e "CXX11FLAGS=-Wall -pedantic -g -O2\nCXX14FLAGS=-Wall -pedantic -g -O2\nCXX17FLAGS=-Wall -pedantic -g -O2\nCFLAGS=-Wall -pedantic -g -O2" >> ~/.R/Makevars

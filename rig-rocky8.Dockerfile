FROM rockylinux:8

RUN dnf update -y

RUN dnf install -y curl sudo

# Set locale
RUN dnf install -y glibc-langpack-en

RUN curl -Ls https://github.com/r-lib/rig/releases/download/latest/rig-linux-latest.tar.gz | sudo tar xz -C /usr/local

RUN mkdir /root/.R && echo 'MAKEFLAGS=-j4' > /root/.R/Makevars

RUN rig add release && rig add devel

WORKDIR /root/workspace

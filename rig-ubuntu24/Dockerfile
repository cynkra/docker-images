FROM ubuntu:24.04

RUN apt-get update && apt-get install -y curl sudo locales ccache

# https://stackoverflow.com/a/28406007/946850
RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && \
    locale-gen

ENV LANG=en_US.UTF-8

ENV LANGUAGE=en_US:en

ENV LC_ALL=en_US.UTF-8

RUN /usr/sbin/update-ccache-symlinks

RUN curl -Ls https://github.com/r-lib/rig/releases/download/latest/rig-linux-latest.tar.gz | sudo tar xz -C /usr/local

RUN mkdir /root/.R && echo 'MAKEFLAGS=-j4' > /root/.R/Makevars

RUN rig add release && rig add devel

WORKDIR /root/workspace

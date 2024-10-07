# Deprecated, but some still use it
FROM centos:centos7

RUN yum -y update

RUN yum -y install epel-release && yum repolist

# https://unix.stackexchange.com/a/63068/19205
RUN yum groupinstall -y 'Development Tools'
# RUN yum --setopt=skip_missing_names_on_install=False install -y install gcc gcc-c++ make

RUN yum --setopt=skip_missing_names_on_install=False install -y curl sudo ccache

RUN ln -s /usr/bin/ccache /usr/local/bin/gcc && ln -s /usr/bin/ccache /usr/local/bin/g++

RUN curl -Ls https://github.com/r-lib/rig/releases/download/latest/rig-linux-latest.tar.gz | sudo tar xz -C /usr/local

RUN rig add release && rig add devel

WORKDIR /root/workspace

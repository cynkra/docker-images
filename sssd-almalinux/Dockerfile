FROM almalinux:9
# Original entrypoint: none
# Original CMD: /bin/bash

# Install required packages for AD authentication
RUN dnf update -y && \
    dnf install -y \
    sssd \
    sssd-ad \
    realmd \
    krb5-workstation \
    authselect \
    oddjob \
    oddjob-mkhomedir \
    adcli \
    samba-common-tools \
    tini \
    systemd \
    procps-ng \
    && dnf clean all

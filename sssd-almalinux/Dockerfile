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
    systemd \
    procps-ng \
    && \
    dnf clean all && \
    curl -sSL https://raw.githubusercontent.com/krallin/tini/releases/download/v0.19.0/tini -o /usr/local/bin/tini && \
    chmod +x /usr/local/bin/tini && \
    true

# Use a minimal alpine base image
FROM alpine:latest
# Original entrypoint: none
# Original CMD: /bin/sh

# Install required dependencies
# Extract only the age and age-keygen binaries from the .tar.gz
RUN \
    apk add --no-cache bash curl gnupg && \
    curl -Lo /usr/local/bin/sops https://github.com/getsops/sops/releases/download/v3.9.4/sops-v3.9.4.linux.amd64 && \
    chmod +x /usr/local/bin/sops && \
    curl -Lo /root/age.tar.gz https://github.com/FiloSottile/age/releases/download/v1.2.1/age-v1.2.1-linux-amd64.tar.gz && \
    tar -xzf /root/age.tar.gz -C /root age && \
    mv /root/age/age /root/age/age-keygen /usr/local/bin/ && \
    rm -rf /root/age.tar.gz /root/age && \
    apk del curl gnupg && \
    sops --version && \
    age --version && \
    age-keygen --version && \
    true

# Set the default shell to bash for convenience
SHELL ["/bin/bash", "-c"]

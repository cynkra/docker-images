FROM ghcr.io/tofutf/tofutf/tofutfd:v0.10.0-4-g1de178b7

# Install 1Password and AWS CLI
RUN \
  echo https://downloads.1password.com/linux/alpinelinux/stable/ >> /etc/apk/repositories && \
  wget https://downloads.1password.com/linux/keys/alpinelinux/support@1password.com-61ddfc31.rsa.pub -P /etc/apk/keys && \
  apk update && \
  apk add --no-cache aws-cli 1password-cli && \
  true


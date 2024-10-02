FROM ghcr.io/tofutf/tofutf/tofutfd:v0.10.0-4-g1de178b7

RUN echo https://downloads.1password.com/linux/alpinelinux/stable/ >> /etc/apk/repositories
RUN wget https://downloads.1password.com/linux/keys/alpinelinux/support@1password.com-61ddfc31.rsa.pub -P /etc/apk/keys
RUN apk update && apk add --no-cache aws-cli 1password-cli

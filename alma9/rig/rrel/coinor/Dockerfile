FROM ghcr.io/cynkra/docker-images/alma9-rig-rrel:latest

COPY date.txt /date.txt

RUN \
  dnf install -y git diffutils && \
  true

RUN \
  mkdir -p /coin-or && \
  cd /coin-or && \
  curl -O https://raw.githubusercontent.com/coin-or/coinbrew/master/coinbrew && \
  chmod u+x coinbrew && \
  ./coinbrew fetch SYMPHONY@master && \
  cd /coin-or && \
  ./coinbrew build SYMPHONY --prefix /opt/coin-or && \
  cd / && \
  rm -rf /coin-or && \
  true

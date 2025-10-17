# Build dust from source using cargo with musl target
FROM rust:latest AS dust-builder

COPY date.txt /date.txt

ARG TARGETARCH=arm64

# Install musl target and dependencies for static linking
RUN \
  if [ "$TARGETARCH" = "arm64" ]; then \
    RUSTARCH=aarch64; \
  else \
    RUSTARCH=x86_64; \
  fi && \
  rustup target add $RUSTARCH-unknown-linux-musl && \
  apt-get update && \
  apt-get install -y musl-tools musl-dev && \
  rm -rf /var/lib/apt/lists/*

# Build dust with musl target for static linking (no glibc dependency)
RUN \
  if [ "$TARGETARCH" = "arm64" ]; then \
    RUSTARCH=aarch64; \
  else \
    RUSTARCH=x86_64; \
  fi && \
  RUSTFLAGS='-C target-feature=+crt-static' cargo install \
    --target $RUSTARCH-unknown-linux-musl \
    du-dust

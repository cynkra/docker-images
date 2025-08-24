# Build dust from source using cargo with musl target
FROM rust:latest AS dust-builder

COPY date.txt /date.txt

# Install musl target and dependencies for static linking
RUN rustup target add x86_64-unknown-linux-musl && \
    apt-get update && \
    apt-get install -y musl-tools musl-dev && \
    rm -rf /var/lib/apt/lists/*

# Build dust with musl target for static linking (no glibc dependency)
RUN RUSTFLAGS='-C target-feature=+crt-static' cargo install \
    --target x86_64-unknown-linux-musl \
    du-dust

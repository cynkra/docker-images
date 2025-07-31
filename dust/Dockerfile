# Build dust from source using cargo
FROM rust:latest AS dust-builder
RUN cargo install du-dust

# Minimal layer to copy dust binary
FROM scratch AS dust-binary
COPY --from=dust-builder /usr/local/cargo/bin/dust /dust

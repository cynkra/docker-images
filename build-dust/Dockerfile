# Build dust from source using cargo
FROM rust:latest AS dust-builder

COPY date.txt /date.txt

RUN cargo install du-dust

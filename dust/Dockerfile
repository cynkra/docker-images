# Minimal layer to copy dust binary
FROM scratch AS dust-binary
COPY --from=ghcr.io/cynkra/docker-images/build-dust:latest /usr/local/cargo/bin/dust /dust

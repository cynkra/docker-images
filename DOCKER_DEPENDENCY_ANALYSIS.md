# Docker Image Dependency Analysis Report

## Summary

- Total Dockerfiles found: 27
- Images with local dependencies: 16
- Build stages required: 4

## Dependency Tree

```text
✓ dm ← rig-ubuntu ← ghcr.io/cynkra/docker-images/rig-ubuntu:latest
✓ r-minimal ← ubuntu:latest (external)
✓ r-postgres ← rig-ubuntu ← ghcr.io/cynkra/docker-images/rig-ubuntu:latest
✓ rchk-igraph ← kalibera/rchk:latest (external)
✓ rig-alma9 ← almalinux/9-base (external)
✓ rig-alma9-rrel ← rig-alma9 ← ghcr.io/cynkra/docker-images/rig-alma9:latest
✓ rig-alma9-rrel-coinor ← rig-alma9-rrel ← ghcr.io/cynkra/docker-images/rig-alma9-rrel:latest
✓ rig-debian ← debian:bookworm (external)
✓ rig-rocky8 ← rockylinux:8 (external)
✓ rig-ubuntu ← ubuntu:22.04 (external)
✓ rig-ubuntu-dbi ← rig-ubuntu ← ghcr.io/cynkra/docker-images/rig-ubuntu:latest
✓ rig-ubuntu-duckdb ← rig-ubuntu ← ghcr.io/cynkra/docker-images/rig-ubuntu:latest
✓ rig-ubuntu-duckdb-dev ← rig-ubuntu-duckdb ← ghcr.io/cynkra/docker-images/rig-ubuntu-duckdb:latest
✓ rig-ubuntu-duckdb4 ← rig-ubuntu ← ghcr.io/cynkra/docker-images/rig-ubuntu:latest
✓ rig-ubuntu-igraph ← rig-ubuntu ← ghcr.io/cynkra/docker-images/rig-ubuntu:latest
✓ rig-ubuntu-revdepcheck ← rig-ubuntu ← ghcr.io/cynkra/docker-images/rig-ubuntu:latest
✓ rig-ubuntu24 ← ubuntu:24.04 (external)
✓ rig-ubuntu24-gcc14 ← rig-ubuntu24-rdev ← ghcr.io/cynkra/docker-images/rig-ubuntu24-rdev:latest
✓ rig-ubuntu24-gcc14-duckdb ← rig-ubuntu24-gcc14 ← ghcr.io/cynkra/docker-images/rig-ubuntu24-gcc14:latest
✓ rig-ubuntu24-rdev ← rig-ubuntu24 ← ghcr.io/cynkra/docker-images/rig-ubuntu24:latest
✓ rig-ubuntu24-rdev-devtools ← rig-ubuntu24-rdev ← ghcr.io/cynkra/docker-images/rig-ubuntu24-rdev:latest
✓ rig-ubuntu24-rrel ← rig-ubuntu24 ← ghcr.io/cynkra/docker-images/rig-ubuntu24:latest
✓ rig-ubuntu24-rrel-devtools ← rig-ubuntu24-rrel ← ghcr.io/cynkra/docker-images/rig-ubuntu24-rrel:latest
✓ rigraph-san ← wch1/r-debug:latest (external)
✓ sops-age ← alpine:latest (external)
✓ sssd-almalinux ← almalinux:9 (external)
✓ tofutf ← ghcr.io/tofutf/tofutf/tofutfd:v0.10.0-4-g1de178b7 (external)
```

## Build Order (Topological Sort)

### Stage 1

- rig-alma9
- rig-ubuntu
- rig-ubuntu24

### Stage 2

- dm
- r-postgres
- rig-alma9-rrel
- rig-ubuntu-dbi
- rig-ubuntu-duckdb
- rig-ubuntu-duckdb4
- rig-ubuntu-igraph
- rig-ubuntu-revdepcheck
- rig-ubuntu24-rdev
- rig-ubuntu24-rrel

### Stage 3

- rig-alma9-rrel-coinor
- rig-ubuntu-duckdb-dev
- rig-ubuntu24-gcc14
- rig-ubuntu24-rdev-devtools
- rig-ubuntu24-rrel-devtools

### Stage 4

- rig-ubuntu24-gcc14-duckdb


## External Dependencies

- `almalinux/9-base` used by: rig-alma9
- `almalinux:9` used by: sssd-almalinux
- `alpine:latest` used by: sops-age
- `debian:bookworm` used by: rig-debian
- `ghcr.io/tofutf/tofutf/tofutfd:v0.10.0-4-g1de178b7` used by: tofutf
- `kalibera/rchk:latest` used by: rchk-igraph
- `rockylinux:8` used by: rig-rocky8
- `ubuntu:22.04` used by: rig-ubuntu
- `ubuntu:24.04` used by: rig-ubuntu24
- `ubuntu:latest` used by: r-minimal
- `wch1/r-debug:latest` used by: rigraph-san

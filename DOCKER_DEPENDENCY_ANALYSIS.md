# Docker Image Dependency Analysis Report

## Summary

- Total Dockerfiles found: 27
- Images with local dependencies: 16
- Build stages required: 4

## Dependency Tree

```text
✓ r-minimal ← ubuntu:latest (external)
✓ rchk-igraph ← kalibera/rchk:latest (external)
✓ rig-alma9 ← almalinux/9-base (external)
✓ rig-alma9-rrel ← rig-alma9 ← ghcr.io/cynkra/docker-images/rig-alma9:latest
✓ rig-alma9-rrel-coinor ← rig-alma9-rrel ← ghcr.io/cynkra/docker-images/rig-alma9-rrel:latest
✓ rig-debian ← debian:bookworm (external)
✓ rig-rocky8 ← rockylinux:8 (external)
✓ rig-ubuntu ← ubuntu:22.04 (external)
✓ rig-ubuntu-dbi ← rig-ubuntu ← ghcr.io/cynkra/docker-images/rig-ubuntu:latest
✓ rig-ubuntu-dm ← rig-ubuntu ← ghcr.io/cynkra/docker-images/rig-ubuntu:latest
✓ rig-ubuntu-duckdb ← rig-ubuntu ← ghcr.io/cynkra/docker-images/rig-ubuntu:latest
✓ rig-ubuntu-duckdb-dev ← rig-ubuntu-duckdb ← ghcr.io/cynkra/docker-images/rig-ubuntu-duckdb:latest
✓ rig-ubuntu-duckdb4 ← rig-ubuntu ← ghcr.io/cynkra/docker-images/rig-ubuntu:latest
✓ rig-ubuntu-igraph ← rig-ubuntu ← ghcr.io/cynkra/docker-images/rig-ubuntu:latest
✓ rig-ubuntu-r-postgres ← rig-ubuntu ← ghcr.io/cynkra/docker-images/rig-ubuntu:latest
✓ rig-ubuntu-revdepcheck ← rig-ubuntu ← ghcr.io/cynkra/docker-images/rig-ubuntu:latest
✓ rig-ubuntu24 ← ubuntu:24.04 (external)
✓ rig-ubuntu24-rdev ← rig-ubuntu24 ← ghcr.io/cynkra/docker-images/rig-ubuntu24:latest
✓ rig-ubuntu24-rdev-devtools ← rig-ubuntu24-rdev ← ghcr.io/cynkra/docker-images/rig-ubuntu24-rdev:latest
✓ rig-ubuntu24-rdev-gcc14 ← rig-ubuntu24-rdev ← ghcr.io/cynkra/docker-images/rig-ubuntu24-rdev:latest
✓ rig-ubuntu24-rdev-gcc14-duckdb ← rig-ubuntu24-rdev-gcc14 ← ghcr.io/cynkra/docker-images/rig-ubuntu24-rdev-gcc14:latest
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

- rig-alma9-rrel
- rig-ubuntu-dbi
- rig-ubuntu-dm
- rig-ubuntu-duckdb
- rig-ubuntu-duckdb4
- rig-ubuntu-igraph
- rig-ubuntu-r-postgres
- rig-ubuntu-revdepcheck
- rig-ubuntu24-rdev
- rig-ubuntu24-rrel

### Stage 3

- rig-alma9-rrel-coinor
- rig-ubuntu-duckdb-dev
- rig-ubuntu24-rdev-devtools
- rig-ubuntu24-rdev-gcc14
- rig-ubuntu24-rrel-devtools

### Stage 4

- rig-ubuntu24-rdev-gcc14-duckdb


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

## FROM Instruction Validation

This section shows the expected FROM instructions based on directory hierarchy:

- `r-minimal` (root): FROM `ubuntu:latest` ✓
- `rchk-igraph` (root): FROM `kalibera/rchk:latest` ✓
- `rig-alma9` (root): FROM `almalinux/9-base` ✓
- `rig-alma9-rrel`: FROM `ghcr.io/cynkra/docker-images/rig-alma9:latest` ✓
- `rig-alma9-rrel-coinor`: FROM `ghcr.io/cynkra/docker-images/rig-alma9-rrel:latest` ✓
- `rig-debian` (root): FROM `debian:bookworm` ✓
- `rig-rocky8` (root): FROM `rockylinux:8` ✓
- `rig-ubuntu` (root): FROM `ubuntu:22.04` ✓
- `rig-ubuntu-dbi`: FROM `ghcr.io/cynkra/docker-images/rig-ubuntu:latest` ✓
- `rig-ubuntu-dm`: FROM `ghcr.io/cynkra/docker-images/rig-ubuntu:latest` ✓
- `rig-ubuntu-duckdb`: FROM `ghcr.io/cynkra/docker-images/rig-ubuntu:latest` ✓
- `rig-ubuntu-duckdb-dev`: FROM `ghcr.io/cynkra/docker-images/rig-ubuntu-duckdb:latest` ✓
- `rig-ubuntu-duckdb4`: FROM `ghcr.io/cynkra/docker-images/rig-ubuntu:latest` ✓
- `rig-ubuntu-igraph`: FROM `ghcr.io/cynkra/docker-images/rig-ubuntu:latest` ✓
- `rig-ubuntu-r-postgres`: FROM `ghcr.io/cynkra/docker-images/rig-ubuntu:latest` ✓
- `rig-ubuntu-revdepcheck`: FROM `ghcr.io/cynkra/docker-images/rig-ubuntu:latest` ✓
- `rig-ubuntu24` (root): FROM `ubuntu:24.04` ✓
- `rig-ubuntu24-rdev`: FROM `ghcr.io/cynkra/docker-images/rig-ubuntu24:latest` ✓
- `rig-ubuntu24-rdev-devtools`: FROM `ghcr.io/cynkra/docker-images/rig-ubuntu24-rdev:latest` ✓
- `rig-ubuntu24-rdev-gcc14`: FROM `ghcr.io/cynkra/docker-images/rig-ubuntu24-rdev:latest` ✓
- `rig-ubuntu24-rdev-gcc14-duckdb`: FROM `ghcr.io/cynkra/docker-images/rig-ubuntu24-rdev-gcc14:latest` ✓
- `rig-ubuntu24-rrel`: FROM `ghcr.io/cynkra/docker-images/rig-ubuntu24:latest` ✓
- `rig-ubuntu24-rrel-devtools`: FROM `ghcr.io/cynkra/docker-images/rig-ubuntu24-rrel:latest` ✓
- `rigraph-san` (root): FROM `wch1/r-debug:latest` ✓
- `sops-age` (root): FROM `alpine:latest` ✓
- `sssd-almalinux` (root): FROM `almalinux:9` ✓
- `tofutf` (root): FROM `ghcr.io/tofutf/tofutf/tofutfd:v0.10.0-4-g1de178b7` ✓

To update FROM instructions automatically, run:
```bash
make check-from   # dry run
make update-from  # apply changes
```

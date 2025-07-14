# Docker Image Dependency Analysis Report

## Summary

- Total Dockerfiles found: 30
- Images with local dependencies: 19
- Build stages required: 5

## Dependency Tree

```text
✓ alma9 ← almalinux/9-base (external)
✓ alma9-rig ← alma9 ← ghcr.io/cynkra/docker-images/alma9:latest
✓ alma9-rig-rrel ← alma9-rig ← ghcr.io/cynkra/docker-images/alma9-rig:latest
✓ alma9-rig-rrel-coinor ← alma9-rig-rrel ← ghcr.io/cynkra/docker-images/alma9-rig-rrel:latest
✓ r-minimal ← ubuntu:latest (external)
✓ rchk-igraph ← kalibera/rchk:latest (external)
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
✓ rigraph-san ← wch1/r-debug:latest (external)
✓ sops-age ← alpine:latest (external)
✓ sssd-almalinux ← almalinux:9 (external)
✓ tofutf ← ghcr.io/tofutf/tofutf/tofutfd:v0.10.0-4-g1de178b7 (external)
✓ ubuntu24 ← ubuntu:24.04 (external)
✓ ubuntu24-msfonts ← ubuntu24 ← ghcr.io/cynkra/docker-images/ubuntu24:latest
✓ ubuntu24-rig ← ubuntu24 ← ghcr.io/cynkra/docker-images/ubuntu24:latest
✓ ubuntu24-rig-rdev ← ubuntu24-rig ← ghcr.io/cynkra/docker-images/ubuntu24-rig:latest
✓ ubuntu24-rig-rdev-devtools ← ubuntu24-rig-rdev ← ghcr.io/cynkra/docker-images/ubuntu24-rig-rdev:latest
✓ ubuntu24-rig-rdev-gcc14 ← ubuntu24-rig-rdev ← ghcr.io/cynkra/docker-images/ubuntu24-rig-rdev:latest
✓ ubuntu24-rig-rdev-gcc14-duckdb ← ubuntu24-rig-rdev-gcc14 ← ghcr.io/cynkra/docker-images/ubuntu24-rig-rdev-gcc14:latest
✓ ubuntu24-rig-rrel ← ubuntu24-rig ← ghcr.io/cynkra/docker-images/ubuntu24-rig:latest
✓ ubuntu24-rig-rrel-devtools ← ubuntu24-rig-rrel ← ghcr.io/cynkra/docker-images/ubuntu24-rig-rrel:latest
```

## Build Order (Topological Sort)

### Stage 1

- alma9
- rig-ubuntu
- ubuntu24

### Stage 2

- alma9-rig
- rig-ubuntu-dbi
- rig-ubuntu-dm
- rig-ubuntu-duckdb
- rig-ubuntu-duckdb4
- rig-ubuntu-igraph
- rig-ubuntu-r-postgres
- rig-ubuntu-revdepcheck
- ubuntu24-msfonts
- ubuntu24-rig

### Stage 3

- alma9-rig-rrel
- rig-ubuntu-duckdb-dev
- ubuntu24-rig-rdev
- ubuntu24-rig-rrel

### Stage 4

- alma9-rig-rrel-coinor
- ubuntu24-rig-rdev-devtools
- ubuntu24-rig-rdev-gcc14
- ubuntu24-rig-rrel-devtools

### Stage 5

- ubuntu24-rig-rdev-gcc14-duckdb


## External Dependencies

- `almalinux/9-base` used by: alma9
- `almalinux:9` used by: sssd-almalinux
- `alpine:latest` used by: sops-age
- `debian:bookworm` used by: rig-debian
- `ghcr.io/tofutf/tofutf/tofutfd:v0.10.0-4-g1de178b7` used by: tofutf
- `kalibera/rchk:latest` used by: rchk-igraph
- `rockylinux:8` used by: rig-rocky8
- `ubuntu:22.04` used by: rig-ubuntu
- `ubuntu:24.04` used by: ubuntu24
- `ubuntu:latest` used by: r-minimal
- `wch1/r-debug:latest` used by: rigraph-san

## FROM Instruction Validation

This section shows the expected FROM instructions based on directory hierarchy:

- `alma9` (root): FROM `almalinux/9-base` ✓
- `alma9-rig`: FROM `ghcr.io/cynkra/docker-images/alma9:latest` ✓
- `alma9-rig-rrel`: FROM `ghcr.io/cynkra/docker-images/alma9-rig:latest` ✓
- `alma9-rig-rrel-coinor`: FROM `ghcr.io/cynkra/docker-images/alma9-rig-rrel:latest` ✓
- `r-minimal` (root): FROM `ubuntu:latest` ✓
- `rchk-igraph` (root): FROM `kalibera/rchk:latest` ✓
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
- `rigraph-san` (root): FROM `wch1/r-debug:latest` ✓
- `sops-age` (root): FROM `alpine:latest` ✓
- `sssd-almalinux` (root): FROM `almalinux:9` ✓
- `tofutf` (root): FROM `ghcr.io/tofutf/tofutf/tofutfd:v0.10.0-4-g1de178b7` ✓
- `ubuntu24` (root): FROM `ubuntu:24.04` ✓
- `ubuntu24-msfonts`: FROM `ghcr.io/cynkra/docker-images/ubuntu24:latest` ✓
- `ubuntu24-rig`: FROM `ghcr.io/cynkra/docker-images/ubuntu24:latest` ✓
- `ubuntu24-rig-rdev`: FROM `ghcr.io/cynkra/docker-images/ubuntu24-rig:latest` ✓
- `ubuntu24-rig-rdev-devtools`: FROM `ghcr.io/cynkra/docker-images/ubuntu24-rig-rdev:latest` ✓
- `ubuntu24-rig-rdev-gcc14`: FROM `ghcr.io/cynkra/docker-images/ubuntu24-rig-rdev:latest` ✓
- `ubuntu24-rig-rdev-gcc14-duckdb`: FROM `ghcr.io/cynkra/docker-images/ubuntu24-rig-rdev-gcc14:latest` ✓
- `ubuntu24-rig-rrel`: FROM `ghcr.io/cynkra/docker-images/ubuntu24-rig:latest` ✓
- `ubuntu24-rig-rrel-devtools`: FROM `ghcr.io/cynkra/docker-images/ubuntu24-rig-rrel:latest` ✓

To update FROM instructions automatically, run:
```bash
make check-from   # dry run
make update-from  # apply changes
```

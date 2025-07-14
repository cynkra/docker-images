# docker-images

This repository contains customized Docker images, built on a regular schedule using cache to avoid unnecessary rebuilds.

## Add a new image

1. Create a new directory.
2. Add all the necessary files to that new directory (`Dockerfile` + any dependencies).
3. Add the name of the directory to the `stages.yml` file. If the docker image depends on an existing one, add it to the next stage otherwise add it to stage-1.
4. Add the image to the list of images in this file.

## Remove an existing image

1. Make sure that no other docker files depends on it.
2. Remove the directory.
3. Remove the directory name from the `stages.yml` file.
4. Remove the image from this file.

## Cache Invalidation Strategy

Several Docker images in this repository use a `date.txt` file for cache invalidation to ensure fresh package installations. The `COPY date.txt /date.txt` instruction forces Docker to rebuild the entire pipeline from that point when the date.txt file changes.

**Important**: Do not remove `COPY date.txt /date.txt` lines from Dockerfiles as they are essential for proper cache invalidation.

## Dockerfile Best Practices

This repository follows specific patterns for optimal Docker image construction:

1. **Concatenated Commands**: Related RUN commands are combined using `&&` to minimize Docker layers and reduce image size
2. **Cleanup Strategy**: All Dockerfiles include cleanup commands (`rm -rf /var/lib/apt/lists/* && rm -rf /tmp/* && rm -rf /var/tmp/*`) to remove temporary files and package caches
3. **Logical Grouping**: Operations are grouped logically (system packages, R packages, configuration) within single RUN instructions
4. **Package Management**: R packages are installed using `pak::pak()` for better performance and dependency resolution

## Automated FROM Instruction Management

This repository includes automated tools for managing FROM instructions in Dockerfiles according to directory hierarchy:

- **Root-level images** (e.g., `rig-ubuntu`, `rig-debian`) use external base images and their FROM instructions should not be modified
- **Nested images** (e.g., `rig-ubuntu/duckdb`, `rig-ubuntu/duckdb/dev`) should inherit from their parent directory image

### Available Commands

```bash
# Check what FROM instructions would be updated (dry run)
make check-from

# Update FROM instructions according to hierarchy
make update-from

# Generate dependency analysis with FROM validation
make analysis
```

The system automatically:

- Validates that nested images inherit from the correct parent image
- Updates FROM instructions to follow the directory hierarchy convention
- Provides clear reporting of any inconsistencies

## Images

### [dm](dm)

Based on rig-ubuntu, configured for database management and modeling tasks. Includes Microsoft ODBC Driver 18 for SQL Server and system tools (gnupg, lsb-release, time) for enterprise database connectivity. Installs R packages from DESCRIPTION file.

### [r-4-duckdb](r-4-duckdb)

**Dependency**: rig-ubuntu
Development environment for working with DuckDB using R 4.x. Includes necessary build tools and optimized for legacy R compatibility.

### [r-minimal](r-minimal)

**Dependency**: ubuntu:latest
Minimal Ubuntu-based image with basic setup. Serves as a lightweight base for specialized use cases.

### [r-postgres](r-postgres)

**Dependency**: rig-ubuntu
PostgreSQL-enabled R environment with postgresql-client and essential system tools. Configured for database development workflows. Installs packages specified in DESCRIPTION file.

### [rchk-igraph](rchk-igraph)

**Dependency**: kalibera/rchk:latest
R check environment with igraph dependencies, based on kalibera/rchk. Includes libglpk-dev for graph optimization algorithms. Used for rigorous package checking and validation.

### [rig-alma9](rig-alma9)

**Dependency**: almalinux/9-base
AlmaLinux 9 with rig installed. Includes essential system packages (curl, sudo, locales, ccache), proper locale configuration (en_US.UTF-8), and optimized R build configuration (MAKEFLAGS=-j4). Foundation image without R installed.

### [rig-alma9-rrel](rig-alma9-rrel)

**Dependency**: rig-alma9
AlmaLinux 9 with R release installed via rig. Ready-to-use R environment for production workflows.

### [rig-debian](rig-debian)

**Dependency**: debian
Debian-based rig environment for compatibility testing and specialized Debian workflows.

### [rig-rocky8](rig-rocky8)

**Dependency**: rockylinux:8
Rocky Linux 8-based rig environment for enterprise RHEL-compatible development and testing.

### [rig-ubuntu](rig-ubuntu)

**Dependency**: ubuntu
Ubuntu-based rig environment with base R installation capabilities. Serves as foundation for many other specialized images.

### [rig-ubuntu-dbi](rig-ubuntu-dbi)

**Dependency**: rig-ubuntu
Database interface development environment with comprehensive R database packages (DBI, RMariaDB, RPostgres, RSQLite, dm, duckdb, odbc, adbi) installed for both R release and R-devel. Includes development tools and system dependencies for database connectivity.

### [rig-ubuntu-duckdb](rig-ubuntu-duckdb)

**Dependency**: rig-ubuntu
DuckDB development environment with build tools (python3, ninja-build, cmake) and R packages (duckplyr, cpp11, decor, devtools). Configured with DUCKDB_R_DEBUG=1 for development debugging.

### [rig-ubuntu-duckdb4](rig-ubuntu-duckdb4)

**Dependency**: rig-ubuntu
Like rig-ubuntu-duckdb, but with R 4.1.3 for compatibility testing. Includes duckdb, cpp11, decor, and devtools packages.

### [rig-ubuntu-duckdb-dev](rig-ubuntu-duckdb-dev)

**Dependency**: rig-ubuntu-duckdb
Development environment with latest development versions of duckdb-r and duckplyr cloned and installed from GitHub repositories. Uses date.txt for cache invalidation.

### [rig-ubuntu-igraph](rig-ubuntu-igraph)

**Dependency**: rig-ubuntu
Graph analysis environment with igraph and its system dependencies (cmake, flex, bison, libglpk-dev, libgmp-dev, libarpack2-dev, python3-venv). Includes igraph, cpp11, and devtools R packages.

### [rig-ubuntu-revdepcheck](rig-ubuntu-revdepcheck)

**Dependency**: rig-ubuntu
Reverse dependency checking environment with r-lib/revdepcheck package for comprehensive package testing workflows.

### [rig-ubuntu24](rig-ubuntu24)

**Dependency**: ubuntu:24.04
Ubuntu 24.04 base with rig installed. Includes essential system packages (curl, sudo, locales, ccache), proper locale configuration (en_US.UTF-8), and optimized R build configuration (MAKEFLAGS=-j4). Foundation image without R installed.

### [rig-ubuntu24-rrel](rig-ubuntu24-rrel)

**Dependency**: rig-ubuntu24
Ubuntu 24.04 with R release installed via rig. Ready-to-use R environment for production workflows.

### [rig-ubuntu24-rrel-devtools](rig-ubuntu24-rrel-devtools)

**Dependency**: rig-ubuntu24-rrel
Development environment based on R release with essential development tools (git, vim, nano, htop, tree, wget, ca-certificates) and R development packages (devtools, usethis, languageserver). Optimized for R package development workflows.

### [rig-ubuntu24-rdev](rig-ubuntu24-rdev)

**Dependency**: rig-ubuntu24
Ubuntu 24.04 with R devel installed via rig. Used for testing packages against cutting-edge R development versions.

### [rig-ubuntu24-rdev-devtools](rig-ubuntu24-rdev-devtools)

**Dependency**: rig-ubuntu24-rdev
Development environment based on R devel with essential development tools (git, vim, nano, htop, tree, wget, ca-certificates) and R development packages (devtools, usethis, languageserver). Optimized for bleeding-edge R package development.

### [rig-ubuntu24-gcc14](rig-ubuntu24-gcc14)

**Dependency**: rig-ubuntu24-rdev
Specialized environment with GCC 14 compiler to replicate CRAN compiler warnings and testing conditions. Configured with update-alternatives for proper compiler selection and enhanced warning flags for thorough code validation.

### [rig-ubuntu24-gcc14-duckdb](rig-ubuntu24-gcc14-duckdb)

**Dependency**: rig-ubuntu24-gcc14
GCC 14 environment optimized for DuckDB development, including build dependencies (python3, ninja-build, cmake) and essential R packages (DBI, cpp11). Configured with DUCKDB_R_DEBUG=1.

### [rigraph-san](rigraph-san)

**Dependency**: wch1/r-debug:latest
Specialized testing environment for rigraph package using multiple R debug variants (RD, RDvalgrind, RDsan, RDcsan, RDthreadcheck). Includes sanitizer configurations (ASAN_OPTIONS) and required system libraries for comprehensive memory and thread safety testing.

#### [sops-age](sops-age)

**Dependency**: alpine:latest
Lightweight Alpine-based image with `sops` and `age` for secret management and encryption workflows. Includes essential tools (git, curl, bash, jq) for CI/CD pipelines.

### [tofutf](tofutf)

**Dependency**: ghcr.io/tofutf/tofutf/tofutfd:v0.10.0-4-g1de178b7
Terraform/OpenTofu environment with additional tooling including 1Password CLI and AWS CLI for infrastructure automation and secret management.

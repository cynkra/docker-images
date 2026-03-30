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

### [alma9](alma9)

**Dependency**: almalinux/9-base
AlmaLinux 9 base with essential system packages and locale configuration (en_US.UTF-8). Foundation image for AlmaLinux-based R environments.

### [alma9/rig](alma9/rig)

**Dependency**: alma9
AlmaLinux 9 with rig installed. Includes essential development packages (curl, sudo, ccache) and optimized R build configuration (MAKEFLAGS=-j4).

### [alma9/rig/rrel](alma9/rig/rrel)

**Dependency**: alma9/rig
AlmaLinux 9 with R release installed via rig. Ready-to-use R environment for production workflows.

### [alma9/rig/rrel/coinor](alma9/rig/rrel/coinor)

**Dependency**: alma9/rig/rrel
AlmaLinux 9 R environment with COIN-OR SYMPHONY optimization library built and installed to /opt/coin-or. Used for mathematical optimization and operations research.

### [clang18-duckdb](clang18-duckdb)

**Dependency**: rhub/clang18
Specialized environment with Clang 18 compiler for testing DuckDB with alternative compiler toolchain. Used for compiler compatibility testing.

### [forky](forky)

**Dependency**: debian:forky
Debian Forky (testing) base with essential system packages and locale configuration. Foundation for testing with cutting-edge Debian.

### [forky/gcc](forky/gcc)

**Dependency**: forky
Debian Forky with GCC compiler and build-essential tools. Base for building R packages with latest GCC.

### [forky/gcc/rig](forky/gcc/rig)

**Dependency**: forky/gcc
Debian Forky with R installed via apt (rig doesn't support Forky yet). Includes ccache and build configuration.

### [forky/gcc/rig/rdev](forky/gcc/rig/rdev)

**Dependency**: forky/gcc/rig
Debian Forky R development environment with pedantic compiler flags (-Wall -pedantic) for strict code quality checking.

### [forky/gcc/rig/rdev/duckdb](forky/gcc/rig/rdev/duckdb)

**Dependency**: forky/gcc/rig/rdev
Forky development environment with DuckDB built from source. Includes build tools (python3, ninja-build, cmake) and DUCKDB_R_DEBUG=1.

### [otf](otf)

**Dependency**: leg100/otfd:0.4.9
OpenTofu/Terraform environment with AWS CLI added. Used for infrastructure automation with cloud provider integration.

### [r-minimal](r-minimal)

**Dependency**: ubuntu:latest
Minimal Ubuntu-based image with basic setup. Serves as a lightweight base for specialized use cases.

### [rchk-igraph](rchk-igraph)

**Dependency**: kalibera/rchk:latest
R check environment with igraph dependencies, based on kalibera/rchk. Includes libglpk-dev for graph optimization algorithms. Used for rigorous package checking and validation.

### [rig-debian](rig-debian)

**Dependency**: debian:bookworm
Debian Bookworm-based rig environment for compatibility testing and specialized Debian workflows.

### [rig-rocky8](rig-rocky8)

**Dependency**: rockylinux:8
Rocky Linux 8-based rig environment for enterprise RHEL-compatible development and testing.

### [rig-ubuntu](rig-ubuntu)

**Dependency**: ubuntu:latest
Ubuntu-based rig environment with base R installation capabilities. Serves as foundation for many other specialized images.

### [rig-ubuntu/dbi](rig-ubuntu/dbi)

**Dependency**: rig-ubuntu
Database interface development environment with comprehensive R database packages (DBI, RMariaDB, RPostgres, RSQLite, dm, duckdb, odbc, adbi) installed for both R release and R-devel. Includes development tools and system dependencies for database connectivity.

### [rig-ubuntu/dm](rig-ubuntu/dm)

**Dependency**: rig-ubuntu
Based on rig-ubuntu, configured for database management and modeling tasks. Includes Microsoft ODBC Driver 18 for SQL Server and system tools for enterprise database connectivity. Installs R packages from DESCRIPTION file.

### [rig-ubuntu/duckdb](rig-ubuntu/duckdb)

**Dependency**: rig-ubuntu
DuckDB development environment with build tools (python3, ninja-build, cmake) and R packages (duckplyr, cpp11, decor, devtools). Configured with DUCKDB_R_DEBUG=1 for development debugging.

### [rig-ubuntu/duckdb4](rig-ubuntu/duckdb4)

**Dependency**: rig-ubuntu
Like rig-ubuntu/duckdb, but with R 4.1.3 for compatibility testing. Includes duckdb, cpp11, decor, and devtools packages.

### [rig-ubuntu/duckdb/dev](rig-ubuntu/duckdb/dev)

**Dependency**: rig-ubuntu/duckdb
Development environment with latest development versions of duckdb-r and duckplyr cloned and installed from GitHub repositories. Uses date.txt for cache invalidation.

### [rig-ubuntu/igraph](rig-ubuntu/igraph)

**Dependency**: rig-ubuntu
Graph analysis environment with igraph and its system dependencies (cmake, flex, bison, libglpk-dev, libgmp-dev, libarpack2-dev, python3-venv). Includes igraph, cpp11, and devtools R packages.

### [rig-ubuntu/r-postgres](rig-ubuntu/r-postgres)

**Dependency**: rig-ubuntu
PostgreSQL-enabled R environment with postgresql-client and essential system tools. Configured for database development workflows. Installs packages specified in DESCRIPTION file.

### [rig-ubuntu/revdepcheck](rig-ubuntu/revdepcheck)

**Dependency**: rig-ubuntu
Reverse dependency checking environment with r-lib/revdepcheck package for comprehensive package testing workflows.

### [ubuntu24](ubuntu24)

**Dependency**: ubuntu:24.04
Ubuntu 24.04 base with locale configuration (en_US.UTF-8). Foundation image for Ubuntu 24.04-based R environments.

### [ubuntu24/msfonts](ubuntu24/msfonts)

**Dependency**: ubuntu24
Ubuntu 24.04 with Microsoft TrueType core fonts installed. Used for consistent font rendering in reports and graphics.

### [ubuntu24/rig](ubuntu24/rig)

**Dependency**: ubuntu24
Ubuntu 24.04 with rig installed. Includes essential system packages (curl, sudo, ccache) and optimized R build configuration (MAKEFLAGS=-j4). Foundation image without R installed.

### [ubuntu24/rig/rrel](ubuntu24/rig/rrel)

**Dependency**: ubuntu24/rig
Ubuntu 24.04 with R release installed via rig. Ready-to-use R environment for production workflows.

### [ubuntu24/rig/rrel/dc](ubuntu24/rig/rrel/dc)

**Dependency**: ubuntu24/rig/rrel
Development container with dust, air, and development tools (git, vim, htop, silversearcher-ag, fd-find). Configured with ubuntu user and sudo access for apt operations.

### [ubuntu24/rig/rrel/dc/dt](ubuntu24/rig/rrel/dc/dt)

**Dependency**: ubuntu24/rig/rrel/dc
Development environment with R development packages (devtools, usethis, languageserver) installed. Optimized for R package development workflows.

### [ubuntu24/rig/rrel/dc/dt/dm](ubuntu24/rig/rrel/dc/dt/dm)

**Dependency**: ubuntu24/rig/rrel/dc/dt
Database management environment with Microsoft ODBC Driver 18 for SQL Server, mssql-tools18, and unixodbc-dev. Configured for enterprise database connectivity.

### [ubuntu24/rig/rrel/dc/dt/pkgcache](ubuntu24/rig/rrel/dc/dt/pkgcache)

**Dependency**: ubuntu24/rig/rrel/dc/dt
Development environment with r-lib/pkgcache installed for fast package caching and dependency resolution.

### [ubuntu24/rig/rdev](ubuntu24/rig/rdev)

**Dependency**: ubuntu24/rig
Ubuntu 24.04 with R devel installed via rig. Used for testing packages against cutting-edge R development versions.

### [ubuntu24/rig/rdev/dc](ubuntu24/rig/rdev/dc)

**Dependency**: ubuntu24/rig/rdev
Development container for R-devel with dust, air, and development tools. Configured with ubuntu user and sudo access.

### [ubuntu24/rig/rdev/dc/dt](ubuntu24/rig/rdev/dc/dt)

**Dependency**: ubuntu24/rig/rdev/dc
R-devel development environment with development packages (devtools, usethis, languageserver) for bleeding-edge R package development.

### [ubuntu24/rig/rdev/gcc14](ubuntu24/rig/rdev/gcc14)

**Dependency**: ubuntu24/rig/rdev
Specialized environment with GCC 14 compiler to replicate CRAN compiler warnings and testing conditions. Configured with update-alternatives for proper compiler selection and enhanced warning flags.

### [ubuntu24/rig/rdev/gcc14/duckdb](ubuntu24/rig/rdev/gcc14/duckdb)

**Dependency**: ubuntu24/rig/rdev/gcc14
GCC 14 environment optimized for DuckDB development, including build dependencies (python3, ninja-build, cmake) and essential R packages (DBI, cpp11). Configured with DUCKDB_R_DEBUG=1.

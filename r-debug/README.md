# R Debug Docker Images

This directory contains Docker images for debugging R memory problems and other low-level issues. These images provide various instrumented builds of R-devel specifically designed for detecting memory errors, undefined behavior, and thread safety issues.

## Overview

The images build on each other in a hierarchical manner:

1. `r-devel` - Base R-devel without optimizations (-O0) for debugging
2. `valgrind` - R-devel with valgrind level 2 instrumentation
3. `san` - R-devel with GCC Address Sanitizer and Undefined Behavior Sanitizer
4. `csan` - R-devel with Clang Address Sanitizer and Undefined Behavior Sanitizer
5. `strictbarrier` - R-devel with strict barrier checking
6. `threadcheck` - R-devel with thread checking to ensure memory management functions are called from the main thread

## Available R Builds

Each image provides different builds of R-devel:

- **RD**: Standard R-devel compiled without optimizations
- **RDvalgrind**: R-devel with valgrind instrumentation (start with `RDvalgrind -d valgrind`)
- **RDsan**: R-devel with GCC sanitizers
- **RDcsan**: R-devel with Clang sanitizers
- **RDstrictbarrier**: R-devel with strict barrier checking (use with `gctorture(TRUE)`)
- **RDthreadcheck**: R-devel with thread checking

## Usage

### Quick Start

For general memory debugging with good performance, start with the SAN build:

```bash
docker run --rm -ti --security-opt seccomp=unconfined ghcr.io/cynkra/docker-images/r-debug-san:latest
RDsan
```

### Specific Debugging Tools

**Valgrind (slowest but most thorough):**
```bash
docker run --rm -ti --security-opt seccomp=unconfined ghcr.io/cynkra/docker-images/r-debug-valgrind:latest
RDvalgrind -d valgrind
```

**Clang Sanitizers (good performance):**
```bash
docker run --rm -ti --security-opt seccomp=unconfined ghcr.io/cynkra/docker-images/r-debug-csan:latest
RDcsan
```

**Thread Safety Checking:**
```bash
docker run --rm -ti --security-opt seccomp=unconfined ghcr.io/cynkra/docker-images/r-debug-threadcheck:latest
RDthreadcheck
```

**Strict Barrier Checking:**
```bash
docker run --rm -ti --security-opt seccomp=unconfined ghcr.io/cynkra/docker-images/r-debug-strictbarrier:latest
RDstrictbarrier
# In R: gctorture(TRUE) or gctorture2(1, inhibit_release=TRUE)
```

## Package Installation

Each R build has its own package library to avoid conflicts. Common packages (devtools, Rcpp, cpp11, etc.) are pre-installed. To install additional packages:

```r
# Inside any R session
pak::pak("your_package")
```

## Environment Variables

The images set several environment variables for optimal debugging:

- `ASAN_OPTIONS='detect_leaks=0:detect_odr_violation=0'`
- `UBSAN_OPTIONS='print_stacktrace=1'`
- `RJAVA_JVM_STACK_WORKAROUND=0`
- `RGL_USE_NULL=true`
- `R_DONT_USE_TK=true`

## Security Context

Some debugging features require running with `--security-opt seccomp=unconfined` to allow memory debugging tools to function properly.

## Building

To build all images in order:

```bash
# Build base image
cd r-devel && make build

# Build subsequent images
cd ../valgrind && make build
cd ../san && make build
cd ../csan && make build
cd ../strictbarrier && make build
cd ../threadcheck && make build
```

## References

- [Writing R Extensions - Checking memory access](https://cran.r-project.org/doc/manuals/r-release/R-exts.html#Checking-memory-access)
- [R memory debugging guide](http://www.stats.ox.ac.uk/pub/bdr/memtests/README.txt)
- Original Docker images by Winston Chang: [wch1/r-debug](https://hub.docker.com/r/wch1/r-debug/)

## Package Libraries

Each R build maintains separate package libraries to prevent conflicts:

- Base packages are shared across all builds (installed to `/usr/local/RD/lib/R/library/`)
- User packages are installed to each build's `site-library/`
- Pre-installed packages: pak, devtools, Rcpp, cpp11, decor, roxygen2, testthat, memoise, rmarkdown

# Architecture Support in Docker Images

This document explains how architecture support works in this repository.

## Multi-Platform Images

All Docker images in this repository are built as **multi-platform images** using Docker manifests. This means:

1. **Individual platform images** are built for each supported architecture (e.g., `latest-amd64`, `latest-arm64`)
2. A **manifest** is created that combines all architectures under a single tag (`latest`)
3. When you pull `image:latest`, Docker automatically selects the correct architecture for your platform

## Default Architecture Support

By default, all images are built for:

- `amd64` (x86_64)
- `arm64` (aarch64)

## Restricting Architecture Support

Some images may need to be restricted to specific architectures due to:

- Dependencies that are only available on certain platforms
- Platform-specific compilation requirements
- External base images that don't support all architectures

### How to Restrict Architectures

Add an `# arch:` comment within the first 10 lines of your Dockerfile:

```dockerfile
# arch: amd64
```

For multiple architectures:

```dockerfile
# arch: amd64, arm64
```

### What Happens When You Restrict

When the `generate_stages.py` script detects an architecture restriction:

1. **GitHub Actions workflow** (`stages.yml`) is generated to build only the specified architectures
2. **Makefiles** are generated with only the relevant architecture-specific targets
3. The **manifest** will only include the available architectures

### Example: rig-debian

The `rig-debian` image is restricted to `amd64` only:

```dockerfile
# arch: amd64

# Before changing this to 24.04, check if pak install from binary
FROM debian:bookworm
```

This means:

- Only `latest-amd64` is built
- The manifest for `latest` only includes amd64
- Attempting to pull on arm64 will fail with a clear error message

## Using Multi-Platform Images

### Correct Usage ✅

Always use the `latest` tag without architecture suffix:

```bash
# Docker automatically pulls the correct architecture
docker pull ghcr.io/cynkra/docker-images/ubuntu24-rig:latest
docker run -it ghcr.io/cynkra/docker-images/ubuntu24-rig:latest bash

# You can explicitly specify platform with the latest tag
docker run --platform linux/amd64 -it ghcr.io/cynkra/docker-images/ubuntu24-rig:latest bash
```

In Dockerfiles:

```dockerfile
FROM ghcr.io/cynkra/docker-images/ubuntu24-rig:latest
```

### Incorrect Usage ❌

Do **not** use architecture-specific tags in production:

```bash
# Wrong - bypasses manifest, locks to specific arch
docker run -it ghcr.io/cynkra/docker-images/ubuntu24-rig:latest-amd64 bash
```

```dockerfile
# Wrong - breaks multi-platform builds
FROM ghcr.io/cynkra/docker-images/ubuntu24-rig:latest-amd64
```

### When to Use Architecture-Specific Tags

Architecture-specific tags (`latest-amd64`, `latest-arm64`) are **only** for:

1. **Debugging**: Testing architecture-specific issues
2. **Development**: During multi-stage builds (internal use)
3. **CI/CD**: Temporary testing in the build pipeline

## Regenerating After Changes

After adding or modifying `# arch:` comments:

```bash
make stages              # Regenerate GitHub Actions workflow
make generate-makefiles  # Regenerate Makefiles
```

The generated files will automatically reflect the new architecture restrictions.

## Implementation Details

The architecture detection and workflow generation is handled by `generate_stages.py`:

1. `extract_architectures()` - Parses `# arch:` comments from Dockerfiles
2. `generate_fine_grained_stages()` - Generates workflow with correct architecture matrix
3. `_generate_makefile_content()` - Generates Makefiles with architecture-aware targets

See `generate_stages.py` for implementation details.

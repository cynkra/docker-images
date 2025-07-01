# CLAUDE.md - Future Instructions

## 1. Use `pak::pak()` for R Package Installation

- **Always use** `pak::pak(c("package1", "package2"))` instead of `install.packages()`
- Benefits: faster parallel downloads, better dependency resolution, more robust error handling
- Example: `RUN R -q -e 'pak::pak(c("devtools", "usethis", "languageserver"))'`

## 2. Preserve Cache Invalidation Files

- **Do not remove** `COPY date.txt /date.txt` lines from Dockerfiles
- These files are used for build cache invalidation to ensure fresh package installations
- When date.txt changes, it forces rebuilds of the entire pipeline

## 3. Docker Image Architecture Best Practices

- Maintain logical build pipeline staging based on dependencies
- Use minimal image layers and appropriate base images
- Separate concerns: base images, R variants, specialized tools
- Document image purposes and dependencies clearly

# CLAUDE.md - Future Instructions

## 1. Use `pak::pak()` for R Package Installation

- **Always use** `pak::pak(c("package1", "package2"))` instead of `install.packages()`
- Benefits: faster parallel downloads, better dependency resolution, more robust error handling
- Example: `RUN R -q -e 'pak::pak(c("devtools", "usethis", "languageserver"))'`

## 2. Preserve Cache Invalidation Files

- **Do not remove** `COPY date.txt /date.txt` lines from Dockerfiles
- These files are used for build cache invalidation to ensure fresh package installations
- When date.txt changes, it forces rebuilds of the entire pipeline

## 3. Use Concatenated Commands for Layer Optimization

- **Always concatenate** related RUN commands using `&&` to minimize Docker layers
- **Always include cleanup** at the end. Ubuntu example: `rm -rf /var/lib/apt/lists/* && rm -rf /tmp/* && rm -rf /var/tmp/*`
- Group logical operations together: system package installation, R package installation, configuration
- RUN followed by backslash, && \ at the end of each line, true in the last line
- Example:

  ```dockerfile
  # Install system dependencies and R packages, then clean up
  RUN apt-get update && apt-get install -y package1 package2 && \
      R -q -e 'pak::pak(c("pkg1", "pkg2"))' && \
      rm -rf /var/lib/apt/lists/* && \
      rm -rf /tmp/* && \
      rm -rf /var/tmp/* && \
      true
  ```

## 4. Docker Image Architecture Best Practices

- Maintain logical build pipeline staging based on dependencies
- Use minimal image layers and appropriate base images
- Separate concerns: base images, R variants, specialized tools
- Document image purposes and dependencies clearly

## 5. Formatting

- Use pylint and black for Python code formatting

## 6. Always Update CLAUDE.md

- **Always update** this CLAUDE.md file when making changes to Docker images or establishing new patterns
- Include any new best practices, patterns, or important considerations discovered during development
- Keep this file as a comprehensive guide for future maintenance and development

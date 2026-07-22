# arch: amd64

FROM rhub/clang20

# Compile the duckdb R package from source with the image's clang toolchain.
# CRAN serves only source packages for Linux, and `type = "source"` makes the
# intent explicit: duckdb is built here, not pulled as a prebuilt binary.
# See duckdb/duckdb-r#1107.
RUN R -q -e 'options(repos = c(CRAN = "https://cloud.r-project.org")); install.packages("duckdb", type = "source")'

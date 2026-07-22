# arch: amd64

FROM rhub/clang18

# Compile the duckdb R package from source with the image's clang toolchain.
# CRAN serves only source packages for Linux, and `type = "source"` makes the
# intent explicit: duckdb is built here, not pulled as a prebuilt binary.
#
# This image installs *only* duckdb; installing extensions is the job of the
# child `clang18-duckdb/extension` image. `install.packages()` merely warns on a
# failed build (it exits 0), so the explicit `requireNamespace()` check turns a
# failed duckdb install into a hard build failure. See duckdb/duckdb-r#1107.
RUN R -q -e 'options(repos = c(CRAN = "https://cloud.r-project.org")); install.packages("duckdb", type = "source"); if (!requireNamespace("duckdb", quietly = TRUE)) stop("duckdb failed to install")'

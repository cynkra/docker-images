# arch: amd64

FROM rhub/clang18
RUN R -q -e 'options(repos = c(CRAN = "https://cloud.r-project.org")); install.packages("duckdb")'

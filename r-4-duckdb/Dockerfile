ARG r_ver=4.0.5
FROM rocker/r-ver:${r_ver}

RUN R -q -e 'install.packages("pak", repos = sprintf("https://r-lib.github.io/p/pak/stable/%s/%s/%s", .Platform$pkgType, R.Version()$os, R.Version()$arch))'

RUN R -q -e 'options(repos = "https://p3m.dev/cran/__linux__/focal/latest"); pak::pak(c("duckdb/duckdb-r", "dbplyr"))'

RUN apt update && apt install -y valgrind

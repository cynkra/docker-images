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

## Images

### [dm](dm)

FIXME

### [r-4-duckdb](r-4-duckdb)

FIXME

### [r-minimal](r-minimal)

FIXME

### [r-postgres](r-postgres)

FIXME

### [rig-centos7](rig-centos7)

FIXME

### [rig-debian](rig-debian)

FIXME

### [rig-rocky8](rig-rocky8)

FIXME

### [rig-ubuntu](rig-ubuntu)

FIXME

### [rig-ubuntu-dbi](rig-ubuntu-dbi)

FIXME

### [rig-ubuntu-duckdb](rig-ubuntu-duckdb)

FIXME

### [rig-ubuntu-duckdb-dev](rig-ubuntu-duckdb-dev)

FIXME

### [rig-ubuntu-igraph](rig-ubuntu-igraph)

FIXME

### [rig-ubuntu-revdepcheck](rig-ubuntu-revdepcheck)

FIXME

### [rigraph-san](rigraph-san)

FIXME

### [tofutf](tofutf)

FIXME

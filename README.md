# This repository contains all customized docker images

To add a new image:

1. Create a new directory.
2. Add all the necessary files to that new directory (Dockerfile + any dependencies).
3. Add the name of the directory to the `stages.yml` file. If the docker image depends on an existing one, add it to the next stage otherwise add it to stage-1.

---

To remove an existing image:

1. Make sure that no other docker files depends on it.
2. Remove the directory.
3. Remove the directory name from the `stages.yml` file.

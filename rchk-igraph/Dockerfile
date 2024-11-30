# Before changing this to 24.04, check if pak install from binary
FROM kalibera/rchk:latest

RUN apt-get update && apt-get install -y libglpk-dev && apt-get clean && rm -rf /var/lib/apt/lists/*

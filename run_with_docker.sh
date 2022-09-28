#!/bin/bash

set -x
set -e

mkdir -p bundle

docker rm -f jekyll

docker run --rm \
  -ti \
  --volume="$PWD:/srv/jekyll:Z" \
  --volume="$PWD/bundle:/usr/local/bundle:Z" \
  --publish [::1]:4000:4000 \
  --name jekyll \
  jekyll/minimal \
  bash serve.sh
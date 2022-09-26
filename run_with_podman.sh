#!/bin/bash

# podman rm -f jekyll
# podman run --rm \
#     -p 4000:4000  \
#     -v $(pwd):/site:Z \
#     --name jekyll \
#     bretfisher/jekyll-serve

set -x
set -e

mkdir -p bundle

podman rm -f jekyll

podman run --rm \
  -ti \
  -e JEKYLL_ROOTLESS=1  \
  --volume="$PWD:/srv/jekyll:Z" \
  --volume="$PWD/bundle:/usr/local/bundle:Z" \
  --publish [::1]:4000:4000 \
  --name jekyll \
  jekyll/minimal \
  bash serve.sh
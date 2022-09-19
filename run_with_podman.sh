#!/bin/bash

podman rm -f jekyll
podman run --rm \
    -p 4000:4000  \
    -v $(pwd):/site:Z \
    --name jekyll \
    bretfisher/jekyll-serve
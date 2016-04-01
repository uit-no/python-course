#!/bin/bash

# run this in the Vagrant VM to convert and serve a notebook as reveal.js
# slides on port 8889. Vagrant forwards that port to your host.

jupyter nbconvert "$1" --to slides --post serve --ServePostProcessor.ip=0.0.0.0 --ServePostProcessor.open_in_browser=False --ServePostProcessor.port=8889

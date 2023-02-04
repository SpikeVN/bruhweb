#!/usr/bin/sh
curl -fsSL https://deb.nodesource.com/setup_16.x | bash -
apt install -y nodejs
pc init
pc run --env prod
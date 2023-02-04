#!/usr/bin/sh
apt update -y
curl -fsSL https://deb.nodesource.com/setup_16.x | bash -
apt-get install -y nodejs
pc init
pc run --env prod
#!/usr/bin/sh
apt update -y
apt install nodejs npm -y
pc init
pc run --env prod
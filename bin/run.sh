#!/usr/bin/env bash

sudo python3 server/server.py /etc/letsencrypt/live/fapfap.e-software.dk/fullchain.pem /etc/letsencrypt/live/fapfap.e-software.dk/privkey.pem > log

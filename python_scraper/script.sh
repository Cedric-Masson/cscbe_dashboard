#!/bin/bash

/usr/local/bin/python3.12 /app/cscbe_scraper.py

printenv | grep -v "no_proxy" >> /etc/environment
cron -f
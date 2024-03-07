FROM python:3.12

# The project is stored in /app
WORKDIR /app

# Install the dependencies
RUN apt-get update && apt-get -y install cron vim libpq-dev
RUN pip install requests psycopg2

# Setting up a cron job every minute
COPY crontab /etc/cron.d/cron_scraper
RUN chmod 0644 /etc/cron.d/cron_scraper
RUN crontab /etc/cron.d/cron_scraper

COPY script.sh ./script.sh
RUN chmod +x /app/script.sh

COPY cscbe_scraper.py ./cscbe_scraper.py

CMD ./script.sh
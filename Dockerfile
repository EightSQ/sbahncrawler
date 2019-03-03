FROM python:3.7-alpine

LABEL	version="1.0" \
		description="A simple crawler." \
		cron.schedule="*/10 * * * *"

ENV CRAWLER_STATIONID 900000230003

VOLUME ["/data"]
RUN mkdir /app
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "crawler.py", "/data/data.csv"]

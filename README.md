# S-Bahn Datensammler
Sammelt Echtzeitdaten von Produkten des Berliner ÖPNV.

## Usage
1. Find the Station ID you are interested with [https://github.com/derhuerst/bvg-rest/blob/master/docs/index.md#get-locations](the bvg-rest API project).
2. 	With Docker:
	```
		$ docker build -t eightsq/sbahncrawler .
		$ docker run \
			-v {some_data_path_on_your_machine}:/data:rw \
			--rm \
			-e CRAWLER_STATIONID={your_station_id} \
			eightsq/sbahncrawler:latest
	```

	Without Docker:
	Make sure you have Python 3. Install the `requests` package. Then,
	```
		$ CRAWLER_STATIONID={your_station_id} python3 crawler.py <output_filename>
	```

Actually, since you want to automate this, set up cronjob, that does this regularly for you (like every 10").
To crawl a different product than S-Bahn, adjust the `productId` filter in the `crawl`-Function inside `crawler.py`.

## Author
EightSQ ([blog.8sq.de](Blog))

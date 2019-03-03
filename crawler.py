import os
import sys
import requests

# StationID variable, find via /locations query endpoint.
# See https://github.com/derhuerst/bvg-rest/blob/master/docs/index.md#get-locations
STATIONID = os.getenv('CRAWLER_STATIONID', '900000230003')
API_DEPARTURES_ENDPOINT = f'https://1.bvg.transport.rest/stations/{STATIONID}/departures'

def crawl(output_fd):
    '''Tries to crawl the api and log S-Bahn's (productCode=0) to filename.'''
    try:
        r = requests.get(API_DEPARTURES_ENDPOINT)

        if r.status_code != 200:
            raise requests.HTTPError()

        doc = r.json()
        for trip in doc:
            """Only log if productCode = 0 (suburban)"""
            """Change this filter accordingly!"""
            if trip['line']['productCode'] != 0:
                continue

            """Output in format
               tripid,departure_timestamp,linename,direction,delay"""
            output_fd.write(f'\"{trip["tripId"]}\",{trip["when"]},{trip["line"]["name"]},\"{trip["direction"]}\",{trip["delay"]}\n')

    except requests.ConnectionError:
        sys.stderr.write('ConnectionError connecting to the API\n')
        sys.exit
    except requests.HTTPError:
        sys.stderr.write(f'Invalid response from API. ({r.status_code})\n')
    except ValueError:
        sys.stderr.write('API seems to have responded no valid JSON.\n')


if __name__ == '__main__':
    out = sys.stdout
    csvheader = "tripid,departure_timestamp,linename,direction,delay\n"

    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            """No header if file already exists."""
            csvheader = ""
        out = open(sys.argv[1], 'a')

    out.write(csvheader)
    crawl(out)
    out.close()

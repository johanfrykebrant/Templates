import logging
import requests
import json
import simplejson

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

logging.basicConfig(filename='test.log', level=logging.WARNING,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# --- Not able to read file ---
try:
    with open("test.txt") as json_data_file:
        data = json.load(json_data_file)
except FileNotFoundError as e:
    logging.error(e)
except Exception as e:
    logging.error(e)
        

# --- Variable not defined ---  
try:
    a = b
except NameError as e:
    logging.error(e)

# --- API response 404 ---
SMHI_forecast = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/3/geotype/point/lon/13.07/lat/55.6/data.json"
response = requests.get(SMHI_forecast)

try:
    jobj = response.json()
except simplejson.scanner.JSONDecodeError as e:
    response = str(response)
    logging.error('{}, Response from API: {}'.format(e, response))
except Exception as e:
    print(type(e))
    logging.error(e)


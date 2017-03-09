#!/usr/bin/env python
import requests
import xml.etree.ElementTree as ET
import json
from datetime import datetime
import pandas as pd


airports = ['ATL', 'LAX', 'ORD', 'DFW', 'JFK', 'DEN', 'SFO', 'CLT', 'LAS',
            'PHX', 'MIA', 'IAH', 'SEA', 'MCO', 'MSP', 'BOS', 'DTW', 'PHL']
url = "http://services.faa.gov/airport/status/"
params = dict(
    format='json',)
d = {}
r = {}

the_time = datetime.now().replace(second=0, microsecond=0)
timestamp = the_time.strftime('%m-%d-%Y %H-%M')
r["update_time"] = timestamp


def str2bool(v):
    return v.lower() in ("true", "1")


info_table_columns = ["Name", "Reason", "Temperature", "Weather"]
info_table = []

for code in airports:
    url_with_airport = url + code
    resp = requests.get(url=url_with_airport, params=params)
    airport = json.loads(resp.text)
    d[airport['IATA']] = (str2bool(airport['delay']))
    if d[airport['IATA']]:
        info_table.append([airport["name"], airport["status"]["reason"],
                    airport["weather"]["temp"], airport["weather"]["weather"]])

info = pd.DataFrame(info_table, columns=info_table_columns)
r["airports"] = d


# {'airports': {'ATL': False,
#   'BOS': False,
#   'CLT': False,
#   'DEN': False,
#   'DFW': False,
#   'DTW': False,
#   'IAH': False,
#   'JFK': False,
#   'LAS': False,
#   'LAX': False,
#   'MCO': False,
#   'MIA': False,
#   'MSP': False,
#   'ORD': False,
#   'PHL': False,
#   'PHX': False,
#   'SEA': False,
#   'SFO': False},
#  'update_time': '03-03-2017 00-22'}

# Load empty map
tree = ET.parse('/home/ubuntu/static/airports.svg')
root = tree.getroot()

# Update map
for element in tree.iter():
    if element.tag.split("}")[1] == "circle":
        for c in r['airports']:
            if element.get("id") == c:
                if r["airports"][c]:
                    element.set("fill", "red")
                else:
                    element.set("fill", "green")

# Write SVG file
tree.write('/home/ubuntu/static/map.svg')


# Write delays Table
if info.shape[0] == 0:
    content = "<h2>Last updated: {}</h2><p>No Delays</p>".format(r['update_time'])
else:
    info.index += 1
    content = "<h2>Last updated: {}</h2>\n{}".format(r["update_time"], info.to_html())

# Write HTML with update information
html= '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8" /><title>Delay.io</title></head><body>{}</body></html>'.format(content)

with open("/home/ubuntu/static/table.html", "w") as f:
    f.write(html)

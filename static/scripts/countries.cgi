#!/usr/bin/env python
import json
import requests
from urllib3.exceptions import InsecureRequestWarning

COUNTRIES="https://restcountries.com/v3.1/all"

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

print("Content-Type: text/plain\n\n")
try:
    countrylist = requests.get(COUNTRIES, verify=False).json()
    countries = sorted([{"name": c["name"]["common"], "alpha2Code": c["cca2"]} for c in countrylist], key=lambda c: c["name"])
except Exception as e:
    countries = [{"name": "Unable to retrieve country list", "alpha2Code": "ZZ"}]

print(json.dumps({'countries': countries}))

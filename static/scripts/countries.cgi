#!/usr/bin/env python3
import random, simplejson, requests

COUNTRIES = "https://countries.dev/countries?fields=name,alpha2Code"

print("Content-Type: text/plain\n\n")
try:
    response = requests.get(COUNTRIES)
    countries= response.json()
    countries_sorted = sorted(countries, key=lambda x: x["name"])
except:
    countries = [{"name": "Unable to retrieve country list", "alpha2Code": "ZZ"}]

print(simplejson.dumps({'countries': countries}))

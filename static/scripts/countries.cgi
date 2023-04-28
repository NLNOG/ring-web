#!/usr/bin/env python3
import random, simplejson, urllib.request

COUNTRIES="https://restcountries.com/v3.1/all"

print("Content-Type: text/plain\n\n")
try:
    countrylist = simplejson.load(urllib.request.urlopen(COUNTRIES))
    countries = sorted([{"name": c["name"]["common"], "alpha2Code": c["cca2"]} for c in countrylist], key=lambda c: c["name"])

except:
    countries = [{"name": "Unable to retrieve country list", "alpha2Code": "ZZ"}]

print(simplejson.dumps({'countries': countries}))

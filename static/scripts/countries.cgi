#!/usr/bin/env python
import random, simplejson, urllib

COUNTRIES="https://restcountries.com/v3.1/all"

print("Content-Type: text/plain\n\n")
try:
    countrylist = simplejson.load(urllib.urlopen(COUNTRIES))
    countries = sorted([{"name": c["name"]["common"], "alpha2Code": c["cca2"]} for c in countrylist], key=lambda c: c["name"])

except:
    countries = [{"name": "Unable to retrieve country list", "alpha2Code": "ZZ"}]

print(simplejson.dumps({'countries': countries}))

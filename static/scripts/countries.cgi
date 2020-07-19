#!/usr/bin/env python
import random, simplejson, urllib

COUNTRIES="https://restcountries.eu/rest/v2/all"

print("Content-Type: text/plain\n\n")
try:
    countries = simplejson.load(urllib.urlopen(COUNTRIES))

except:
    countries = [{"name": "Unable to retrieve country list", "alpha2Code": "ZZ"}]

print(simplejson.dumps({'countries': countries}))

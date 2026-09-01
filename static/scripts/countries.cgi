#!/usr/bin/env python3
import random, simplejson, requests

COUNTRIES = "https://api.restcountries.com/countries/v5?response_fields=names.common,codes.alpha_2"
with open("../../restcountries.token", "r") as f:
        TOKEN = f.readline().strip()

print("Content-Type: text/plain\n\n")
try:
    offset = 0
    countries = []
    while True:
        response = requests.get(f"{COUNTRIES}&limit=100&offset={offset}",
                                headers={'Authorization': TOKEN})
        countrylist = response.json()
        countries_tmp = [{"name": c["names"]["common"], "alpha2Code": c["codes"]["alpha_2"]} for c in countrylist["data"]["objects"]]
        countries = countries + countries_tmp
        if countrylist["data"]["meta"]["more"] != True:
            break
        else:
            offset = offset + 100

    countries_sorted = sorted(countries, key=lambda x: x["name"])

except:
    countries = [{"name": "Unable to retrieve country list", "alpha2Code": "ZZ"}]

print(simplejson.dumps({'countries': countries}))

#!/usr/bin/env python3
import simplejson, urllib.request, yaml

SWYAML="https://raw.githubusercontent.com/NLNOG/ring-ansible/master/roles/software/vars/install.yml"


print("Content-Type: text/plain\n\n")
software = {}
try:
    software = yaml.safe_load(urllib.request.urlopen(SWYAML))
except:
    pass

if not 'software' in software.keys():
    software = {'software':{'all':['N/A']}}

print(simplejson.dumps(software))

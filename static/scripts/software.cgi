#!/usr/bin/env python
import simplejson, urllib, yaml

SWYAML="https://raw.githubusercontent.com/NLNOG/ring-ansible/master/roles/software/vars/install.yml"


print("Content-Type: text/plain\n\n")
try:
    software = yaml.safe_load(urllib.urlopen(SWYAML))
except:
    software = {'all': 'N/A'}

print(simplejson.dumps(software))

#! /usr/bin/env python3
import json
import requests
import pycountry

style = {
    None: "err",
    0: "err",
    1: "ok",
}

nodestatus = {
    None: "inactive",
    0: "inactive",
    1: "active",
}

alive = {
    None: "offline",
    0: "offline",
    1: "online",
}

participants = requests.get("https://api.ring.nlnog.net/1.0/participants").json()["results"]["participants"]
pmap = {}
for p in participants:
    pname = p["company"]
    if len(pname) > 30:
        pname = pname[:25] + "..."
    pmap[p["id"]] = f"""<a href='{p.get("url", "")}' target=_blank title='{p['company']}'>{pname}</a>"""

nodes = requests.get("https://api.ring.nlnog.net/1.0/nodes").json()
for node in nodes["results"]["nodes"]:
    node["hostname"] = f"<a href='https://map.ring.nlnog.net/?node={node['id']}'><div title='node is {nodestatus[node['active']]}' class='pre node_{style[node['active']]}'>{node['hostname'].replace('.ring.nlnog.net', '')}</div></a>"
    node["participant"] = f"{pmap[node['participant']]}<a href='https://www.peeringdb.com/asn/{node['asn']}'><div class='pre'>AS{node['asn']}</div></a>"
    node["ip"] = ""
    if node["ipv4"]:
        node["ip"] = f"<div title='node is {alive[node['alive_ipv4']]} on IPv4' class='pre node_{style[node['alive_ipv4']]}'>{node['ipv4']}</div>"
    if node["ipv6"]:
        node["ip"] = f"{node['ip']}<div title='node is {alive[node['alive_ipv6']]} on IPv6' class='pre node_{style[node['alive_ipv6']]}'>{node['ipv6']}</div>"
    country = pycountry.countries.get(alpha_2=node["countrycode"])
    node["location"] = f"{country.name} ({country.alpha_2}) {country.flag}"
    if node["city"]:
        node["location"] = f"{node['city']}<br>{node['location']}"

print("Content-Type: application/json\n\n")
print(json.dumps(nodes["results"]["nodes"]))

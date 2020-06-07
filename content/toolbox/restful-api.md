+++
title = "RESTful API"
aliases = ["toolbox-api", "rest-api"]
layout = "single"
+++

API access to the RING database is available via:

> https://api.ring.nlnog.net/

## How to use the API
Example: `https://api.ring.nlnog.net/1.0/nodes/active/country/BE` returns all active nodes in Belgium.

The response has the following format:
```
{
  "info": {
    "resultcount": 3,
    "success": 1
  },
  "results": {
    "nodes": [
      {
        "statecode": null,
        "active": 1,
        "geo": "50.870572,4.47695",
        "id": 248,
        "datacenter": "Interxion Brussel",
        "participant": 228,
        "countrycode": "BE",
        "hostname": "combell01.ring.nlnog.net",
        "asn": 34762,
        "ipv4": "37.148.176.54",
        "ipv6": "2a00:1c98:10:7::2"
      },
      {
        "statecode": null,
        "active": 1,
        "geo": "50.887222,4.455278",
        "id": 168,
        "datacenter": "",
        "participant": 154,
        "countrycode": "BE",
        "hostname": "openminds01.ring.nlnog.net",
        "asn": 30961,
        "ipv4": "188.93.100.32",
        "ipv6": "2a02:d08:1001:201::1000"
      },
      {
        "statecode": null,
        "active": 1,
        "geo": "50.881431,4.454129",
        "id": 68,
        "datacenter": null,
        "participant": 66,
        "countrycode": "BE",
        "hostname": "boxed-it01.ring.nlnog.net",
        "asn": 50156,
        "ipv4": "195.200.224.123",
        "ipv6": "2001:67c:344:1010:5054:ff:feca:6f60"
      }
    ]
  }
}
```
In case of an error the following output format is used:
```
{
  "info": {
    "errormessage": "Error connecting to database: (2005, \"Unknown MySQL server host 'not.the.db.server.ring.nlnog.net' (2)\")",
    "success": 0
  }
}
```
See [https://api.ring.nlnog.net/1.0](https://api.ring.nlnog.net/1.0) for an overview of all available targets.


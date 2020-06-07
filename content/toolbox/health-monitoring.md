+++
title = "Health Monitoring"
aliases = ["ring-health"]
layout = "single"
+++

Each RING node runs a health monitoring script to check various parameters, such as free disk space, external connectivity and DNS resolver status. A report of a node’s health status is available on the following URL:
```
http://<node_name>.ring.nlnog.net/status.json
```

The health report has the following format:
```
{
  "info": {
    "success": true,
    "date": "2019-01-29T20:01:59.528466"
  },
  "health": {
    "mountstatus_root": true,
    "diskspace_root": true,
    "ipv6_addresses": true,
    "ipv6_gateway": true,
    "ipv6_reachability": true,
    "ipv4_addresses": true,
    "ipv4_gateway": true,
    "ipv4_reachability": true,
    "dns_config": true,
    "dns_resolvers": true,
    "https_github": true,
    "http_aptrepo_bit": true,
    "http_aptrepo_ring": true,
    "ansible_cron": true,
    "ansible_run": true,
    "ipv4_ringapi": true,
    "ipv6_ringapi": true
  },
  "descriptions": {
    "mountstatus_root": "The root filesystem is in read/write status",
    "diskspace_root": "The root filesystem has enough free disk space",
    "ipv6_addresses": "The IPv6 address of the node matches the ring database",
    "ipv6_gateway": "The IPv6 gateway is reachable",
    "ipv6_reachability": "There is IPv6 connectivity beyond the gateway",
    "ipv4_addresses": "The IPv4 address of the node matches the ring database",
    "ipv4_gateway": "The IPv4 gateway is reachable",
    "ipv4_reachability": "There is IPv4 connectivity beyond the gateway",
    "dns_config": "The local host is configured as DNS resolver",
    "dns_resolvers": "The configured DNS resolvers are functioning",
    "https_github": "A webrequest for 'https://github.com/' succeeded",
    "http_aptrepo_bit": "A webrequest for 'http://ftp.bit.nl/ubuntu' succeeded",
    "http_aptrepo_ring": "A webrequest for 'http://apt.ring.nlnog.net/deb/dists/ring/Release' succeeded",
    "ansible_cron": "The ansible cron job is correctly configured",
    "ansible_run": "Ansible has recently run",
    "ipv4_ringapi": "Pushing this health report to the IPv4 ring API succeeded",
    "ipv6_ringapi": "Pushing this health report to the IPv6 ring API succeeded"
  }
}
```
Our administration system currently uses the reports to actively contact owners of RING nodes that have not completed their Ansible runs or for which there is a problem with IPv4 or IPv6 connectivity. We encourage participants to add the above URL to their monitoring systems to actively monitor their own nodes.


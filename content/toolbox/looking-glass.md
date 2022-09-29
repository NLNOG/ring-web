+++
title = "Looking Glass"
aliases = ["lg", "lookingglass"]
layout = "single"
+++

## Looking Glass web interface
There is a public web interface available at the following address:

> https://lg.ring.nlnog.net/

Currently the ring LG uses [OpenBGPd](https://openbgpd.org/) as the BGP speaker.

## How to use the Looking Glass through SSH

With recent updates to the web-based interface, the SSH access through `lg01.infra.ring.nlnog.net` became obsolete.

## Peering with the Looking Glass
Peering with this Looking Glass is optional for ring users. If you want to peer with NLNOG RING, send [us](mailto:ring-admins@nlnog.net) your details or create a [pull-request](https://github.com/NLNOG/ring-ansible/blob/master/roles/openbgpd/vars/peers.yml), and configure a session with the following information:
```
AS: 199036
IPv4: 212.114.120.72 (lg02.infra.ring.nlnog.net)
IPv6: 2001:7b8:62b:1:0:d4ff:fe72:7848 (lg02.infra.ring.nlnog.net)
Type: eBGP Multi-Hop
Policy: import NONE from AS199036, export ANY
```
The fine people at [BIT](https://www.bit.nl/) sponsored the RING with the Autonomous System – `AS199036`.


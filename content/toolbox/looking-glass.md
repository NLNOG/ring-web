+++
title = "Looking Glass"
aliases = ["lg", "lookingglass"]
layout = "single"
+++

## Looking Glass web interface
There is a public web interface available at the following address:

> https://lg.ring.nlnog.net/

## How to use the Looking Glass through SSH
The NLNOG RING offers a looking glass, solely accessible through SSH by RING users! You can ssh to `lg01.infra.ring.nlnog.net`. Don’t forget to use the proper username! If you ssh to this host you should drop straight to a dialog menu, where you can select either IPv4 or IPv6. Here are some pointers how to retrieve information:

* Show detailed information for a prefix or IP:
  ```
  show route for 85.184.184.1 all
  ```
* Show all routes originated by `AS15562`:
  ```
  show route where bgp_path.last = 15562
  ```
* Show all routes which have `AS5580` in the path:
  ```
  show route where bgp_path ~ [= * 5580 * =]
  ```
* Equivalent of `show bgp sum`:
  ```
  show protocols
  ```
Currently the ring is using [BIRD](https://bird.network.cz/) as the BGP speaker, it might take some getting used to get valuable information out of it. ;-)

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


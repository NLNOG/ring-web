+++
author = "Job Snijders"
title = "RING success - the IPv4 .255 problem"
date = "2012-10-16"
description = "RING success - the IPv4 .255 problem"
categories = [
    "announcement",
]
+++

*This is an example one of the RING participants (BelW&uuml;) wanted to share with all RING participants.*

Some days ago a customer of us encountered problems with connecting from another ISPs (via DSL) to his VPN concentrator in his head-office network which is connected through us.

Unfortunately the other ISP does not participate within the RING.  But nevertheless I did a RING-traceroute to the VPN concentrator to check if there are (other) reachability problems. The customer was reachable from all other sites but not from keenondots01.  So I looked deeper into that, tried some traceroutes etc. and noticed this in /etc/hosts:

`91.218.150.255  keenondots01    keenondots01.ring.nlnog.net`

Mh, a .255 IPv4 address...  Until that time I did not known the source IP address on the remote (DSL) site, asked the customer, and yes it was a .255 address.  So the problem was that some old firewall statements denied all IPv4 addresses with 255 in the last octet.  And this was easy to fix.

I think it's great to have that variation of IP addresses, AS numbers, upstreams, firewalls (or at least basic access-lists) etc. within the RING.  So even if another ISP does not participate within the RING there is maybe a RING participant with a similar setup for its RING node which will give you the hint to find the solution for your problem.


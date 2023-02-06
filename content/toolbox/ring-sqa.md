+++
title = "RING SQA"
aliases = ["sqa"]
layout = "single"
+++

The purpose of [RING SQA](https://github.com/NLNOG/ring-sqa) is to detect outages as fast as possible that only affect a subset of all internet destinations.

RING SQA pings all other nodes (IPv4 + IPv6) every 30 seconds to derive a baseline, this baseline is compared to the last 3 minutes of measurements. If the median of the baseline is tripped for three consecutives minutes, an alarm is raised.

When an alarm is raised, three MTRs are immediately launched towards destinations that previously were reachable, but suddenly not anymore. The purpose of these traces is to provide an investigation starting point for your NOC.

All in all super fast outage detection. All participants are invited to use this system! Gratis! :-)

One can simply configure where alerts should be emailed by changing the `/etc/ring-sqa/alarm.conf` file on your own RING node(s) to something like this (do keep in mind the indenting!):

```
job@ringnode01.ring.nlnog.net:~$ sudo cat /etc/ring-sqa/alarm.conf
---
email:
  to: noc@yourcompany.com
  from: sqa-alert@ your_ring_node .ring.nlnog.net
  prefix: 'RING ALERT '
irc:
  host: 1.2.3.4
  port: 5502
  password: derp
  channel: ! '#noc'
```    
Afterwards restart the ring-sqa daemons to load the new config:
```
job@ringnode01:~$ sudo systemctl restart ring-sqa4
job@ringnode01:~$ sudo systemctl restart ring-sqa6
```
Et voila! After 30 minutes the machine will stand guard over your network. RING participants with multiple hubs or datacenters will benefit from spinning up more nodes, as monitoring is from each RING nodes individual perspective.

We extend a HUGE thank you to [Saku Ytti](https://github.com/ytti) who wrote RING SQA. Please send him beer, chocolate, and flowers.

Below we’ve included an example outage alert.

```
------------------ Example RING SQA Message ---------------------------

From: sqa@xing02.ring.nlnog.net
To: noc@
Subject: RING ALERT raising ipv4 alarm - 16 new nodes down
Body:

Regarding: xing02.ring.nlnog.net ipv4

This is an automated alert from the distributed partial outage 
monitoring system "RING SQA".

At 2014-07-27 10:18:05 UTC the following measurements were analysed 
as indicating that there is a high probability your NLNOG RING node 
cannot reach the entire internet. Possible causes could be an outage 
in your upstream's or peer's network.

The following nodes previously were reachable, but became unreachable 
over the course of the last 3 minutes:

- itps01.ring.nlnog.net            128.65.97.93 AS42010 GB
- fullsave01.ring.nlnog.net       141.0.202.201 AS39405 FR
- globalaxs01.ring.nlnog.net       176.10.80.10 AS 9009 GB
- kwaoo01.ring.nlnog.net         178.250.209.33 AS24904 CH
- suretec01.ring.nlnog.net          185.8.92.17 AS199659 GB
- swisscom01.ring.nlnog.net      193.247.170.254 AS 3303 CH
- claranet01.ring.nlnog.net         195.157.9.4 AS 8426 GB
- claranet04.ring.nlnog.net        195.22.19.34 AS 8426 PT
- dcsone01.ring.nlnog.net         203.123.48.14 AS37989 SG
- trueinternet01.ring.nlnog.net  203.144.167.57 AS 7470 TH
- jump01.ring.nlnog.net          212.13.217.117 AS 8943 GB
- lchost01.ring.nlnog.net        213.230.217.125 AS25098 GB
- suomi01.ring.nlnog.net         217.119.42.194 AS16302 FI
- melbourne01.ring.nlnog.net     37.128.187.253 AS39451 GB
- netability01.ring.nlnog.net       46.182.9.20 AS 1197 IE
- viatel02.ring.nlnog.net          46.183.108.2 AS31122 FR
- claranet06.ring.nlnog.net          92.54.7.29 AS 8426 ES


As a debug starting point 3 traceroutes were launched right after 
detecting the event, they might assist in pinpointing what broke:

trueinternet01.ring.nlnog.net  AS 7470 (TH)
mtr -i0.5 -c5 -r -w -n 203.144.167.57
  1.|-- 109.233.156.241        0.0%     6    0.5   0.5   0.5   0.6   0.0
  2.|-- 109.233.156.1          0.0%     5    0.8   0.9   0.8   1.1   0.1
  3.|-- 109.233.156.2          0.0%     5    0.8   0.8   0.8   0.9   0.0
  4.|-- 64.209.88.33           0.0%     5    0.9   1.0   0.9   1.5   0.3
  5.|-- 159.63.23.198         60.0%     5  265.1 264.9 264.7 265.1   0.3
  6.|-- ???                   100.0     5    0.0   0.0   0.0   0.0   0.0
  7.|-- ???                   100.0     5    0.0   0.0   0.0   0.0   0.0
  8.|-- ???                   100.0     5    0.0   0.0   0.0   0.0   0.0
  9.|-- ???                   100.0     5    0.0   0.0   0.0   0.0   0.0
 10.|-- ???                   100.0     5    0.0   0.0   0.0   0.0   0.0
 11.|-- 203.144.144.30        80.0%     5  297.4 297.4 297.4 297.4   0.0
 12.|-- ???                   100.0     4    0.0   0.0   0.0   0.0   0.0

fullsave01.ring.nlnog.net      AS39405 (FR)
mtr -i0.5 -c5 -r -w -n 141.0.202.201
  1.|-- 109.233.156.241        0.0%     6    0.5   0.5   0.5   0.5   0.0
  2.|-- 109.233.156.1          0.0%     5    0.8   3.2   0.8  12.2   5.0
  3.|-- 109.233.156.2          0.0%     5    0.8   0.9   0.8   1.0   0.1
  4.|-- 109.233.156.37         0.0%     5    1.0   1.0   0.9   1.5   0.3
  5.|-- 149.11.106.1           0.0%     5    1.1   1.4   1.1   1.7   0.2
  6.|-- 130.117.3.137          0.0%     5    1.5   1.7   1.5   1.8   0.2
  7.|-- 154.54.62.77           0.0%     5   11.4  11.7  11.3  13.0   0.7
  8.|-- 154.54.75.154          0.0%     5  201.0 166.9  66.9 323.0 101.5
  9.|-- 154.54.56.214          0.0%     5   23.0  23.0  22.8  23.0   0.1
 10.|-- 149.11.58.62          80.0%     5   26.4  26.4  26.4  26.4   0.0
 11.|-- ???                   100.0     5    0.0   0.0   0.0   0.0   0.0
 12.|-- 141.0.202.201         80.0%     5   25.0  25.0  25.0  25.0   0.0

globalaxs01.ring.nlnog.net     AS 9009 (GB)
mtr -i0.5 -c5 -r -w -n 176.10.80.10
  1.|-- 109.233.156.241        0.0%     6    0.4   0.5   0.4   0.5   0.0
  2.|-- 109.233.156.1          0.0%     5    0.9   1.8   0.7   5.3   1.9
  3.|-- 81.201.115.41          0.0%     5    0.9   0.9   0.8   1.0   0.1
  4.|-- 62.209.32.18          40.0%     5    1.3   1.2   1.2   1.3   0.1
  5.|-- 80.81.192.165          0.0%     5    1.3   9.3   1.2  41.5  18.0
  6.|-- 193.27.64.245         60.0%     5  191.9 108.1  24.3 191.9 118.5
  7.|-- 193.27.64.66          80.0%     5   43.6  43.6  43.6  43.6   0.0
  8.|-- ???                   100.0     5    0.0   0.0   0.0   0.0   0.0
  9.|-- ???                   100.0     5    0.0   0.0   0.0   0.0   0.0
 10.|-- 176.10.80.2           80.0%     5   26.1  26.1  26.1  26.1   0.0
 11.|-- ???                   100.0     5    0.0   0.0   0.0   0.0   0.0
 12.|-- ???                   100.0     4    0.0   0.0   0.0   0.0   0.0
 13.|-- ???                   100.0     3    0.0   0.0   0.0   0.0   0.0
 14.|-- ???                   100.0     2    0.0   0.0   0.0   0.0   0.0
 15.|-- 176.10.80.10           0.0%     1   24.3  24.3  24.3  24.3   0.0



An alarm is raised under the following conditions: every 30 seconds 
your node pings all other nodes. The amount of nodes that cannot be 
reached is stored in a circular buffer, with each element representing 
a minute of measurements. In the event that the last three minutes are 
1.2 above the median of the previous 27 measurement slots, a partial 
outage is assumed. The ring buffer's output is as following:

29 min ago  41 measurements failed (baseline)
28 min ago  41 measurements failed (baseline)
27 min ago  41 measurements failed (baseline)
26 min ago  42 measurements failed (baseline)
25 min ago  41 measurements failed (baseline)
24 min ago  41 measurements failed (baseline)
23 min ago  41 measurements failed (baseline)
22 min ago  41 measurements failed (baseline)
21 min ago  41 measurements failed (baseline)
20 min ago  41 measurements failed (baseline)
19 min ago  41 measurements failed (baseline)
18 min ago  41 measurements failed (baseline)
17 min ago  41 measurements failed (baseline)
16 min ago  41 measurements failed (baseline)
15 min ago  41 measurements failed (baseline)
14 min ago  41 measurements failed (baseline)
13 min ago  41 measurements failed (baseline)
12 min ago  41 measurements failed (baseline)
11 min ago  41 measurements failed (baseline)
10 min ago  41 measurements failed (baseline)
 9 min ago  41 measurements failed (baseline)
 8 min ago  41 measurements failed (baseline)
 7 min ago  41 measurements failed (baseline)
 6 min ago  41 measurements failed (baseline)
 5 min ago  41 measurements failed (baseline)
 4 min ago  41 measurements failed (baseline)
 3 min ago  45 measurements failed (baseline)
 2 min ago  66 measurements failed (raised alarm)
 1 min ago  65 measurements failed (raised alarm)
 0 min ago  65 measurements failed (raised alarm)
```


+++
author = "Job Snijders"
title = "Routing issue root cause analysis using AMP"
date = "2012-10-02"
description = "Routing issue root cause analysis using AMP"
categories = [
    "announcement",
]
+++

*This is an example one of the RING participants (eBay Classifieds Group) wanted to share with all RING participants.*


Several weeks ago we ([eBay Classifieds Group](http://www.ebayclassifiedsgroup.com)) encountered an issue with some customers coming from Denmark (more precise, TDC customers), having issues reaching websites in the [eBay Classifieds Grou](http://www.ebayclassifiedsgroup.com) network. These issues were showing as a slow website, and packetloss to our network. This lasted for some time, but it didn't escalate in time to me, so by the time it did, the issue was already gone.

Now I haven't been following the connected member list for the NLNOG/RING project, but Job Snijders pointed me out that TDC does have a RING node!

Now Job showed me during that weekend while we had some drinks, his new cool tool on the ring, it was even better then what I did pitch to him some moons ago. Not just latency monitoring, but the NLNOG/RING project keeps track of the number of hops, and keeping archives of traceroutes. And it all presents it in a very nice interface.

### Debugging:

First, looked up the actual issue at hand.

**AMP Latency Measurement:**
[![A](http://www.maartenmoerman.nl/screenshots/cab82340f10eedd1.png)](http://amp.ring.nlnog.net/graph.php?graph=576b-icmp-latency&src=ring-tdc01&dst=ring-ebayclassifiedsgroup01&date=2012-08-01&rge=8-day&use=1&xmin=1343779200000&xmax=1343865600000&ymin=0&ymax=120&boxes=mean_jitter_loss)

From 13:40 there is an increased jitter, and packet loss visible! So, let's check out that cool graph that displays number of hops history.

**AMP Path Analysis:**
[![B](http://www.maartenmoerman.nl/screenshots/b65bf124005a46cb.png)](http://amp.ring.nlnog.net//graph.php?src=ring-tdc01&dst=ring-ebayclassifiedsgroup01&graph=scamper-trace-Pudp_paris-d0-s0-f1-g5-m32-l1-q2-M1&rge=1-day&date=2012-08-01)

And we see increase in number of hops, now let's take a look at the actual 'traceroute' history.

**AMP Traceroute History:**
[![C](http://www.maartenmoerman.nl/screenshots/9ccc426a12b532e3.png)](http://amp.ring.nlnog.net/trace_detail.php?src=ring-ebayclassifiedsgroup01&dst=ring-tdc01&date=2012-08-01#49500)

Take a small look at 13:45 on August 1st, hey... why has the traceroute from ECG towards TDC changed into going over the AMS-IX platform instead of the usual Level3 path?  We see the real cause at 14:00, the number 3 hop has become Novatel in Bulgary.

Now, a quick search in my mailbox reveals that Novatel recently connected to AMS-IX, also this is listed on the AMS-IX "connected" page.

[![AMS-IX](http://instituut.net/~job/screenshots/e8228bcde9a5eb7f.png)]()

### Conclusion:

It seems Novatel went live at AMS-IX the day before, my idea is that they accidentally leaked their NTT routes via the AMS-IX routeservers, and had their NTT link congested by doing so. This might have been prevented if the AMS-IX routeservers would have done strict RPSL checking.

If you have any questions regarding the use of the tool, or question about this article, don't hesitate to contact me: [Maarten Moerman / mmoerman@ebay.com](mailto:mmoerman@ebay.com)


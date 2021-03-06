+++
author = "Teun Vink"
title = "ring-trace"
date = "2011-11-29"
description = "ring-trace"
categories = [
    "announcement",
]
+++

One of the nice features of the ring is the ability to view routing information from a large (and growing!) number of sources all around te world. We can combine this information to create cool things, like graphs which show the similarities and differences in traceroutes towards a common destination. This is exactly what `ring-trace` does. More detailed information on how to use `ring-trace` can be found on the [Toolbox](http://ring.nlnog.net/toolbox/) page.

Here are a few examples of graphs generated by ring-trace which show some interesting things:

[![trace-www.apple.com](/images/post/ring-trace/apple-thumb.jpg)](/images/post/ring-trace/trace-www.apple_.com_.jpg)
[![trace-www.telstra.net](/images/post/ring-trace/telstra-thumb.jpg)](/images/post/ring-trace/trace-www.telstra.net_.jpg)
[![trace-www.ripe.net](/images/post/ring-trace/ripe-thumb.jpg)](/images/post/ring-trace/trace-www.ripe_.net_.jpg)
[![trace-www.arin.net](/images/post/ring-trace/arin-thumb.jpg)](/images/post/ring-trace/trace-www.arin_.net_.jpg)

The traces towards `www.apple.com` show indications on how Apple implemented global loadbalancing. The trace towards `www.telstra.net` is a nice example of a host "far away", which gives us some indications of the transit providers used by various networks. The traces towards `www.arin.net` show a somewhat similar picture. The `www.ripe.net` show some IPv6 traces with 'broken' hops in it.

`ring-trace` can be downloaded [here](https://github.com/SnijdersIT/nlnog-ring/raw/master/scripts/ring-trace). It requires `graphviz` and `python-dnspython` packages on Ubuntu. Bug reports, fixes and suggestions for additional code are welcome of course, as well as graphs of the most awesome traces around the world.


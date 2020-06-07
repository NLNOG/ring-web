+++
author = "Job Snijders"
title = "Distributed Smokeping"
date = "2011-01-18"
description = "Distributed Smokeping"
categories = [
    "announcement",
]
+++

**UPDATE:** Due to scalability issues with the smokeping master/slave architecture we had to abandon this type of measurements in early 2013.

A [smokeping](http://oss.oetiker.ch/smokeping/) Master/Slave setup has been created to graph latency between all nodes thus graphing nodes in context of a torus. With this smokeping setup problems on the Dutch internet exchanges such as AMS-IX or NL-IX are easily made visible. Also malfunctioning route-servers can be spotted.

Here is a sample image:

[![smokeping](/images/post/distributed-smokeping/lroot_mini-300x119.png)](/images/post/distributed-smokeping/lroot_mini.png)

Please visit the [NLNOG RING Smokeping](http://ring.nlnog.net/smokeping)



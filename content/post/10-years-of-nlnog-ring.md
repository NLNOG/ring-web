+++
author = "Martin Pels"
title = "10 years of NLNOG RING"
date = "2021-01-31"
description = "10 years of NLNOG RING"
categories = [
    "announcement",
]
+++

This month marks the tenth anniversary of the [NLNOG RING](https://ring.nlnog.net/) project.
In this article we look back on how the project came to be and how it evolved over this past decade.

### A network engineer’s tale…

The story of NLNOG RING starts on the [#nlnog](https://nlnog.net/irc/) IRC channel, at the end of 2010.
A network engineer received complaints that his customers had difficulty reaching various destinations in several Dutch networks.
The case was a curious one, because the problem would come and go.
Some TCP sessions would establish immediately, whereas others would take multiple attempts before a connection was made.
It was clear something was broken, but locating the root cause proved to be difficult.

To find the source of the problem, the engineer proceeded to ask engineers from other networks for traceroute outputs, gathering data about how packets would travel from their networks to his.
The other engineers were of course happy to help, but because each question had to be answered individually it took a long time to gather the necessary data.
All in all it took several days to get a complete picture and identify a root cause, which turned out to be a faulty backbone link within the fabric of a large Dutch internet exchange point.

![Manual coordination of network troubleshooting](/images/post/10-years-of-nlnog-ring/original-problem.png "Manual coordination of network troubleshooting")

During the surrounding discussion on the IRC channel, seeing the amount of effort it took to collect the required information from different vantage points, the question came up: “What if we had a way for an engineer to access other networks securely, and collect troubleshooting data, without having to wait for the other side?”
Several people immediately offered to dedicate servers or virtual machines to the project, and a few others started building tooling for software installation and user management.
And so, in January 2011, NLNOG RING [was born](http://mailman.nlnog.net/pipermail/nlnog/2011-January/002433.html).

### Architecture and tools

The NLNOG RING is a “looking glass on steroids”. Participants join the project by making a (virtual) server available, hosted inside their own network. In return they gain access to their own shell account on all the machines provided by all other participating networks.

Right from the start we were conscious of the fact that we would have to manage a potentially large number of systems with a small group of volunteers.
To do this in a time-efficient manner we deployed [Puppet](https://puppet.com/) on all provided systems.
This allowed us to install software tools and configure users in a centralized manner.
To further limit the scope of work we decided to support only a single operating system: [Ubuntu LTS](https://ubuntu.com/blog/what-is-an-ubuntu-lts-release).
For security we did not want to rely on passwords. All user access is controlled through SSH keys and there is no superuser access for any of the participants.

The basis of the NLNOG RING is a shell account, which offers a lot of freedom to participants to run their own troubleshooting scripts or programs.
To add extra value to this, each machine is provisioned with a collection of commonly used network troubleshooting tools.
We provide a DNS-interface and a [RESTful API](https://ring.nlnog.net/toolbox/restful-api/) for retrieving participant and node information, and we have a regular BGP [looking glass](http://lg.ring.nlnog.net/) providing insight into many networks.

NLNOG RING is a community project.
Over the years, many people have contributed tools and code to make the project more useful.
One of the first tools was [ring-trace](https://github.com/NLNOG/nlnog-ring/blob/master/scripts/ring-trace), a piece of software to run traceroutes from different vantage points, and display them in a graphical format.

![Example of ring-trace output](/images/post/10-years-of-nlnog-ring/trace-ring.nlnog.net.jpeg "Example of ring-trace output")

Another user-contributed tool is [ring-sqa](https://github.com/NLNOG/ring-sqa), a piece of software that attempts to automatically detect connectivity problems between NLNOG RING nodes and notifies their owners.
Events are also correlated to detect larger, sometimes Internet-wide outages, which are published on a [dashboard](http://sqa.ring.nlnog.net/).

Since 2013 we also cooperate with [RIPE Atlas](https://atlas.ripe.net/), to combine the strengths of the two platforms.
NLNOG RING nodes are selectable as [measurement targets](https://atlas.ripe.net/targets/ringnodes/list/) in the RIPE Atlas interface.
Furthermore, the RIPE Atlas [tools package](https://github.com/RIPE-NCC/ripe-atlas-tools) is installed on all NLNOG RING nodes, so participants can integrate RIPE Atlas measurements in scripts run on the RING.

### Operating model and sponsoring

The NLNOG RING was started by a couple of network engineers in their free time, and is still completely run by a small number of volunteers.
All participating networks provide their own machines.
In most cases (75%) this is a VM, making the barrier to participate very low.

At the start of the project all management tooling was running on infrastructure from [InTouch](https://intouch.eu/), the employer of one of our founding volunteers.
As the project grew the requirement for some dedicated management infrastructure arose.
In 2013 we successfully held a [fundraiser](https://ring.nlnog.net/post/ring-fundraiser-successfully-closed/), which enabled us to obtain the necessary hardware for hosting our management tooling.
Over the years more [sponsors](https://ring.nlnog.net/patrons/) donated resources. These generous donations help us to run the project on essentially zero budget.

### Growth

Because the project originated within the Dutch ISP community, the first participants were all Dutch network operators.
After giving our first public presentation at [RIPE62](https://ripe62.ripe.net/presentations/176-JobSnijders_NLNOG_RING_RIPE62.pdf) in May of 2011, ISPs from outside The Netherlands also showed interest in participating.
While The Netherlands is still the country with the most active participants (93 nodes as of January 2021), the majority of participants is based elsewhere.
At the time of writing we have 472 participating autonomous systems, with (virtual) machines in [56 countries](http://map.ring.nlnog.net/).

![Map of NLNOG RING nodes (January 2021)](/images/post/10-years-of-nlnog-ring/ring-map=january-2021.png "Map of NLNOG RING nodes (January 2021)")

Supporting all these machines was significantly increasing in load on our central Puppet server, to a point where in 2016 configuration of a single machine would take more than 30 minutes.
In addition to this we were facing the planned obsolescence of Puppet 2, which meant we would have to rewrite a significant part of our configurations to a syntax supported by Puppet 3.
Altogether a good opportunity to re-evaluate our architecture.

After evaluating several configuration management systems we decided on [Ansible](https://www.ansible.com/), mostly because of its support for a masterless “pull” model.
In this model all servers download their latest configs from a source code repository, and apply their changes locally.
This removes the need for a centralized management server, which means we can scale to a virtually unlimited number of machines.
All configuration files are published on our [GitHub repository](https://github.com/NLNOG/ring-ansible/), so that all participants can contribute.

To further cope with the increased growth in participants and machines we automated [health monitoring](https://ring.nlnog.net/toolbox/health-monitoring/), to automatically notify participants of problems with the (virtual) machines they provided to us.

### What’s next?

In ten years the NLNOG RING has grown from a handful of machines in the Netherlands to over 500 nodes worldwide, and we continue to see the number of active nodes grow.
To scale the platform further we plan to invest some time in building more self service tooling for provisioning of machines.
Another item high on our wishlist is a graphing solution that displays latency and packet loss on the full mesh of network paths between all nodes.
We will also continue to add features and tools [requested](https://github.com/NLNOG/ring-ansible/issues) by participants.

We of course hope to continue to see a diverse set of ISPs join the project. The success of the project largely depends on the networks that provide us with resources. We thank all [current participants](https://ring.nlnog.net/participants/) for making the NLNOG RING a huge success! Tell your friends to join too!

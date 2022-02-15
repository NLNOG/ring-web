+++
title = "Introduction"
aliases = ["about"]
+++

## Motivation

I’ve noticed that there are a lot of friendly ‘shell access’ exchange deals between network operators. This makes it easier for parties to debug network issues and troubleshoot ‘from the outside’. A point of view outside your network is absolutely essential, seeing what others see is a useful thing with a variety of network problems. Well known examples are ‘it works for even numbered ip address, but not for odd numbered ip address via this and this route’.

To encourage and provide a streamlined way of cooperating I introduce the “NLNOG RING”. In essence the deal is very simple: you make a (virtual) machine available to the RING, and you gain access on all servers which are part of the project, hence the name “RING”.

A great example would be to launch a traceroute from 80 servers in different networks and quickly get the results instead of waiting till somebody has the time to run some tests for you.

## Participation

Participation is open to everybody who meets the following requirements:

* You are a network operator
* The organisation you work for has BGP routers connected to the “Default Free Zone” and maybe even IXP’s.
* Your organisation has its own ASN and IP prefix(es).
* You have enable or configure rights on those routers.
* You are involved in the networkers community.
* You have permission from your organisation to become involved in the NLNOG RING.

## Applying for the RING

Admission to the project is discretionary and judged by perceived value for the RING as a whole. If your application is for an additional machine in a covered ASN, please contact us first.

***If you would like to join, please fill out the [application form](/contact/application-form).***

## Machine

The following requirements are mandatory:

* Clean Ubuntu 18.04 Bionic Beaver 64-bit (amd64/x86_64) Server Edition installation (no special packages are required except openssh-server)
* 64 bit CPU
* 1 globally reachable and unique statically configured **IPv6** address
* No packet filtering between your RING node and the internet
* You are willing to give full sudo access to the Ring-Admins (we will get to the security considerations later in this document)

You may choose to deploy the server directly on physical hardware or as a VM. We do not support (LXC) containers.

The following suggestions are indicative:

* 1 core or CPU
* 20 gigabyte disk space
* At least 1024 megabyte RAM, but more is better
* 10mbit NIC (more is fine)

Please decide for yourself what is appropiate; the machine will be a mere shell server managed by ansible.

## Management

All regular nodes (machines provided by organisations) are managed through a centralized ansible system. Ring-Admins will take care of software and security updates, installation and user management. The goal is to make it as easy as possible for organisations to provide a machine and not worry about it afterwards.

Machine owners are allowed and encouraged to install software which they deem necessary to comply with the standards of their organisation, examples are: n2, backup programs or a snmp daemon.

## Abuse

This RING is based on mutual trust: “you give me access I give you access”. We hope this model is strong enough to be viable. Abuse of the resources provided by the NLNOG RING is absolutely forbidden and we apply a ‘zero tolerance’ policy. This means that after one abuse incident you will be permantly banned from the RING. Through extensive logging and limitating the rights users have on other people’s systems we also hope to prevent abuse. For more information regarding the security of machines please see the [Security](/security) section of this website.

## Acknowledgements

A non-exhaustive list of people involved in the design and management of the NLNOG RING since its inception: Peter van Dijk, Teun Vink, Edwin Hermans, Martin Pels, Pieter Lexis, Matt Griswold and me.

If you have any questions please do not hesitate to contact us. Contact information can be found on the [Contact](/contact) page.

Kind regards,

Job Snijders


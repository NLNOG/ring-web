+++
title = "Security"
+++

This document describes the current NLNOG RING Security considerations.

## Access credentials
We will not use any passwords anywhere on the ring servers, this makes management easier and is more secure. Everything will be done through ssh-keys. In the [User Guide](/user-guide) you can find more information about how to sync your ssh-keys amongst all servers.

## Roles
**Regular users**: These users will have shell access to all servers in the Ring. They will have no sudo or root rights. They will not be allowed to do modifications to the systems and are not allowed to install packages. This group will be the main users of the Ring Servers. These users should be able to troubleshoot and debug with tools like mtr, traceroute, tcpdump and ping.

**Owners**: An owner is a useraccount who has donated a server to the ring. The owner has root/sudo access on their own machine and is allowed to make changes they see fit (hopefully without disrupting the functionality of the system ;-). Owners are expected to install software like vmware-tools, munin-node or n2. Also, they might make backups of their system with rsync. Owners do not have to take care of security updates, user management or the installation of software. This will be done from a central management system.

**Ring-Admins**: This is a small group of publicly known people whom the owners trust with sudo access on their systems. Ring-admins will manage the ring: installation and updating of software, creation of users and will be the first line of support in case of abuse tickets. Currently the ring-admins are Job Snijders, Martin Pels, Peter van Dijk, Sander Smeenk, Arjen Zonneveld and Teun Vink. Contact details can be found on the [Contact page](/contact).

## Machine roles
**Regular ring node**: This is a machine donated by an organisation. Regular users from all organisations in the ring can logon to these machines to perform tasks related to network troubleshooting. The owner of a node has full rights to his node, but not others.

**Master server**: These machines are a starting point for regular users to maintain their ssh keys, update contact information about their organisation. Ring-Admins manage the master servers.

**Log server**: This machine sole purpose is to receive logs from all servers related to the ring and securely store them. It will be publicly known who hosts a log server and who has access to it. These servers are managed by the Ring-Admins.

## Abuse
Abusing the trust other organisations give you is absolutly forbidden. We apply a ‘zero tolerance’ policy, which means that after the first incident you will be permantly banned from the project. If the Ring-Admins discover or are notified about an abuse incident they will contact the owners of the machine on which the abuse took place and fully disclose what happend and who was involved.

Furthermore we hope to prevent abuse by actively applying security updates as soon as they come out and not expose services except SSH to the outside world. Also keep in mind that regular users have no sudo rights.


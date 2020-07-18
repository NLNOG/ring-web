+++
title = "User Guide"
aliases = ["manual", "howto", "how-to-use"]
layout = "single"
+++

## Provisioning a server

First fill in the [Application Form](/contact/application-form).

Install Ubuntu in accordance with the requirements. The user that is created by the installation can be called `nlnog`. Please send the FQDN of the machine and the password (pgp encrypted) to one of the ring-admins. The ring-admin will provision the host and setup dns in the ring.nlnog.net zone. When installation is finished the nlnog user will be removed from the machine.

PGP & SSH Keys are available in the [Contact](/contact) section.

After you have been notified that the server has been added to the ring and is under control of our central configuration management, there are the following tasks you need to perform:

1. Login with your assigned username & the ssh-key you gave us
2. Add additional ssh keys to the `~/ssh-keys` file on `manage.ring.nlnog.net`. Within 30 to 60 minutes all the authorized_keys files will be updated based on your ssh-keys file. This way you can give co-workers access to the ring.

## Using the ring

Several utilities are available to you, see the [Available Software](/user-guide/software) section for a full list. If you need a package please email [ring-admins@nlnog.net](mailto:ring-admins@nlnog.net) with your request. Generally we only install packages available to a stock Ubuntu install.

* Never use passwords on the ring, only use ssh-keys.
* You can create your own key for the ring, or use a key that you use on a day-to-day basis. The former is preferred.
* There are some custom ring scripts available to you to execute commands on all or a subset of the servers. These scripts rely on your key. You can run them from your own machine or from one of the ring nodes (using it as a jumphost), if you want to do this then you should be using an [SSH Agent](http://en.wikipedia.org/wiki/Ssh-agent) to make your key available to this session; [ring-ssh](/toolbox/#ring-ssh) takes care of this for you.
* If you are using a custom key, the following SSH configuration should work for you:
  ```
  Host *.ring.nlnog.net
    User $you
    IdentityFile /home/$you/.ssh/nlnog.key
  ```
* To use your own ringnode as a jumphost to reach all other nodes, add:
  ```
  ProxyCommand ssh -W %h:%p $you@$IP_address_of_your_ringnode
  ```
* To run ring-commands from your local system, add:
  ```
  UserKnownHostsFile /home/$you/.ssh/known_hosts_ring
  ```
* And for easy retrieval of updates for this file, add the following to your .bashrc:
  ```
  alias ring_gethostsfile='scp $yournode:/etc/ssh/ssh_known_hosts ~/.ssh/known_hosts_ring'
  ```

* Do not use ForwardAgent when connecting to ring-nodes. Use `ring-ssh` instead.

## Overview of all ring servers
For a list of all ring servers you can use the following resources:

* [/participants/](/participants)
* `/etc/hosts` on every node
* `dig +short txt ring.nlnog.net`
* [/api/1.0/nodes](https://api.ring.nlnog.net/1.0/nodes)

## Ring scripts
Please visit the [Toolbox](/toolbox) section for a full overview of all scripts available to ring users.


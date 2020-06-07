+++
author = "Job Snijders"
title = "Upgrading the entire RING to Ubuntu 16.04 LTS"
date = "2017-04-04"
description = "Upgrading the entire RING to Ubuntu 16.04 LTS"
categories = [
    "announcement",
]
+++

Next week we're going to upgrade all Ubuntu 12.04 LTS (aka "Precise") hosts to Ubuntu 16.04 LTS (aka "Xenial"). This upgrade is necessary to ensure that all RING nodes receive timely security updates. An additional benefit is that we'll have more modern software.

> Do not ubuntu upgrade yourself, the RING admins will first attempt an upgrade.
> If possible, a RAM upgrade to at least 1GB would be appreciated.

### Timeline:

**Sun 09-04-2017T23:59Z - disable RING SQA on all nodes**

Since the upgrades require reboots & daemon restarts, and we can't exactly pace and predict when what happens, we don't want to risk sending people false RING SQA alerts dude to clusters of nodes being upgraded. The solution is that we will temporary disable RING SQA.

**Mon 10-04-2017 - launch ansible upgrade script on all nodes**

Martin Pels authored a really cool ansible [playbook](https://github.com/NLNOG/ring-ansible/blob/master/ubuntu_upgrade.yml) which facilitates the upgrade path (which actually is 12.04 -> 14.04 -> 16.04).

We'll disable all auxiliary services (scamper, ringfpingd, munin-node), run the playbook against all nodes, reboot them, and hope for the best!

**Wed 11-04-2017 - reach out to owners of nodes which didn't survive**

We expect that a number of nodes (for whatever reason) will not successfully upgrade to 16.04. Our management system will notify you if the upgrade was not succesful. In such cases we'll simply ask that you re-provision the node with Ubuntu 16.04 LTS and not bother trying to repair the upgrade.

**Thu 12-04-2017 - enable RING SQA on all nodes, celebrate**

Thursday most of the NLNOG RING should be back to normal, until next time in 2022 :-)

If you have any questions or concerns, let us know!


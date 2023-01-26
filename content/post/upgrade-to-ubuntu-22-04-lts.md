+++
author = "Martin Pels"
title = "Maintenance: Upgrade to Ubuntu 22.04 LTS"
date = "2023-01-26"
description = "Maintenance: Upgrade to Ubuntu 22.04 LTS"
categories = [
    "announcement",
]
+++

On February 7 2023 we will be upgrading all Ubuntu 18.04 LTS (aka "Bionic") RING nodes to Ubuntu 22.04 LTS (aka "Jammy"). This upgrade is necessary to ensure that all RING nodes receive timely security updates. An additional benefit is that we'll have more modern software.

> Note: Do not perform the Ubuntu upgrade yourself, the RING admins will first attempt an upgrade.

### Timeline

**2023-02-06 17:00 UTC: Disable RING SQA on all nodes**

By disabling SQA we make sure no excessive alerts are being sent while the nodes are being upgraded.

**2023-02-07 08:00 UTC: Configure upgrade playbook on all nodes**

Each node will be automatically upgraded to Ubuntu 20.04, rebooted, upgraded to Ubuntu 22.04 and rebooted again. We expect all nodes to complete this process around 11:00 UTC.

**2023-02-07 13:00 UTC: Reach out to owners of nodes which didn't survive**

We expect that a number of nodes (for whatever reason) will not successfully upgrade to 22.04. We will notify you if the upgrade was not succesful. In such cases we'll simply ask that you re-provision the node with Ubuntu 22.04 LTS and not bother trying to repair the upgrade.

**2023-02-08: Re-enable RING SQA, celebrate**

Thursday most of the NLNOG RING should be back to normal, until next time in 2027 :-)

If you have any questions or concerns, let us know!


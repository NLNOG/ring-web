+++
title = "Toolbox"
layout = "single"
+++

Below you can find several tools which make use of the ring setup. If you have written any tools and are willing to share them, or if you have great ideas for tools which are missing, please [contact](/contact) us!

## ring-all

This script allows you to run a command on all servers which participate in the NLNOG ring. `ring-all` can be found in `/usr/local/bin` on all ring servers. You can also download the script and the accompanying ruby module so it can be run from other machines.

**Usage:**

```
ring-all [command and arguments]
```
**Example:**

```
% ./ring-all dig +short -t SOA ring.nlnog.net
host: intouch01.ring.nlnog.net
ns1.6core.net. hostmaster.6core.net. 2011012601 14400 1800 2419200 300
host: zylon01.ring.nlnog.net
ns1.6core.net. hostmaster.6core.net. 2011012601 14400 1800 2419200 300
host: xlshosting01.ring.nlnog.net
ns1.6core.net. hostmaster.6core.net. 2011012601 14400 1800 2419200 300
(etc)
``` 

## ring-ping
This is a wrapper script for the ping tool which allows you to run ping commands from all servers. The script can calculate the average ping time or show ping times for each server in the ring. Of course, it supports both IPv4 and IPv6! `ring-ping` can be found in `/usr/local/bin` on all ring servers and can be downloaded here so it can be run from other machines.

**Usage:**

```
ring-ping [-6v] host
           -6    Use IPv6
           -v    Print RTT for each server
```
**Example:**

```
% ./ring-ping ripe.net
15 servers: 2ms average
```
```
% ./ring-ping -6 www.ipv6actnow.org
15 servers: 3ms average
```
```
% ./ring-ping -v www.isoc.nl
interconnect01:      2.161
widexs01:            1.053
coloclue01:          1.797
easyhosting01:       1.274
duocast01:           4.845
xlshosting01:        0.920
cambrium01:          1.164
intouch01:           1.514
bit01:               2.539
nxs01:               0.975
ic-hosting01:        1.721
xs4all01:            1.089
zylon01:             1.470
previder01:          2.792
leaseweb01:          2.464
15 servers: 1ms average
```

## graphite
A graphite setup has been created to graph latency between all nodes. Our graphite install can be found at [graphite.ring.nlnog.net](http://graphite.ring.nlnog.net/) (note: currently offline).

Graphite offers the possibility for creating your own graphs and dashboards. To create an account for your RING user, place a password in the file `~/graphite.pass` on `manage.ring.nlnog.net`. The graphite web login account will be automatically created within one hour.

## ring-trace
ring-trace is a tool which allows you to create graphs which visualise traceroutes from a number of ring sources.

**Usage:**
```
usage: ring-trace [-h] [-a | -c] [-b] [-B] [-e HOST] [-i HOST]
                  [-l {dot,neato,fdp,sfdp,twopi,circo}] [-n RANDOM]
                  [-o OUTFILE] [-p N] [-r] [-t {dot,gif,pdf,png,jpg,ps,svg}]
                  [-T TIMEOUT] [-u USER] [-U] [-v] [-vv] [-x | -X] [-4 | -6]
                  destination

positional arguments:
  destination           destination of the traces

optional arguments:
  -h, --help            show this help message and exit
  -a, --asn             group by ASN instead of IP
  -c, --show-country    show country codes for IP addresses
  -b, --pastebin        send output to a pastebin instead of saving it to file
  -B, --remove-broken-hops
                        remove broken hops from output image
  -e HOST, --exclude HOST
                        exclude a specific host
  -i HOST, --include HOST
                        include this host
  -l {dot,neato,fdp,sfdp,twopi,circo}, --layout {dot,neato,fdp,sfdp,twopi,circo}
                        layout style (dot by default)
  -n RANDOM, --random RANDOM
                        pick a given number of hosts at random
  -o OUTFILE, --output OUTFILE
                        output filename (trace-DESTINATION.type by default)
  -p N, --hops N        pick top N and bottom N hosts based on hopcount
  -r, --resolve         try to resolve all addresses (WARNING: can take long!)
  -t {dot,gif,pdf,png,jpg,ps,svg}, --type {dot,gif,pdf,png,jpg,ps,svg}
                        output filetype (jpg by default)
  -T TIMEOUT, --timeout TIMEOUT
                        SSH connection timeout in seconds (10 by default)
  -u USER, --user USER  username for SSH logins
  -U, --udp             use UDP instead of ICMP ECHO
  -v, --verbose         verbose mode
  -vv, --extra-verbose  extra verbose mode (SSH debugging)
  -x, --exclude-ixp     remove IXP hops from traces
  -X, --highlight-ixp-hops
                        highlight IXP hops in output
  -4, --ipv4            enforce IPv4
  -6, --ipv6            enforce IPv6
```
It’s usually a good idea to limit the number of hosts (using the `-n` flag) to improve the readability of the generated graph and reduce the runtime. Resolving all nodes usually is a bad idea, since it takes quite a long time. To make a graph more readable the `-a` flag can be used, which shows traces grouped by autonomous system and `-B` to remove all broken hops.

Since `ring-trace v1.4` it is possible to use a config file to set your own default values. The file should be named `.ringtrace.cfg` and should be in your homedirectory. Here’s a sample of a config file:

```
[Config]
# -a, --asn: group hops by ASN
GroupByASN=True
# -b, --pastebin: send output to a pastebin
Pastebin=False
# -B, --remove-broken: remove broken hops
RemoveBroken=False
# -e, --exclude: exclude hosts (comma separated)
ExcludeHosts=
# -i, --include: include hosts (comma separated)
IncludeHosts=bit01
# -l, --layout, select a different layout
# choices: dot,neato,fdp,sfdp,twopi,circo
Layout=dot
# -n, --random: the number of random nodes to query
UseNodes=2
# -o, --outfile: output filename
Filename=
# -r, --resolve: resolve all IPs and ASNs
Resolve=False
# -t, --type: output filetype (gif, pdf, png, ps, svg)
FileType=png
# -T, --timeout
SSHTimeout=10
# -U, --udp: use UDP instead of ICMP
UDP=False
# -v, --verbose, -vv, --extra-verbose: set verbosity level
Verbose=1
# -x, --exclude-ixp: exclude IXP hops
ExcludeIXP=True
# -X, --highlight-ixp-hops, highlight all IXP hops
HighlightIXPHops=False
# -4, --ipv4: force IPv4
IPv4=False
# -6, --ipv6: force IPv6
IPv6=False
```
`ring-trace` can be found on all ring nodes. With pastebin option (`-b`) it is possible to automatically upload the generated graph to a pastebin. You can also run ring-trace on your local machine if you have a SSH-agent running locally. The code can be downloaded [here](https://github.com/NLNOG/nlnog-ring/raw/master/scripts/ring-trace). Feature requests, bugs and ideas are always welcome, preferably via the [Github issue tracker](https://github.com/NLNOG/nlnog-ring/issues).

## ring-curl
`ring-curl` is a wrapper around the `libcurl` API and `ring-all`. It can be used to run HTTP requests on multiple RING nodes. This is particularly useful for debugging CDN problems.

**Usage:**

```
ring-curl [options] <url>

Options:
  --user-agent <string>         User-agent
  --request-header <header>     Add request header
  --request-type <GET|POST>     Request type
  --post-data <string>          Data for POST request

  --headers                     Print all headers
  --header <header>             Print specific header
  --body                        Print page body
  --md5                         Print md5sum of page body
  --curlinfo                    Print curl variable
  --curl-param <variable>       Print specific curl variable
  --all                         Print all data

  --output <txt|json|perl>      Output format
  --local                       Only run on local RING node
  --ring-opts <string>          Argument string to pass to 'ring-all'
  --help                        Display this message
```
**Example:**

```
% ring-curl --header CDN-Node --curl-param local_ip --curl-param http_code http://www.leaseweb.com/ | grep -e ": "
* Executed on behalf of: martin
* Date: 2016-01-29 14:41:31 (UTC)
* Executed on: 50 nodes; 9 nodes timed out or were unreachable
    CDN-Node: WDC1-EDGE02013
    local_ip: 187.72.248.26
    http_code: 301
    CDN-Node: FRA1-EDGE03013
    local_ip: 77.246.27.26
    http_code: 301
    CDN-Node: SIN1-EDGE05001
    local_ip: 172.31.0.100
    http_code: 301
    CDN-Node: SV1-EDGE04012
    local_ip: 174.136.100.234
    http_code: 301
    CDN-Node: WDC1-EDGE02013
    local_ip: 108.60.128.14
    http_code: 301
    CDN-Node: AMS1-EDGE01013
    local_ip: 195.178.185.171
    http_code: 301
    CDN-Node: AMS1-EDGE01012
    local_ip: 46.183.250.9
    http_code: 301
    CDN-Node: AMS1-EDGE01012
    local_ip: 77.244.137.180
    http_code: 301
    CDN-Node: FRA1-EDGE03013
    local_ip: 195.22.19.34
    http_code: 301

    [...]
```

## ring-ssh
The use of SSH Agent forwarding poses a security risk, in that it forwards all identities in your agent to the remote system. Individuals with root access on the remote system may take over your agent’s socket and use it to login on other systems. `ring-ssh` mitigates this risk by creating a separate `ssh-agent` instance containing only your ring-identity, and forwarding this agent to the remote system. The script can be downloaded [here](https://github.com/NLNOG/nlnog-ring/raw/master/scripts/ring-ssh).

**Usage:**

```
   ring-ssh [arguments and host]
```
**Example:**

```
% ring-ssh coloclue01.ring.nlnog.net
```

#!/usr/bin/python3

import cgi, cgitb
import getpass
import html
import smtplib
import socket
from string import Template

# E-mail templates
ADMINADDR='martin@rodecker.nl'
APPLICATIONMAIL = '''From: $contact <$email>
To: NLNOG RING Admins <$adminmail>
Subject: RING Application from $company - $autnum

General info:
=============

Company: $company
Website: $url
NOC: $nocemail
Company description: $companydesc

Applicant: $contact
Applicant email: $email
Heard about RING: $hear_about

Remarks:
$remarks

SSH Keys:
$sshkeys

NODE:
=====

User: nlnog
Pass: $password 
ASN: $autnum
IPv6: $ipv6
IPv4: $ipv4
Geo: $geo
Datacenter: $dc

Command templates:
==============

ring-admin add participant "$company" "$contact" $email $nocemail $$username "$companydesc" $url

ring-admin add machine $$username $$hostname $autnum $countrycode $geo "$dc" $ipv6 $ipv4 $statecode 

--
This mail was sent via a contact form on NLNOG RING https://ring.nlnog.net/
'''
CONFIRMATIONMAIL = '''From: NLNOG RING Admins <$adminmail>
To: $contact <$email>
Subject: RING Application from $company - $autnum

Dear $contact,

Thank you for your interest in the NLNOG RING. Your application has been received and will be processed shortly.

Kind regards,

NLNOG RING Admins
E: ring-admins@nlnog.net
W: http://ring.nlnog.net/

--
This mail was sent via a contact form on NLNOG RING https://ring.nlnog.net/
'''

# Get data
form = cgi.FieldStorage() 

company = None
if form.getvalue('company'):
    company = html.escape(form.getvalue('company'),quote=True)
companydesc = None
if form.getvalue('companydesc'):
    companydesc = html.escape(form.getvalue('companydesc'),quote=True)
url = None
if form.getvalue('url'):
    url = html.escape(form.getvalue('url'),quote=True)
logo = None
if form.getvalue('logo'):
    logo = form.getvalue('logo')
contact = None
if form.getvalue('contact'):
    contact = html.escape(form.getvalue('contact'),quote=True)
email = None
if form.getvalue('email'):
    email = html.escape(form.getvalue('email'),quote=True)
nocemail = None
if form.getvalue('nocemail'):
    nocemail = html.escape(form.getvalue('nocemail'),quote=True)
sshkeys = None
if form.getvalue('sshkeys'):
    sshkeys = html.escape(form.getvalue('sshkeys'),quote=True)

autnum = None
if form.getvalue('autnum'):
    autnum = html.escape(form.getvalue('autnum'),quote=True)
ipv6 = None
if form.getvalue('ipv6'):
    ipv6 = html.escape(form.getvalue('ipv6'),quote=True)
ipv4 = None
if form.getvalue('ipv4'):
    ipv4 = html.escape(form.getvalue('ipv4'),quote=True)
countrycode = None
if form.getvalue('countrycode'):
    countrycode = html.escape(form.getvalue('countrycode'),quote=True)
statecode = None
if form.getvalue('statecode'):
    statecode = html.escape(form.getvalue('statecode'),quote=True)
geo = None
if form.getvalue('geo'):
    geo = html.escape(form.getvalue('geo'),quote=True)
dc = None
if form.getvalue('dc'):
    dc = html.escape(form.getvalue('dc'),quote=True)
username = None
if form.getvalue('username'):
    username = html.escape(form.getvalue('username'),quote=True)
password = None
if form.getvalue('password'):
    password = html.escape(form.getvalue('password'),quote=True)

hear_about = None
if form.getvalue('hear_about'):
    hear_about = html.escape(form.getvalue('hear_about'),quote=True)
remarks = None
if form.getvalue('remarks'):
    remarks = html.escape(form.getvalue('remarks'),quote=True)

ttext = Template(APPLICATIONMAIL)
appformbody = ttext.substitute(company=company,
                               companydesc=companydesc,
                               url=url,
                               contact=contact,
                               email=email,
                               nocemail=nocemail,
                               sshkeys=sshkeys,
                               autnum=autnum,
                               ipv6=ipv6,
                               ipv4=ipv4,
                               countrycode=countrycode,
                               statecode=statecode,
                               geo=geo,
                               dc=dc,
                               username=username,
                               password=password,
                               hear_about=hear_about,
                               remarks=remarks,
                               adminmail=ADMINADDR)
ttext = Template(CONFIRMATIONMAIL)
confirmbody = ttext.substitute(company=company,
                               contact=contact,
                               email=email,
                               autnum=autnum,
                               adminmail=ADMINADDR)

# Send mails
sender = getpass.getuser() + '@' + socket.getfqdn()
server = smtplib.SMTP('localhost')
## Application mail
server.sendmail(sender,ADMINADDR,appformbody)
## Confirmation mail
server.sendmail(sender,email,confirmbody)
server.quit()

print('Content-type:text/html\r\n\r\n')
print('<html>')
print('<head>')
print('<title>NLNOG RING</title>')
print('<meta http-equiv="refresh" content="0; url=/contact/application-submitted/">')
print('</head>')
print('<body>')
print('<p>Application submitted. Redirecting...</p>')
print('</body>')
print('</html>')

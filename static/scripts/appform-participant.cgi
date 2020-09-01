#!/usr/bin/python3

import cgi, cgitb
import getpass
import html
import email, smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import socket
from string import Template

# E-mail templates
ADMINADDR='ring-admins@nlnog.net'
APPLICATIONMAIL = '''General info:
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

User: $username
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
CONFIRMATIONMAIL = '''Dear $contact,

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

company = ""
if form.getvalue('company'):
    company = html.escape(form.getvalue('company'),quote=True)
companydesc = ""
if form.getvalue('companydesc'):
    companydesc = html.escape(form.getvalue('companydesc'),quote=True)
url = ""
if form.getvalue('url'):
    url = html.escape(form.getvalue('url'),quote=True)
logo = form['logo']
contact = ""
if form.getvalue('contact'):
    contact = html.escape(form.getvalue('contact'),quote=True)
email = ""
if form.getvalue('email'):
    email = html.escape(form.getvalue('email'),quote=True)
nocemail = ""
if form.getvalue('nocemail'):
    nocemail = html.escape(form.getvalue('nocemail'),quote=True)
sshkeys = ""
if form.getvalue('sshkeys'):
    sshkeys = html.escape(form.getvalue('sshkeys'),quote=True)

autnum = ""
if form.getvalue('autnum'):
    autnum = html.escape(form.getvalue('autnum'),quote=True)
ipv6 = ""
if form.getvalue('ipv6'):
    ipv6 = html.escape(form.getvalue('ipv6'),quote=True)
ipv4 = ""
if form.getvalue('ipv4'):
    ipv4 = html.escape(form.getvalue('ipv4'),quote=True)
countrycode = ""
if form.getvalue('countrycode'):
    countrycode = html.escape(form.getvalue('countrycode'),quote=True)
statecode = ""
if form.getvalue('statecode'):
    statecode = html.escape(form.getvalue('statecode'),quote=True)
geo = ""
if form.getvalue('geo'):
    geo = html.escape(form.getvalue('geo'),quote=True)
dc = ""
if form.getvalue('dc'):
    dc = html.escape(form.getvalue('dc'),quote=True)
username = ""
if form.getvalue('username'):
    username = html.escape(form.getvalue('username'),quote=True)
password = ""
if form.getvalue('password'):
    password = html.escape(form.getvalue('password'),quote=True)

hear_about = ""
if form.getvalue('hear_about'):
    hear_about = html.escape(form.getvalue('hear_about'),quote=True)
remarks = ""
if form.getvalue('remarks'):
    remarks = html.escape(form.getvalue('remarks'),quote=True)
bits = ""
if form.getvalue('bits'):
    bits = html.escape(form.getvalue('bits'),quote=True)

if bits != "128":
    print('Content-type:text/html\r\n\r\n')
    print('<html>')
    print('<head>')
    print('<title>NLNOG RING</title>')
    print('</head>')
    print('<body>')
    print('<p>Wrong answer. Please go back and try again.</p>')
    print('</body>')
    print('</html>')
else:
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
                                   remarks=remarks)
    ttext = Template(CONFIRMATIONMAIL)
    confirmbody = ttext.substitute(contact=contact)

    # Send mails
    sender = getpass.getuser() + '@' + socket.getfqdn()
    server = smtplib.SMTP('localhost')

    ## Application mail
    message = MIMEMultipart()
    message['From'] = "%s <%s>" % (contact,email)
    message['To'] = "NLNOG RING Admins <%s>" % (ADMINADDR)
    message['Subject'] = "RING Application from %s - %s" % (company,autnum)
    message.attach(MIMEText(appformbody, "plain"))
    if logo != None:
        logo_name = os.path.basename(logo.filename)
        attachment = MIMEBase("application", "octet-stream")
        attachment.set_payload(logo.file.read())
        encoders.encode_base64(attachment)
        attachment.add_header(
            "Content-Disposition",
            "attachment; filename="+logo_name,
        )
        message.attach(attachment)
    text = message.as_string()
    server.sendmail(sender,ADMINADDR,text)

    ## Confirmation mail
    message = MIMEMultipart()
    message['From'] = "NLNOG RING Admins <%s>" % (ADMINADDR)
    message['To'] = "%s <%s>" % (contact,email)
    message['Subject'] = "RING Application from %s - %s" % (company,autnum)
    message.attach(MIMEText(confirmbody, "plain"))
    text = message.as_string()
    server.sendmail(sender,email,text)
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

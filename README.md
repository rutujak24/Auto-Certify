# Automatic-Certificate-generator-and-sender-python

Ever imagined that the python program can send emails automatically on just a single click of yours? Well, Python being a 
vast and diversified programming language makes this possible. This concept is known as email automation or email processing 
with python. 

Python supports the email package library for managing emails. This email package can read write and send emails. 
These emails can be simple like text message and can also be complex like MIME messages. For email processing with python,
we need to import some libraries. Firstly SMTP (Simple Mail Transfer Protocol) Client has to be imported.
<pre>
import smtplib
</pre>

Having understood basic structure and general implementation of email processing with python for simple text emails, 
now we can move forward and deal with the MIME messages in automation of emails. For complex MIME messages we need to 
import the MIME library, as follows:
<pre>
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
</pre>

This project creates certificates from a template for all participants in excel sheet and sends them via email, also creates a folder which stores the send email certificates.

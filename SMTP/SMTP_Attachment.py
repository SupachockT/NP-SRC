import sys
import json
from smtplib import *
from getpass import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def SMTP_Server(smtp_domain, smtp_port):
    try:
        server = SMTP(smtp_domain, smtp_port)
        server.starttls()
        print('SMTP connection successful')
        return server
    except:
        print('Error: could not connect to SMTP server')
        smtp_domain = input('please input SMTP domain name: ')
        smtp_port = input('please input SMTP port: ')
        return SMTP_Server(smtp_domain, smtp_port)

def GET_Account(file_name):
    try:
        with open(file_name, 'r') as json_file:
            data_dict = json.load(json_file)
    except:
        print('error occur during reading file')
        sys.exit()
    else:
        return data_dict

def SMTP_Login(server, sender_email, password):
    try:
        server.login(sender_email, password)
        print('Login successful...')
        return sender_email, password
    except SMTPException as e:
        print('Failed to login. Error:', e)
        sender_email = input('Please input your email: ')
        password = getpass('Please input your password: ')
        # Recursive call to SMTP_Login
        return SMTP_Login(server, sender_email, password)

def Text_Attachment(server, sender_email, file_name):
    receiver_email = input('please input your receiver email address: ')
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = input('Please input mail subject: ')
    email_message = input('Please input message: ')
    body = email_message
    msg.attach(MIMEText(body, 'plain'))

    attachment = open(file_name, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename = %s' % file_name)
    msg.attach(part)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

server = SMTP_Server(smtp_domain='smtp.gmail.com', smtp_port=587)
sender, password, receiver = GET_Account('SMTP_Account.json').values()
sender, password = SMTP_Login(server=server, sender_email=sender, password=password)
Text_Attachment(server, sender, 'AttachmentFile.txt')
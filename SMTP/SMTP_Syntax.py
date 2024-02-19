import smtplib

#smtplid.SMTP take 2 parameters (host, port)
server = smtplib.SMTP(host='smtp.gmail.com', port=587)
server.starttls() #TLS(Transport layer security)

#s servers can require authentication for sending emails.
server.login('ampandj@gmail.com', 'kqkh foul cowo hgel')

msg = 'Hello, I am from SMTP.'
msgHTML = """From: From Person <ampandj@gmail.com>
To: To Person <ampandj@gmail.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""

try:
    #(sender email) (recieve email) (message)
    server.sendmail('ampandj@gmail.com', 'ampandj@gmail.com', msgHTML)
    print('Email sent successfully!')
except smtplib.SMTPException as e:
    print(f'Error: unable to send email. {e}')
finally:
    server.quit()


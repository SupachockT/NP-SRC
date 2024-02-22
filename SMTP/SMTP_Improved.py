import smtplib
import sys
import json

def GET_Account():
    try:
        with open('SMTP_Account.json', 'r') as json_file:
            data_dict = json.load(json_file)
    except:
        print('error occur during reading file')
        sys.exit()
    else:
        return data_dict

account, password, receiver = GET_Account().values()
print('read file succesfully:', account, password, receiver)

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    print('Connect to server succesfully.')
    try:
        server.login(account, password)
        msg = 'This is message from the future me'
        server.sendmail(account, receiver, msg)
        print('Send mail succesfully.')
    except:
        print('Incorrect account or password.')
    finally:
        server.quit()
except:
    print('No SMTP service found.')
    
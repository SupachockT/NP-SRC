from ftplib import FTP
from FTP_Function import *

#username = client_test, password = 123456
ftp = FTP('127.0.0.1')

ftp.login(user='client_test', passwd='123456')

print("Welcome to the FTP client!")
print("Available commands:")
print("1 - List files in current directory")
print("2 - Download a file")
print("3 - Upload a file")
print("4 - Change directory")
print("5 - get current directory")
print("0 - Exit")

while True:
    cmd = int(input('Please enter a number: '))

    if(cmd == 1): 
        ftp.retrlines('LIST')
    elif(cmd == 2):
        file = input('to download file: ')
        DownloadFile(ftp, file)
    elif(cmd == 3):
        file = input('to upload file: ')
        UploadFile(ftp, file)
    elif(cmd == 4):
        directory = (input('directory to change: '))
        ChangeDir(ftp, directory)
    elif(cmd == 5):
        ShowDir(ftp)
    elif(cmd == 0): 
        ftp.close()
    else: 
        break
print('you exit the loop!')
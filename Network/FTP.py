from ftplib import FTP

def UploadFile(filename):
    ftp.storbinary('STOR ' + filename, open(filename,'rb') )

def DownloadFile(filename):
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    localfile.close()

def CreateDirectory(directory_name):
    ftp.mkd(directory_name)
    
def DeleteDirectory(directory_name):
    ftp.rmd(directory_name)
    
def ChangeDirectory(directory_name):
    ftp.cwd(directory_name)

def LookDirectory():
    print(ftp.pwd())

directory_name = '6430300978'
ftp = FTP('10.64.160.5')

ftp.login(user='st03603423', passwd='st03603423')

ftp.mkd(directory_name)
ftp.cwd(directory_name)
UploadFile('ReportGrade.txt')
ftp.retrlines('LIST')
ftp.quit()

'''
print("Welcome to the FTP client!")
print("Available commands:")
print("1 - List files in current directory")
print("2 - Download a file")
print("3 - Upload a file")
print("4 - Change directory")
print("5 - Where am i")
print("0 - Exit")

while True:
    cmd = int(input('Please enter a number: '))
    if(cmd == 1): 
        ftp.retrlines('LIST')
    elif(cmd == 2):
        file = input('to download file: ')
        DownloadFile(file)
        print('process download...')
    elif(cmd == 3):
        UploadFile(file)
        print('process upload...')
    elif(cmd == 4):
        ChangeDirectory(directory_name)
        print('change directory...')
    elif(cmd == 5):
        LookDirectory()
    elif(cmd == 0): 
        ftp.close()
    else: 
        break
print('you exit the loop!')
'''
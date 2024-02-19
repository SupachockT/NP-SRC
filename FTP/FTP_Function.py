#function for FTP Client Passive Mode

def UploadFile(ftp_server, file_name):
    try:
        ftp_server.storbinary('STOR ' + file_name, open(file_name,'rb') )
    except:
        print('you do not have file in your direcotry.')
    else:
        print('process download...')

def DownloadFile(ftp_server, file_name):
    try:
        localFile = open(file_name, 'wb')
        ftp_server.retrbinary('RETR ' + file_name, localFile.write, 1024)
        localFile.close()
    except:
        print('server do not have that file ready.')
    else:
        print('process download...')

def MakeDir(ftp_server, directory_name):
    ftp_server.mkd(directory_name)

def DelDir(ftp_server, directory_name):
    ftp_server.rmd(directory_name)

def ChangeDir(ftp_server, directory_name):
    try:
        ftp_server.cwd(directory_name)
    except:
        print('No directory.')
    else:
        print('change directory...')

def ShowDir(ftp_server):
    print(ftp_server.pwd())

def IsDirExist(ftp_server, directory_name):
    try:
        ftp_server.cwd(directory_name)
        return True
    except:
        ftp_server.mkd(directory_name)
        return False
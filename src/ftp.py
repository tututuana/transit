from ftplib import FTP


def connect(server, username='anonymous', password=''):
    global ftp
    ftp = FTP(server)
    ftp.login(username, password)
    
    welcome = ftp.getwelcome()
    files = ftp.nlst()

    return(files)

def welcome():
    welcome = ftp.getwelcome()
    return(welcome)

def ls():
    files = ftp.nlst()

    return(files)

def cd(dir):
    ftp.cwd(dir)
    
    return(ls())

def bye():
    ftp.quit()

def download(filename):
    with open(str(filename), 'wb') as fp:
        ftp.retrbinary('RETR ' + str(filename), fp.write)
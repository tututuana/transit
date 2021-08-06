from ftplib import FTP

def connect(server, port=22, username='anonymous', password=''):
    global ftp
    ftp = FTP(server)
    ftp.login(username, password)
    
    welcome = ftp.getwelcome()
    files = ftp.nlst()

    return(files)

def cd(dir):
    ftp.cwd(dir)
    files = ftp.nlst()

    return(files)
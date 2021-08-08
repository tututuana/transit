'''
Transit CLI (Version 0.1)
MIT License
'''

import ftp, sys, getpass, time, ftplib
from rich import print

def ls():
    for item in ftp.ls():
        if len(str(item).split('.png')) > 1:
            print('[red] :sparkles: ' + item + '[/red]', end='  ')
        
        elif len(str(item).split('.py')) > 1:
            print('[red] :snake: ' + item + '[/red]', end='  ')
        
        elif len(str(item).split('.')) > 1:
            print('[red] :page_facing_up: ' + item + '[/red]', end='  ')
        
        else:
            print('[blue] :file_folder: ' + item + '[/blue]', end='  ')
    print()

def cd(dir):
    try:
        ftp.cd(dir=dir)
        ls()
    except ftplib.error_perm:
        print(':warning: Couldn\'t find path.')

def download(filename):
    print(':arrow_down_small: Downloading...', end='\r')
    ftp.download(filename=filename)
    print(':heavy_check_mark: Done!         ', end='\r')
    print()
#########################################################
server = 'test.rebex.net' #input('Server: ')

print(':wave: ', end='')
username = input('Username: ')
print(':lock: ', end='')
password = getpass.getpass('Password: ')

try:
    ftp.connect(server=server, username=username, password=password)
except:
    print(':x: Couldn\'t connect.')
    sys.exit()

print(':heavy_check_mark: Connected to the server.')
time.sleep(0.5)
print()

while True:
    cmd = input('→ ')
    cmd = cmd.lower()

    if cmd.startswith('cd') or cmd.startswith('chdir'):
        cd(cmd.split(' ')[1])
    
    elif cmd.startswith('ls') or cmd.startswith('dir'):
        ls()

    elif cmd.startswith('exit') or cmd.startswith('bye'):
        print(':wave: Good bye!')
        try:
            ftp.bye()
        except:
            pass
        sys.exit()
    
    elif cmd.startswith('download') or cmd.startswith('get'):
        download(cmd.split(' ')[1])
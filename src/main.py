from systemINFO import systemINFO
import ftp

serverType = 'FTP'
server = 'test.rebex.net'

ftp.connect(server=server, username='demo', password='password')
print(ftp.welcome())
print(ftp.ls())
ftp.download('readme.txt')
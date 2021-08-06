from systemINFO import systemINFO
import ftp

serverType = 'FTP'
server = 'test.rebex.net'
port = 22

ftp.connect(server=server, port=port, username='demo', password='password')
print(ftp.cd('pub'))
import os, platform, socket, getpass

systemINFO = {
    'os' : {
        'name': str(os.name), 
        'type': str(platform.system()),
        'version': str(platform.release())
    },
    'hardware' : {
        'cpu': str(platform.processor())
    },
    'network': {
        'node': str(platform.node()),
        'ip': str(socket.gethostname()),
        'user': str(getpass.getuser())
    }
}
import random, sys, ftp
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton,
                               QVBoxLayout, QWidget)
from __feature__ import snake_case, true_property

# Connect to a FTP server
server = 'test.rebex.net'
username = 'demo'
password = 'password'
ftp.connect(server=server, username=username, password=password)

class mainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QVBoxLayout(self)

        # Connecting the signal
        for i in ftp.ls():
            self.button = QPushButton(i)
            self.layout.add_widget(self.button)

            
            download = lambda fileName: ftp.download(i)
            self.button.clicked.connect(download)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = mainWindow()
    widget.show()

    sys.exit(app.exec_())
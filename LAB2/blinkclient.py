from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QApplication, QPushButton
from PyQt5.QtCore import QSize    
from morsecodefunc import morseconvert
import socket

class Windowmaker(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(550, 140))    
        self.setWindowTitle("Blinker") 

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Hz:')
        self.nameLabel.move(20, 20)

        self.line2 = QLineEdit(self)
        self.line2.move(120, 20)
        self.line2.resize(400, 37)

        mybutton = QPushButton('Send to pi', self)
        mybutton.clicked.connect(self.clickMethod)
        mybutton.resize(400,32)
        mybutton.move(120, 80)        

    def clickMethod(self):
        text="b"+self.line2.text()
        self.line2.clear()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            host = "192.168.1.124"
            port = 8001
            s.connect((host,port))
            s.sendall(bytes(text,"utf-8"))

if __name__ == "__main__":

    app = QApplication(["Morsecode"])
    Window = Windowmaker()
    Window.show()
    app.exec_()

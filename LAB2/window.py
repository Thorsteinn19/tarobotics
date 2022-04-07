from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QApplication, QPushButton
from PyQt5.QtCore import QSize    

class Windowmaker(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(550, 140))    
        self.setWindowTitle("Namebox") 

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Name:')
        self.nameLabel.move(20, 20)

        self.line = QLineEdit(self)
        self.line.move(120, 20)
        self.line.resize(400, 32)


        mybutton = QPushButton('Print', self)
        mybutton.clicked.connect(self.clickMethod)
        mybutton.resize(400,32)
        mybutton.move(120, 60)        

    def clickMethod(self):
        print(self.line.text())
        self.close()

if __name__ == "__main__":
    app = QApplication(["Name window"])
    Window = Windowmaker()
    Window.show()
    app.exec_()
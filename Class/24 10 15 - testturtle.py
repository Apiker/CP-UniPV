import turtle
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Giovanni Orlotti - Essay 1")
        self.setWindowIcon(QIcon('assets/icon.ico'))
        self.setMinimumWidth(600)
        self.w = None

        self.sides = 0

        #First Column
        box1 = QGroupBox("Draw a shape")

        self.selectlabel = QLabel("Select your shape: ")
        self.selectionmenu = QComboBox()
        self.selectionmenu.setEditable(False)
        self.selectionmenu.addItems(["Circle", "Polygon"])
        self.selectionmenu.currentTextChanged.connect(self.updatecombobox)

        self.polygonbox = QComboBox()
        self.polygonbox.hide()
        self.polygonbox.setEditable(True)
        self.polygonbox.addItems(["3", "4", "5", "6", "7", "8"])        

        self.drawbutton = QPushButton("Draw")
        self.drawbutton.clicked.connect(self.draw)



        # ///Layout///
        centerwidget = QWidget()

        imagelayout = QVBoxLayout(centerwidget)
        groupboxlayout = QHBoxLayout()

        box1layout = QVBoxLayout()
        
        box1layout.addWidget(self.selectlabel)
        box1layout.addWidget(self.selectionmenu)
        box1layout.addWidget(self.polygonbox)

        box1.setLayout(box1layout)
        groupboxlayout.addWidget(box1)
        

        imagelayout.addLayout(groupboxlayout)
        imagelayout.addWidget(self.drawbutton)

        self.setCentralWidget(centerwidget)


    def updatecombobox(self, text):
        if text == "Circle":
            self.polygonbox.hide()
        elif text == "Polygon":
            self.polygonbox.show()
    
    def draw(self):
        selection = self.selectionmenu.currentText()
        if selection == "Circle":
            self.drawcircle()
        elif selection =="Polygon":
            self.drawpoly()
    
    def drawcircle(self):
        bob = turtle.Turtle()
        bob.circle(50)
    
    def drawpoly(self):
        bob = turtle.Turtle()
        sides = int(self.polygonbox.currentText())
        for _ in range(sides): 
            turtle.forward(20) 
            turtle.right(360 / sides)


app = QApplication(sys.argv)

window = Application()
window.show()
app.exec()

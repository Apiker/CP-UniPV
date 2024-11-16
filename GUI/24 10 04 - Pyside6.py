from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys

class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTabWidget")
        self.setWindowIcon(QIcon('assets/simplemanager.ico'))
        self.setMinimumWidth(451)
        self.w = None

        # --Menu bar--
        menu = self.menuBar()

        file = menu.addMenu("File")
        file.addAction("Test")
        file.addAction("Test")
        close = file.addAction("Close")
        close.triggered.connect(self.quit)

        edit = menu.addMenu("Edit")
        edit.addAction("Copy")
        edit.addAction("Paste")
        edit.addAction("Cut")
        edit.addAction("Undo")
        edit.addAction("Redo")

        user = menu.addMenu("User")
        user.addAction("Profile")
        user.addAction("Log Out")

        # --Toolbar--
        toolbar = QToolBar("Toolbar")
        toolbar.setIconSize(QSize(16,16))
        toolbar.setMovable(False)
        self.addToolBar(Qt.LeftToolBarArea, toolbar)

        self.color = QPushButton()
        self.color.setIcon(QIcon('assets/impostazioni.png'))
        self.color.setCheckable(True)
        self.color.setStatusTip("Color settings")
        self.color.toggled.connect(self.changecolor)
        toolbar.addWidget(self.color)
        
        toolbar.addSeparator()

        hide = QAction(self)
        hide.setStatusTip("Hide controls")
        hide.setIcon(QIcon('assets/chiudi.png'))
        hide.triggered.connect(self.hideactiontoolbar)
        toolbar.addAction(hide)

        show = QAction(self)
        show.setStatusTip("Show controls")
        show.setIcon(QIcon('assets/done.png'))
        show.triggered.connect(self.showactiontoolbar)
        toolbar.addAction(show)

        # --Status bar--
        self.setStatusBar(QStatusBar(self))


        # --Central Window--

        # --TabWidget--
        tabwidget = QTabWidget()

        # --FIRST TAB--
        # --First Row--
        self.label = QLabel("Insert value: ")
        self.lineedit = QLineEdit()
        self.lineedit.editingFinished.connect(self.setvalue)
        self.sendbutton = QPushButton("Set")
        self.sendbutton.clicked.connect(self.setvalue)

        # --Second Row--
        self.minlabel = QLabel("0")
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(255)
        self.slider.valueChanged.connect(self.sliderposition)
        self.maxlabel = QLabel("255")

        # --Third Row--
        self.label2 = QLabel("Slidebar value: ")
        self.valuelabel = QLabel("0")

        # --Fourth Row--
        self.button = QPushButton("Set value to min")
        self.button.clicked.connect(self.buttonpressed)
        self.button2 = QPushButton("Set value to max")
        self.button2.clicked.connect(self.button2pressed)
        self.specialbutton = QPushButton("Hide slidebar")
        self.specialbutton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        self.specialbutton.pressed.connect(self.pressedfunction)
        self.specialbutton.released.connect(self.releasedfunction)
        self.hidebutton = QPushButton("Hide controls")
        self.button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        self.button2.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        self.hidebutton.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        self.hidebutton.setCheckable(True)
        self.hidebutton.toggled.connect(self.hidecommands)

        # --Fifth Row--
        # --Non exclusive Checkbox - Fifth Row, Column 1--
        box1 = QGroupBox("Choose one or more")
        windows = QCheckBox("Windows")
        linux = QCheckBox("Linux")
        macos = QCheckBox("MacOs")
        android = QCheckBox("Android")
        ios = QCheckBox("iOS")

        oslayout = QVBoxLayout()
        oslayout.addWidget(windows)
        oslayout.addWidget(linux)
        oslayout.addWidget(macos)
        oslayout.addWidget(android)
        oslayout.addWidget(ios)
        box1.setLayout(oslayout)

        # -- Exclusive Checkbox - Fifth Row, Column 2--
        box2 = QGroupBox("Choose one")
        corona = QCheckBox("Corona")
        ichnusa = QCheckBox("Ichnusa")
        moretti = QCheckBox("Moretti")
        peroni = QCheckBox("Peroni")
        heineken = QCheckBox("Heineken")
        
        exclusive_button_group = QButtonGroup(self)
        exclusive_button_group.addButton(corona)
        exclusive_button_group.addButton(ichnusa)
        exclusive_button_group.addButton(moretti)
        exclusive_button_group.addButton(peroni)
        exclusive_button_group.addButton(heineken)

        beerlayout = QVBoxLayout()
        beerlayout.addWidget(corona)
        beerlayout.addWidget(ichnusa)
        beerlayout.addWidget(moretti)
        beerlayout.addWidget(peroni)
        beerlayout.addWidget(heineken)
        box2.setLayout(beerlayout)

        # --Sixth Row--
        # -- Radio Buttons --
        answers = QGroupBox("Choose an answer")
        answer1 = QRadioButton("Answer 1")
        answer2 = QRadioButton("Answer 2")
        answer3 = QRadioButton("Answer 3")

        answerslayout = QVBoxLayout()
        answerslayout.addWidget(answer1)
        answerslayout.addWidget(answer2)
        answerslayout.addWidget(answer3)
        answers.setLayout(answerslayout)

        # --SECOND TAB--
        # --QListWidget --
        global listwidget
        listwidget = QListWidget()
        listwidget.addItems(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

        add = QPushButton("Add")
        add.clicked.connect(self.addItem)
        remove = QPushButton("Remove")
        remove.clicked.connect(self.removeItem)
        multi = QPushButton("Select multiple items")
        multi.setCheckable(True)
        multi.toggled.connect(self.toggleMultiSelection)

        combobox = QComboBox()
        combobox.addItems(["Ferrari", "Lamborghini", "Pagani", "BMW", "Audi", "Mercedes", "Lotus", "Koenigsegg", "Bugatti", "McLaren"])

        # --Second Column--
        # --Image--
        self.image = QLabel()
        self.image.setPixmap(QPixmap("assets/cat.jpg").scaled(180, 467))
        self.image.hide()

        # ///Layout///
        centerwidget = QWidget()

        #FIRST TAB
        firsttabwidget = QWidget()
        #First row (line edit)
        firstrowlayout = QHBoxLayout()
        firstrowlayout.addWidget(self.label)
        firstrowlayout.addWidget(self.lineedit)
        firstrowlayout.addWidget(self.sendbutton)

        #Second row (slider)
        secondrowlayout = QHBoxLayout()
        secondrowlayout.addWidget(self.minlabel)
        secondrowlayout.addWidget(self.slider)
        secondrowlayout.addWidget(self.maxlabel)

        #Third Row (value label)
        thirdrowlayout = QHBoxLayout()
        thirdrowlayout.addWidget(self.label2)
        thirdrowlayout.addWidget(self.valuelabel)

        #Fourth Row, First Column (Buttons)
        firstcolumnlayout = QVBoxLayout()
        firstcolumnlayout.addWidget(self.button)
        firstcolumnlayout.addWidget(self.button2)
        firstcolumnlayout.addWidget(self.hidebutton)
        #Fourth Row, Second Column (Buttons)
        secondcolumnlayout = QVBoxLayout()
        secondcolumnlayout.addWidget(self.specialbutton)
        #Fourth Row (Buttons)
        fourthrowlayout = QHBoxLayout()
        fourthrowlayout.addLayout(firstcolumnlayout)
        fourthrowlayout.addLayout(secondcolumnlayout)
        
        #Fifth and Sixth Row (checkbox and radiobuttons)
        firstlayout = QHBoxLayout()
        firstlayout.addWidget(box1)
        firstlayout.addWidget(box2)
        secondlayout = QVBoxLayout()
        secondlayout.addLayout(firstlayout)
        secondlayout.addWidget(answers)

        #FIRST TAB LAYOUT
        tabonelayout = QVBoxLayout()
        tabonelayout.addLayout(firstrowlayout)
        tabonelayout.addLayout(secondrowlayout)
        tabonelayout.addLayout(thirdrowlayout)
        tabonelayout.addLayout(fourthrowlayout)
        tabonelayout.addLayout(secondlayout)

        firsttabwidget.setLayout(tabonelayout)

        #SECOND TAB
        secondtabwidget = QWidget()
        #SECOND TAB LAYOUT
        tabtwolayout = QVBoxLayout()
        tabtwolayout.addWidget(listwidget)
        tabtwolayout.addWidget(add)
        tabtwolayout.addWidget(remove)
        tabtwolayout.addWidget(multi)
        tabtwolayout.addWidget(combobox)

        secondtabwidget.setLayout(tabtwolayout)

        #FIRST COLUMN LAYOUT
        #add tabs
        tabwidget.addTab(firsttabwidget, "QSlider")
        tabwidget.addTab(secondtabwidget, "QListFile")
        #define tabwidget layout
        tabslayout = QVBoxLayout()
        tabslayout.addWidget(tabwidget)

        #FINAL LAYOUT
        layoutwimage = QHBoxLayout(centerwidget)
        layoutwimage.addLayout(tabslayout)
        layoutwimage.addWidget(self.image)   

        self.setCentralWidget(centerwidget)
        

    def sliderposition(self, value):
        self.valuelabel.setText(str(value))


    def buttonpressed(self):
        self.slider.setValue(0)

    def button2pressed(self):
        self.slider.setValue(255)
    
    def hidecommands(self, value):
        if value == True:
            self.label.hide()
            self.lineedit.hide()
            self.sendbutton.hide()
            self.minlabel.hide()
            self.slider.hide()
            self.maxlabel.hide()
            self.label2.hide()
            self.valuelabel.hide()
            self.button.hide()
            self.button2.hide()
            self.specialbutton.hide()
            self.hidebutton.setText("Show controls")
        else:
            self.label.show()
            self.lineedit.show()
            self.sendbutton.show()
            self.minlabel.show()
            self.slider.show()
            self.maxlabel.show()
            self.label2.show()
            self.valuelabel.show()
            self.button.show()
            self.button2.show()
            self.specialbutton.show()
            self.hidebutton.setText("Hide controls")
    
    def quit(self):
        app.quit()

    def hideactiontoolbar(self):
        if self.hidebutton.isChecked():
            self.controlshidden()
        else:
            self.hidebutton.setChecked(True)
            self.hidecommands(value=True)

    def showactiontoolbar(self):
        if self.hidebutton.isChecked():
            self.hidebutton.setChecked(False)
            self.hidecommands(value=False)
            
        else:
            self.controlshown()
    
    def changecolor(self, value):
        if value == True:
            self.image.show()
        else:
            self.image.hide()

    def controlshidden(self):
        message = QMessageBox()
        message.setWindowTitle("Warning!")
        message.setWindowIcon(QIcon('assets/simplemanager.ico'))
        message.setIcon(QMessageBox.Warning)
        message.setText("Controls already hidden!")
        message.setInformativeText("Press Apply to show them")
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Apply)
        message.setDefaultButton(QMessageBox.Ok)
        ret = message.exec()

        if ret == QMessageBox.Ok:
            return
        else:
            self.hidebutton.setChecked(False)
            self.hidecommands(value=False)
    
    def controlshown(self):
        message = QMessageBox()
        message.setWindowTitle("Warning!")
        message.setWindowIcon(QIcon('assets/simplemanager.ico'))
        message.setIcon(QMessageBox.Warning)
        message.setText("Controls already shown!")
        message.setInformativeText("Press Apply to hide them")
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Apply)
        message.setDefaultButton(QMessageBox.Ok)
        ret = message.exec()

        if ret == QMessageBox.Ok:
            return
        else:
            self.hidebutton.setChecked(True)
            self.hidecommands(value=True)
        
    def delusional(self):
        ref = QMessageBox.information(self, "Anticlimatic, I know...", "This button doesn't really do anything...", QMessageBox.Ok)
        if ref == QMessageBox.Ok:
            return
    
    def pressedfunction(self):
        self.minlabel.hide()
        self.slider.hide()
        self.maxlabel.hide()
        self.label2.hide()
        self.valuelabel.hide()
    
    def releasedfunction(self):
        self.minlabel.show()
        self.slider.show()
        self.maxlabel.show()
        self.label2.show()
        self.valuelabel.show()
    
    def setvalue(self):
        number = self.lineedit.text()
        if number.isnumeric():
            if int(number) >= 0 and int(number) <= 255:
                self.slider.setValue(int(number))
                self.lineedit.clear()
            else:
                self.lineedit.clear()
                self.minandmax()
        else:
            self.lineedit.clear()
            self.onlynumbers()
    
    def onlynumbers(self):
        ref = QMessageBox.critical(self, "Error", "Only numbers allowed, try again", QMessageBox.Ok)
        if ref == QMessageBox.Ok:
            return
    
    def minandmax(self):
        ref = QMessageBox.critical(self, "Error", "Insert a number between 0 and 255", QMessageBox.Ok)
        if ref == QMessageBox.Ok:
            return

    def addItem(self):
        if self.w is None:
            self.w = AddWindow()
        self.w.show()

    def removeItem(self):
        number = listwidget.selectedItems()
        for i in number:
            listwidget.takeItem(listwidget.row(i))
    
    def toggleMultiSelection(self, button):
        if button == True:
            listwidget.setSelectionMode(QAbstractItemView.MultiSelection)
        else:
            listwidget.setSelectionMode(QAbstractItemView.SingleSelection)


class AddWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QListWidget")
        self.setWindowIcon(QIcon('assets/simplemanager.ico'))

        label = QLabel("New item:")
        self.name = QLineEdit()
        self.name.returnPressed.connect(self.addItem)
        send = QPushButton("Add")
        send.clicked.connect(self.addItem)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.name)
        layout.addWidget(send)

        self.setLayout(layout)
    
    def addItem(self):
        t = str(self.name.text())
        if t != "":
            listwidget.addItem(t)
            self.name.clear()
        else:
            self.noText()
    
    def noText(self):
        message = QMessageBox()
        message.setWindowTitle("Warning!")
        message.setWindowIcon(QIcon('assets/simplemanager.ico'))
        message.setIcon(QMessageBox.Warning)
        message.setText("Can't add an empty item")
        message.setInformativeText("Write the item's name and then press 'Add'")
        message.setDefaultButton(QMessageBox.Ok)
        ret = message.exec()

        if ret == QMessageBox.Ok:
            return

app = QApplication(sys.argv)

window = Application()
window.show()
app.exec()
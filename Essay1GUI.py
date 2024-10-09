from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys

class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Giovanni Orlotti - Essay 1")
        self.setWindowIcon(QIcon('assets/icon.ico'))
        self.setMinimumWidth(600)
        self.w = None

        #First Column
        box1 = QGroupBox("Years to seconds")

        self.yearslabel = QLabel("Insert number of years: ")
        self.yearslineedit = QLineEdit()
        self.yearslineedit.returnPressed.connect(self.yconvert)
        self.yearsbutton = QPushButton("Convert")
        self.yearsbutton.clicked.connect(self.yconvert)

        self.ydisclaimerlabel = QLabel("Calculation based on 30-day months in a year")

        self.monthslabel = QLabel("Months: ")
        self.dayslabel = QLabel("Days: ")
        self.hourslabel = QLabel("Hours: ")
        self.minuteslabel = QLabel("Minutes: ")
        self.secondslabel = QLabel("Seconds: ")

        #Second Column
        box2 = QGroupBox("Seconds to years")

        self.secondsinputlabel = QLabel("Insert number of seconds: ")
        self.secondslenedit = QLineEdit()
        self.secondslenedit.returnPressed.connect(self.sconvert)
        self.secondsbutton = QPushButton("Convert")
        self.secondsbutton.clicked.connect(self.sconvert)

        self.sdisclaimerlabel = QLabel("Calculation based on 30-day months in a year")

        self.sminuteslabel = QLabel("Minutes: ")
        self.shourslabel = QLabel("Hours: ")
        self.sdayslabel = QLabel("Days: ")
        self.smonthslabel = QLabel("Months: ")
        self.syearslabel = QLabel("Seconds: ")

        #Third Column
        box3 = QGroupBox("Address")
        box3.setMinimumWidth(300)

        namelabel = QLabel("Name:")
        self.name = QLineEdit()
        surnamelabel = QLabel("Surname:")
        self.surname = QLineEdit()
        countrylabel = QLabel("Country:")
        self.country = QLineEdit()
        citylabel = QLabel("City:")
        self.city = QLineEdit()
        streetlabel = QLabel("Street:")
        self.street = QLineEdit()
        numberlabel = QLabel("Number:")
        self.number = QLineEdit()
        postalcodelabel = QLabel("Postal code:")
        self.postalcode = QLineEdit()

        spacelabel1 = QLabel("")
        submitbutton = QPushButton("Submit")
        submitbutton.clicked.connect(self.submit)
        spacelabel2 = QLabel("")

        self.userlabel = QLabel("User:")
        self.addresslabel = QLabel("Address:")

        self.shybutton = QPushButton("I'm shy")
        self.shybutton.setCheckable(True)
        self.shybutton.toggled.connect(self.shyfunc)

        self.shy = self.image = QLabel()
        self.shy.setPixmap(QPixmap("assets/soshy.png").scaled(910, 250))
        self.shy.hide()



        # ///Layout///
        centerwidget = QWidget()

        imagelayout = QVBoxLayout(centerwidget)
        groupboxlayout = QHBoxLayout()

        box1layout = QVBoxLayout()

        yearslabel = QHBoxLayout()
        yearslabel.addWidget(self.yearslabel)
        yearslabel.addWidget(self.yearslineedit)

        box1layout.addLayout(yearslabel)
        box1layout.addWidget(self.yearsbutton)
        box1layout.addWidget(self.ydisclaimerlabel)
        box1layout.addWidget(self.monthslabel)
        box1layout.addWidget(self.dayslabel)
        box1layout.addWidget(self.hourslabel)
        box1layout.addWidget(self.minuteslabel)
        box1layout.addWidget(self.secondslabel)

        box1.setLayout(box1layout)
        groupboxlayout.addWidget(box1)

        box2layout = QVBoxLayout()

        secondslabel = QHBoxLayout()
        secondslabel.addWidget(self.secondsinputlabel)
        secondslabel.addWidget(self.secondslenedit)

        box2layout.addLayout(secondslabel)
        box2layout.addWidget(self.secondsbutton)
        box2layout.addWidget(self.sdisclaimerlabel)
        box2layout.addWidget(self.sminuteslabel)
        box2layout.addWidget(self.shourslabel)
        box2layout.addWidget(self.sdayslabel)
        box2layout.addWidget(self.smonthslabel)
        box2layout.addWidget(self.syearslabel)

        box2.setLayout(box2layout)
        groupboxlayout.addWidget(box2)

        box3layout = QVBoxLayout()
        
        namelayout = QHBoxLayout()
        namelayout.addWidget(namelabel)
        namelayout.addWidget(self.name)
        surnamelayout = QHBoxLayout()
        surnamelayout.addWidget(surnamelabel)
        surnamelayout.addWidget(self.surname)
        countrylayout = QHBoxLayout()
        countrylayout.addWidget(countrylabel)
        countrylayout.addWidget(self.country)
        citylayout = QHBoxLayout()
        citylayout.addWidget(citylabel)
        citylayout.addWidget(self.city)
        streetlayout = QHBoxLayout()
        streetlayout.addWidget(streetlabel)
        streetlayout.addWidget(self.street)
        numberlayout = QHBoxLayout()
        numberlayout.addWidget(numberlabel)
        numberlayout.addWidget(self.number)
        postallayout = QHBoxLayout()
        postallayout.addWidget(postalcodelabel)
        postallayout.addWidget(self.postalcode)


        box3layout.addLayout(namelayout)
        box3layout.addLayout(surnamelayout)
        box3layout.addLayout(countrylayout)
        box3layout.addLayout(citylayout)
        box3layout.addLayout(streetlayout)
        box3layout.addLayout(numberlayout)
        box3layout.addLayout(postallayout)
        box3layout.addWidget(spacelabel1)
        box3layout.addWidget(submitbutton)
        box3layout.addWidget(spacelabel2)
        box3layout.addWidget(self.userlabel)
        box3layout.addWidget(self.addresslabel)
        

        box3.setLayout(box3layout)
        groupboxlayout.addWidget(box3)

        imagelayout.addLayout(groupboxlayout)
        imagelayout.addWidget(self.shybutton)
        imagelayout.addWidget(self.shy)

        self.setCentralWidget(centerwidget)

    def yconvert(self):
        self.input = self.yearslineedit.text()
        if self.input.isnumeric():
            if int(self.input) > 0:
                self.setvyalue()
                #self.yearslineedit.clear()
            else:
                self.yearslineedit.clear()
                self.minandmax()
        else:
            self.yearslineedit.clear()
            self.onlynumbers()
    
    def setvyalue(self):
        years = self.input
        mnt = int(years) * 12
        dys = mnt * 30
        hrs = dys * 24
        min = hrs * 60
        scn = min * 60

        self.monthslabel.setText("Months: " + str(mnt))
        self.dayslabel.setText("Days: " + str(dys))
        self.hourslabel.setText("Hours: " + str(hrs))
        self.minuteslabel.setText("Minutes: " + str(min))
        self.secondslabel.setText("Seconds: " + str(scn))
    
    def sconvert(self):
        self.secinput = self.secondslenedit.text()
        if self.secinput.isnumeric():
            if int(self.secinput) > 0:
                self.setsvalue()
                #self.secondslenedit.clear()
            else:
                self.secondslenedit.clear()
                self.minandmax()
        else:
            self.secondslenedit.clear()
            self.onlynumbers()
    
    def setsvalue(self):
        seconds = self.secinput
        minutes = int(seconds)/60
        hours = minutes/60
        days = hours/24
        months = days/30
        years = months/12

        self.sminuteslabel.setText("Minutes: " + str(minutes))
        self.shourslabel.setText("Hours: " + str(hours))
        self.sdayslabel.setText("Days: " + str(days))
        self.smonthslabel.setText("Months: " + str(months))        
        self.syearslabel.setText("Years: " + str(years))
        
    def onlynumbers(self):
        ref = QMessageBox.critical(self, "Error", "Only numbers allowed, try again", QMessageBox.Ok)
        if ref == QMessageBox.Ok:
            return
    
    def minandmax(self):
        ref = QMessageBox.critical(self, "Error", "Insert a number higher than 0", QMessageBox.Ok)
        if ref == QMessageBox.Ok:
            return
        
    def submit(self):
        name = self.name.text()
        surname = self.surname.text()
        country = self.country.text()
        city = self.city.text()
        street = self.street.text()
        number = self.number.text()
        postalcode = self.postalcode.text()

        self.userlabel.setText("User: " + name + " " + surname)
        self.addresslabel.setText("Address: " + street + " " + number + ", " + postalcode + ", " + city + ", " + country)

    def shyfunc(self, button):
        if button == True:
            self.shy.show()
        else:
            self.shy.hide()

class Shywindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Giovanni Orlotti - Essay 1")
        self.setWindowIcon(QIcon('assets/icon.ico'))
        self.w = None
            

app = QApplication(sys.argv)

window = Application()
window.show()
app.exec()
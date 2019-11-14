from PyQt5.QtGui import QBrush, QColor, QFont
from PyQt5.QtWidgets import QApplication, QStackedWidget, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGraphicsWidget, QPushButton,  QListWidget, QListWidgetItem, QLineEdit, QFormLayout
from PyQt5.QtCore import Qt
import courses as cs

class Students(QWidget):
    def __init__(self, data):
        super().__init__()
        self._course = cs.Course(data)
        self.title = QLabel('Students')
        self.nums = QLabel('Enrolled: ')
        self.num = QLabel(str(len(self._course.getStudents())))
        self.delBtn = QPushButton('Remove')
        self.addBtn = QPushButton('Add')
        self.backBtn = QPushButton('Back')
        self.list = QListWidget()
        self.ll = self._course.getStudents()

        i = 0
        while i < len(self.ll):
            itm = QListWidgetItem(self.ll[i], self.list)
            itm.setFont(QFont("Open Sans Regular", 8, QFont.Bold))
            itm.setForeground(QBrush(QColor('dimgray')))
            i += 1

        hlay = QHBoxLayout()
        hlay0 = QHBoxLayout()
        hlay1 = QHBoxLayout()
        hlayout = QHBoxLayout()
        vlay = QVBoxLayout()

        self.title.setAlignment(Qt.AlignHCenter)
        self.title.setFont(QFont("Open Sans Regular", 16, QFont.Bold))
        self.title.setFixedWidth(self.width() * 0.75)
        self.title.setWordWrap(True)
        self.title.setStyleSheet("color: goldenrod")
        self.nums.setFont(QFont("Open Sans Regular", 12, QFont.Bold))
        self.nums.setStyleSheet("color: goldenrod")
        self.num.setFont(QFont("Open Sans Regular", 12, QFont.Bold))
        self.num.setStyleSheet("color: goldenrod")
        self.addBtn.setStyleSheet("background-color: goldenrod; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 12px; padding: 6px;")
        self.backBtn.setStyleSheet("background-color: goldenrod; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 12px; padding: 6px;")
        self.delBtn.setStyleSheet("background-color: goldenrod; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 12px; padding: 6px;")

        hlay0.addSpacing(30)
        hlay0.addWidget(self.backBtn)
        hlay0.addSpacing(30)
        hlayout.addSpacing(30)
        hlayout.addWidget(self.addBtn)
        hlayout.addSpacing(60)
        hlayout.addWidget(self.delBtn)
        hlayout.addSpacing(30)
        hlay.setAlignment(Qt.AlignHCenter)
        hlay.addSpacing(30)
        hlay.addWidget(self.nums)
        hlay.addWidget(self.num)
        hlay.addSpacing(30)
        hlay1.addSpacing(30)
        hlay1.addWidget(self.list)
        hlay1.addSpacing(30)
        vlay.addSpacing(15)
        vlay.addWidget(self.title)
        vlay.addLayout(hlay)
        vlay.addLayout(hlay1)
        vlay.addLayout(hlayout)
        vlay.addLayout(hlay0)
        vlay.addSpacing(30)
        self.setLayout(vlay)

class Student():
    def __init__(self, data):
        self.__name = data['name']
        self.__matric = data['matric']
        self.__leftprint = data['leftprint']
        self.__rightprint = data['rightprint']

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setMatric(self, name):
        self.__matric = name

    def getMatric(self):
        return self.__matric

    def setLeftPrint(self, name):
        self.__leftprint = name

    def getLeftPrint(self):
        return self.__leftprint

    def setRightPrint(self, name):
        self.__rightprint = name

    def getRightPrint(self):
        return self.__rightprint

class StudentForm(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel('Fill in the form!')
        self.left = QLabel('Left')
        self.right = QLabel('Right')
        self.fingerprint = QLabel('Fingerprint')
        self.addLFPBtn = QPushButton('Add')
        self.addRFPBtn = QPushButton('Add')
        self.nxtBtn = QPushButton('Register')
        self.backBtn = QPushButton('Back')
        self.statLFP = QLabel('Status: NULL')
        self.statRFP = QLabel('Status: NULL')
        self.leftFP = QLabel('Left')
        self.rightFP = QLabel('Right')
        self.fingerprint = QLabel('Fingerprint')

        self.nameLineEdit = QLineEdit()
        self.matricLineEdit = QLineEdit()

        flay = QFormLayout()
        hlay = QHBoxLayout()
        hlay0 = QHBoxLayout()
        hlay2 = QHBoxLayout()
        hlay3 = QHBoxLayout()
        hlay4 = QHBoxLayout()
        vlay2 = QVBoxLayout()
        vlay3 = QVBoxLayout()
        vlay = QVBoxLayout()
        vlay0 = QVBoxLayout()

        self.title.setAlignment(Qt.AlignHCenter)
        self.title.setFont(QFont("Open Sans Regular", 16, QFont.Bold))
        self.title.setFixedWidth(self.width() * 0.675)
        self.title.setStyleSheet('color: peru')
        self.title.setWordWrap(True)
        self.addLFPBtn.setFont(QFont("Open Sans Regular", 20, QFont.Light))
        self.addRFPBtn.setFont(QFont("Open Sans Regular", 20, QFont.Light))
        self.nxtBtn.setFont(QFont("Open Sans Regular", 20, QFont.Light))
        self.backBtn.setFont(QFont("Open Sans Regular", 20, QFont.Light))
        self.leftFP.setFont(QFont("Open Sans Regular", 10, QFont.Bold))
        self.leftFP.setStyleSheet('color: goldenrod')
        self.rightFP.setFont(QFont("Open Sans Regular", 10, QFont.Bold))
        self.rightFP.setStyleSheet('color: goldenrod')
        self.fingerprint.setFont(QFont("Open Sans Regular", 10, QFont.Bold))
        self.fingerprint.setStyleSheet('color: goldenrod')
        self.statLFP.setFont(QFont("Open Sans Regular", 10, QFont.Bold))
        self.statLFP.setStyleSheet('color: goldenrod')
        self.statRFP.setFont(QFont("Open Sans Regular", 10, QFont.Bold))
        self.statRFP.setStyleSheet('color: goldenrod')
        self.backBtn.setStyleSheet("background-color: goldenrod; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 12px; color: darkslategrey; padding: 6px;")
        self.nxtBtn.setStyleSheet("background-color: goldenrod; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 12px; color: darkslategrey; padding: 6px;")
        self.addLFPBtn.setStyleSheet("background-color: goldenrod; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 12px; color: darkslategrey; padding: 6px;")
        self.addRFPBtn.setStyleSheet("background-color: goldenrod; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 12px; color: darkslategrey; padding: 6px;")

        flay.addRow(self.tr('<font color="goldenrod" size=8>   &Name:</font>'), self.nameLineEdit)
        flay.addRow(self.tr('<font color="goldenrod" size=8> &Matric:</font>'), self.matricLineEdit)

        hlay3.addSpacing(30)
        hlay3.addLayout(flay)
        hlay3.addSpacing(30)

        hlay4.addSpacing(30)
        hlay4.addWidget(self.title)
        hlay4.addSpacing(30)
        hlay4.setAlignment(Qt.AlignHCenter)
        
        hlay.addSpacing(30)
        hlay.addWidget(self.backBtn)
        hlay.addSpacing(60)
        hlay.addWidget(self.nxtBtn)
        hlay.addSpacing(30)

        vlay2.addWidget(self.leftFP)
        vlay2.addWidget(self.statLFP)
        vlay2.addWidget(self.addLFPBtn)

        vlay3.addWidget(self.rightFP)
        vlay3.addWidget(self.statRFP)
        vlay3.addWidget(self.addRFPBtn)

        vlay0.addWidget(self.fingerprint)
        hlay0.addLayout(vlay2)
        hlay0.addLayout(vlay3)
        vlay0.addLayout(hlay0)

        hlay2.addSpacing(30)
        hlay2.addLayout(vlay0)
        hlay2.addSpacing(30)
        vlay.addSpacing(15)
        vlay.addLayout(hlay4)
        vlay.addLayout(hlay3)
        vlay.addLayout(hlay2)
        vlay.addLayout(hlay)
        vlay.addSpacing(15)
        vlay.addSpacing(30)
        self.setLayout(vlay)

class StudentListForm(QWidget):
    def __init__(self, data):
        super().__init__()
        self.title = QLabel('Add or Enroll Students!')
        self.info = QLabel('Double Click to Student(s) to mark for Selection!')
        self.addBtn = QPushButton('Add')
        self.enroBtn = QPushButton('Enroll')
        self.backBtn = QPushButton('Back')
        self.list = QListWidget()
        self.ll = data

        i = 0
        while i < len(self.ll):
            itm = QListWidgetItem(self.ll[i], self.list)
            itm.setFont(QFont("Open Sans Regular", 8, QFont.Bold))
            itm.setForeground(QBrush(QColor('dimgray')))
            i += 1

        hlay = QHBoxLayout()
        hlay0 = QHBoxLayout()
        hlay2 = QHBoxLayout()
        hlay3 = QHBoxLayout()
        hlay4 = QHBoxLayout()
        vlay = QVBoxLayout()

        self.title.setAlignment(Qt.AlignHCenter)
        self.title.setFont(QFont("Open Sans Regular", 16, QFont.Bold))
        self.title.setFixedWidth(self.width() * 0.675)
        self.title.setStyleSheet('color: peru')
        self.title.setWordWrap(True)
        self.info.setFont(QFont("Open Sans Regular", 10, QFont.Bold))
        self.info.setStyleSheet("color: goldenrod")
        self.addBtn.setStyleSheet("background-color: goldenrod; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 12px; padding: 6px;")
        self.backBtn.setStyleSheet("background-color: goldenrod; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 12px; padding: 6px;")
        self.enroBtn.setStyleSheet("background-color: goldenrod; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 12px; padding: 6px;")

        hlay.addSpacing(30)
        hlay.addWidget(self.title)
        hlay.addSpacing(30)
        hlay0.addSpacing(30)
        hlay0.addWidget(self.info)
        hlay0.addSpacing(30)
        hlay2.addSpacing(30)
        hlay2.addWidget(self.list)
        hlay2.addSpacing(30)
        hlay3.addSpacing(30)
        hlay3.addWidget(self.addBtn)
        hlay3.addSpacing(60)
        hlay3.addWidget(self.enroBtn)
        hlay3.addSpacing(30)
        hlay4.addSpacing(30)
        hlay4.addWidget(self.backBtn)
        hlay4.addSpacing(30)
        vlay.addSpacing(15)
        vlay.addLayout(hlay)
        vlay.addSpacing(10)
        vlay.addLayout(hlay0)
        vlay.addLayout(hlay2)
        vlay.addLayout(hlay3)
        vlay.addLayout(hlay4)
        self.setLayout(vlay)
import sys
import os
import json as j
from PyQt5.QtGui import QBrush, QPixmap, QPalette, QFont
from PyQt5.QtWidgets import QApplication, QStackedWidget, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGraphicsWidget, QPushButton,  QListWidget, QListWidgetItem, QLineEdit, QFormLayout
from PyQt5.QtCore import Qt

class WelcomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel('Biometric Attendance System using Fingerprint and Iris')
        self.regBtn = QPushButton('Register\nCourse')
        self.selBtn = QPushButton('Select\nCourse')
        hlayout = QHBoxLayout()
        vlayout = QVBoxLayout()
        vlayout1 = QVBoxLayout()

        self.title.setAlignment(Qt.AlignHCenter)
        self.title.setFont(QFont("Open Sans Regular", 24, QFont.Bold))
        self.title.setFixedWidth(self.width() * 0.75)
        self.title.setWordWrap(True)
        self.title.setStyleSheet("color: goldenrod")
        self.regBtn.setFont(QFont("Open Sans Regular", 20, QFont.Light))
        self.selBtn.setFont(QFont("Open Sans Regular", 20, QFont.Light))
        self.regBtn.setMinimumWidth(160)
        self.regBtn.setMinimumHeight(160)
        self.selBtn.setMinimumWidth(160)
        self.selBtn.setMinimumHeight(160)
        self.regBtn.setStyleSheet("background-color: goldenrod; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 22px; padding: 6px;")
        self.selBtn.setStyleSheet("background-color: goldenrod; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: beige;"
                " font: bold 22px; padding: 6px;")

        hlayout.addWidget(self.regBtn)
        hlayout.addWidget(self.selBtn)
        vlayout1.addSpacing(15)
        vlayout1.addWidget(self.title)
        vlayout.addLayout(vlayout1)
        vlayout.addLayout(hlayout)
        self.setLayout(vlayout)
        
class SelectPage(QWidget):
    def __init__(self, ls):
        super().__init__()
        self.title = QLabel('Select a course')
        self.list = QListWidget()
        self.backBtn = QPushButton('Back')
        hlayout = QHBoxLayout()
        vlayout = QVBoxLayout()
        
        self.list.resize(256, 192)
        self.l = ls
        
        i=0
        while i < len(self.l):
            QListWidgetItem(self.l[i], self.list)
            i += 1
        
        hlayout.addWidget(self.backBtn)
        hlayout.addSpacing(100)
        vlayout.addWidget(self.title)
        vlayout.addWidget(self.list)
        vlayout.addLayout(hlayout)
        self.setLayout(vlayout)
        
class RegisterPage(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel('Course registration:')
        
        self.regBtn = QPushButton('Register')
        self.backBtn = QPushButton('Back')
        self.titleLineEdit = QLineEdit()
        self.codeLineEdit = QLineEdit()
        self.periodLineEdit = QLineEdit()
        self.dayLineEdit = QLineEdit()
        
        formLayout = QFormLayout()
        hlay = QHBoxLayout()
        vlay = QVBoxLayout()

        self.title.setAlignment(Qt.AlignHCenter)
        self.title.setFont(QFont("Open Sans Regular", 24, QFont.Bold))
        self.title.setFixedWidth(self.width() * 0.75)
        self.title.setWordWrap(True)
        self.title.setStyleSheet("color: goldenrod")
        self.regBtn.setFont(QFont("Open Sans Regular", 20, QFont.Light))
        self.backBtn.setFont(QFont("Open Sans Regular", 20, QFont.Light))
        self.regBtn.setMinimumWidth(120)
        self.regBtn.setMaximumHeight(40)
        self.backBtn.setMinimumWidth(120)
        self.backBtn.setMaximumHeight(40)
        self.regBtn.setStyleSheet("background-color: goldenrod; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 22px; padding: 6px;")
        self.backBtn.setStyleSheet("background-color: goldenrod; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 22px; padding: 6px;")
        
        formLayout.addRow(self.tr('<font color="gold" size=12>&Course Title:</font>'), self.titleLineEdit)
        formLayout.addRow(self.tr('<font color="gold" size=12> &Course Code:</font>'), self.codeLineEdit)
        formLayout.addRow(self.tr('<font color="gold" size=12>    &Week Day:</font>'), self.dayLineEdit)
        formLayout.addRow(self.tr('<font color="gold" size=12>      &Period:</font>'), self.periodLineEdit)
        hlay.addWidget(self.backBtn)
        hlay.addSpacing(50)
        hlay.addWidget(self.regBtn)
        vlay.addSpacing(25)
        vlay.addWidget(self.title)
        vlay.addLayout(formLayout)
        vlay.addSpacing(25)
        vlay.addLayout(hlay)
        vlay.addSpacing(15)
        self.setLayout(vlay)
        
class Courses(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel('Computer Logic')
        self.code = QLabel('CPE324')
        self.day = QLabel('Tuesday')
        self.period = QLabel('02:30 pm')
        self.studBtn = QPushButton('Student(s)')
        self.attdBtn = QPushButton('Attendance')
        self.backBtn = QPushButton('Back')
        self.course = Course()
        
        vlay = QVBoxLayout()
        hlay = QHBoxLayout()
        hlayout = QHBoxLayout()
        hlayout1 = QHBoxLayout()
        
        hlay.addWidget(self.code)
        hlay.addSpacing(20)
        hlay.addWidget(self.day)
        hlay.addSpacing(20)
        hlay.addWidget(self.period)
        hlayout.addWidget(self.studBtn)
        hlayout.addSpacing(50)
        hlayout.addWidget(self.attdBtn)
        hlayout1.addWidget(self.backBtn)
        vlay.addWidget(self.title)
        vlay.addLayout(hlay)
        vlay.addLayout(hlayout)
        vlay.addLayout(hlayout1)
        self.setLayout(vlay)
        
class Attendances(QWidget):
    def __init__(self):
        super().__init__()
        self.week = QLabel('Week 1')
        self.code = QLabel('CPE324')
        self.attend = QLabel('Attendee(s): ')
        self.score = QLabel('__ / __')
        self.active = QLabel('Waiting!!!<br>Enter Biometric!')
        self.attBtn = QPushButton('Start Attendance')
        self.viewBtn = QPushButton('View All Attendance')
        self.backbtn = QPushButton('Back')
        
        vlay = QVBoxLayout()
        hlay = QHBoxLayout()
        hlayout = QHBoxLayout()
        hlayout0 = QHBoxLayout()
        
        hlay.addWidget(self.attend)
        hlay.addWidget(self.score)
        hlayout.addWidget(self.attBtn)
        hlayout.addSpacing(50)
        hlayout.addWidget(self.viewBtn)
        hlayout0.addWidget(self.attBtn)
        hlayout0.addWidget(self.backbtn)
        vlay.addWidget(self.code)
        vlay.addWidget(self.week)
        vlay.addLayout(hlay)
        vlay.addWidget(self.active)
        vlay.addLayout(hlayout0)
        self.setLayout(vlay)
        
class Students(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel('Students')
        self.nums = QLabel('Enrolled: ')
        self.num = QLabel('00')
        self.addBtn = QPushButton('Add')
        self.delBtn = QPushButton('Delete')
        self.editBtn = QPushButton('Edit')
        self.backBtn = QPushButton('Back')
        self.list = QListWidget()

        hlay = QHBoxLayout()
        hlayout = QHBoxLayout()
        vlay = QVBoxLayout()

        hlayout.addWidget(self.backBtn)
        hlayout.addSpacing(10)
        hlayout.addWidget(self.delBtn)
        hlayout.addWidget(self.editBtn)
        hlay.addWidget(self.nums)
        hlay.addWidget(self.num)
        vlay.addWidget(self.title)
        vlay.addLayout(hlay)
        vlay.addWidget(self.list)
        vlay.addLayout(hlayout)
        self.setLayout(vlay)

class Course():
    def __init__(self):
        super().__init__()
        self.__title = 'Dummy Dummy'
        self.code = 'Dummy Dummy'
        self.day = 'Dummy Dummy'
        self.period = 'Dummy Dummy'

    def setTitle(self, name):
        self.__title = name

    def getTitle(self):
        return self.__title

    def setCode(self, name):
        self.__code = name

    def getCode(self):
        return self.__code

    def setDay(self, name):
        self.__day = name

    def getDay(self):
        return self.__day

    def setPeriod(self, name):
        self.__period = name

    def getPeriod(self):
        return self.__period

class Student():
    def __init__(self):
        self.__name = 'Dummy Dummy'
        self.__matric = 'Dummy Dummy'
        self.__leftprint = 'Dummy Dummy'
        self.__rightprint = 'Dummy Dummy'
        self.__leftiris = 'Dummy Dummy'
        self.__rightiris = 'Dummy Dummy'

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

    def setLeftIris(self, name):
        self.__leftiris = name

    def getLeftIris(self):
        return self.__leftiris

    def setRightIris(self, name):
        self.__rightiris = name

    def getRightIris(self):
        return self.__rightiris

class StudentForm(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel('Fill in the form!')
        self.left = QLabel('Left')
        self.right = QLabel('Right')
        self.iris = QLabel('Iris')
        self.fingerprint = QLabel('Fingerprint')
        self.name = ''
        self.matric = ''

        nameLineEdit = QLineEdit()
        matricLineEdit = QLineEdit()
        flay = QFormLayout()
        vlay = QVBoxLayout()
        hlayout = QHBoxLayout()
        hlayout0 = QHBoxLayout()
        hlayout1 = QHBoxLayout()
        vlayout0 = QVBoxLayout()
        vlayout1 = QVBoxLayout()
        vlayout2 = QHBoxLayout()
        vlayout3 = QHBoxLayout()
        vlayout4 = QHBoxLayout()
        vlayout5 = QHBoxLayout()

        self.leftFingerprint = QWidget()
        self.rightFingerprint = QWidget()
        self.leftIris = QWidget()
        self.rightIris = QWidget()
        self.leftFingerprint.resize(120, 160)
        self.rightFingerprint.resize(120, 160)
        self.leftIris.resize(120, 160)
        self.rightIris.resize(120, 160)

        flay.addRow(self.tr('   &Name:'), nameLineEdit)
        flay.addRow(self.tr(' &Matric:'), matricLineEdit)
        vlayout2.addWidget(self.left)
        vlayout2.addWidget(self.leftFingerprint)
        vlayout4.addWidget(self.right)
        vlayout4.addWidget(self.rightFingerprint)
        vlayout3.addWidget(self.left)
        vlayout3.addWidget(self.leftIris)
        vlayout5.addWidget(self.right)
        vlayout5.addWidget(self.rightIris)
        hlayout0.addLayout(vlayout2)
        hlayout0.addLayout(vlayout4)
        hlayout1.addLayout(vlayout3)
        hlayout1.addLayout(vlayout5)
        vlayout0.addWidget(self.fingerprint)
        vlayout0.addLayout(hlayout0)
        vlayout1.addWidget(self.iris)
        vlayout1.addLayout(hlayout1)
        hlayout.addLayout(vlayout0)
        hlayout.addLayout(vlayout1)
        vlay.addWidget(self.title)
        vlay.addLayout(flay)
        vlay.addLayout(hlayout)
        self.setLayout(vlay)

class ViewAttendance(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel('View Attendance')
        self.backBtn = QPushButton('Back')
        self.list = QListWidget()

        self.list.resize(400, 240)

class Controller():
    def __init__(self):
        course = Course()
        course.setTitle('Computer Programming')
        course.setCode('CPE311')
        course.setPeriod('9:00')
        course.setDay('Monday')
        self.saveCourse(course)

    def getCourseCodes(self):
        doc = self.readfile('courses')
        lst = []
        for x in doc:
            lst.append(x)
        return lst

    def getCourse(self, code):
        doc = self.readfile('courses')
        lst = {}
        for x in doc:
            if x == code:
                lst = doc[x]
        return lst

    def saveCourse(self, course):
        doc = self.readfile('courses')
        jsonObj = {"title": course.getTitle(),"code": course.getCode(),"day": course.getDay(),"period": course.getPeriod()}
        doc[course.getCode()] = jsonObj
        self.savefile('courses', 'w', doc)

    def savefile(self, name, mode, data):
        with open(name + '.json', mode) as f:
            j.dump(data, f, indent=4)
        f.close()

    def readfile(self, name):
        with open(name + '.json') as f:
            data = j.load(f)
        f.close()
        return data

class StackedWidgetUI(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.con = Controller()
        self.welcome = WelcomePage()
        self.select = SelectPage(self.con.getCourseCodes())
        self.register = RegisterPage()
        self.course = Courses()
        self.attend = Attendances()
        self.students = Students()
        self.studform = StudentForm()
        self.view = ViewAttendance()

        pal = QPalette()
        pal.setBrush(QPalette.Window, QBrush(QPixmap("background_dark.jpeg")))
        self.setPalette(pal)

        self.welcome.regBtn.clicked.connect(self.regBtnClicked)
        self.welcome.selBtn.clicked.connect(self.selBtnClicked)
        self.select.backBtn.clicked.connect(self.backBtnClicked)
        self.register.regBtn.clicked.connect(self.regRegBtnClicked)
        self.register.backBtn.clicked.connect(self.backBtnClicked)
        self.course.studBtn.clicked.connect(self.stuBtnClicked)
        self.course.attdBtn.clicked.connect(self.attBtnClicked)
        self.course.backBtn.clicked.connect(self.backBtnClicked)
        self.attend.attBtn.clicked.connect(self.attAttBtnClicked)
        self.attend.viewBtn.clicked.connect(self.viewBtnClicked)
        self.attend.backbtn.clicked.connect(self.backAttBtnClicked)
        self.students.addBtn.clicked.connect(self.addBtnClicked)
        self.students.delBtn.clicked.connect(self.delBtnClicked)
        self.students.editBtn.clicked.connect(self.editBtnClicked)
        self.students.backBtn.clicked.connect(self.backStuBtnClicked)
        self.view.backBtn.clicked.connect(self.backVewBtnClicked)
        self.select.list.itemClicked.connect(self.currentItemClicked('CPE526'))

        self.addWidget(self.welcome)
        self.addWidget(self.select)
        self.addWidget(self.register)
        self.addWidget(self.course)
        self.addWidget(self.attend)
        self.addWidget(self.students)
        self.addWidget(self.studform)
        self.addWidget(self.view)

        self.setGeometry(0, 0, 480, 320)

    def concurrency(self):
        pass

    def regBtnClicked(self):
        self.setCurrentIndex(2)
        self.register.regBtn.setDisabled(True)

    def selBtnClicked(self):
        self.setCurrentIndex(1)

    def regRegBtnClicked(self):
        title = self.register.titleLineEdit.text()
        code = self.register.codeLineEdit.text()
        day = self.register.dayLineEdit.text()
        period = self.register.periodLineEdit.text()

        course = Course()
        course.setCode(code)
        course.setDay(day)
        course.setPeriod(period)
        course.setTitle(title)

        self.con.saveCourse(course)
        self.register.titleLineEdit.setText('')
        self.register.codeLineEdit.setText('')
        self.register.dayLineEdit.setText('')
        self.register.periodLineEdit.setText('')
        self.setCurrentIndex(3)

    def stuBtnClicked(self):
        self.setCurrentIndex(5)

    def attBtnClicked(self):
        self.setCurrentIndex(4)

    def attAttBtnClicked(self):
        # Not defined
        pass

    def backAttBtnClicked(self):
        self.setCurrentIndex(3)

    def viewBtnClicked(self):
        self.setCurrentIndex(7)

    def addBtnClicked(self):
        self.setCurrentIndex(6)

    def delBtnClicked(self):
        # Not defined
        pass

    def editBtnClicked(self):
        self.setCurrentIndex(6)

    def backBtnClicked(self):
        self.setCurrentIndex(0)

    def backStuBtnClicked(self):
        self.setCurrentIndex(3)

    def backVewBtnClicked(self):
        self.setCurrentIndex(4)

    def currentItemClicked(self, code):
        cour = self.con.getCourse(code)
        self.course.course.setTitle(cour['title'])
        self.course.course.setDay(cour['day'])
        self.course.course.setCode(cour['code'])
        self.course.course.setPeriod(cour['period'])
        self.course.title = QLabel(self.course.course.getTitle())
        self.course.code = QLabel(self.course.course.getCode())
        self.course.day = QLabel(self.course.course.getDay())
        self.course.period = QLabel(self.course.course.getPeriod())
        self.setCurrentIndex(3)

def main():
    app = QApplication(sys.argv)
    stack = StackedWidgetUI()
    con = Controller()
    stack.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
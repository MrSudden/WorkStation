import courses as cs
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt

class Attendant():
    def __init__(self, data):
        self.__week = None
        self.__count = 0
        self.__code = ''
        self.__students = []
        self.setWeek(data['week'])
        self.setCode(data['code'])
        self.setCount(data['count'])
        self.setStudents(data['students'])

    def incrementWeek(self):
        self.__week += 1

    def incrementCount(self):
        self.__count += 1

    def setCode(self, name):
        self.__code = name

    def getCode(self):
        return self.__code

    def addStudents(self, data):
        if not data in self.__students:
            self.__students.append(data)
            self.incrementCount()

    def setCount(self, cnt):
        self.__count = cnt

    def getCount(self):
        return self.__count

    def setWeek(self, wk):
        self.__week = wk

    def getWeek(self):
        return self.__week

    def setStudents(self, lst):
        self.__students = lst

    def getStudents(self):
        return self.__students

class Attendances(QWidget):
    def __init__(self, cour, data):
        super().__init__()
        self._attend = Attendant(data)
        self._course = cs.Course(cour)
        self.week = QLabel('Week ' + str(self._attend.getWeek()))
        self.code = QLabel(str(self._attend.getCode()))
        self.attend = QLabel('Attendee(s): ')
        self.score = QLabel(str(self._attend.getCount()) + ' / ' + str(len(self._course.getStudents())))
        self.active = QLabel('Click Start to\nBegin Attendance!')
        self.attBtn = QPushButton('Start Lecture Attendance')
        self.examBtn = QPushButton('Start Exam Attendance')
        self.viewBtn = QPushButton('View All Attendance')
        self.backBtn = QPushButton('Back')
        
        vlay = QVBoxLayout()
        hlay = QHBoxLayout()
        hlayout = QHBoxLayout()
        hlayout0 = QHBoxLayout()
        hlayout1 = QHBoxLayout()
        hlayout2 = QHBoxLayout()

        self.week.setFont(QFont("Open Sans Regular", 16, QFont.Bold))
        self.week.setStyleSheet("color: goldenrod")
        self.code.setFont(QFont("Open Sans Regular", 12, QFont.Bold))
        self.code.setStyleSheet("color: goldenrod")
        self.score.setFont(QFont("Open Sans Regular", 12, QFont.Bold))
        self.score.setStyleSheet("color: goldenrod")
        self.active.setAlignment(Qt.AlignHCenter)
        self.active.setFont(QFont("Open Sans Regular", 12, QFont.Bold))
        self.active.setStyleSheet("color: goldenrod")
        self.attend.setFont(QFont("Open Sans Regular", 12, QFont.Bold))
        self.attend.setStyleSheet("color: goldenrod")
        self.examBtn.setStyleSheet("background-color: goldenrod; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 12px; padding: 6px;")
        self.attBtn.setStyleSheet("background-color: goldenrod; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 12px; padding: 6px;")
        self.backBtn.setStyleSheet("background-color: goldenrod; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 12px; padding: 6px;")
        self.viewBtn.setStyleSheet("background-color: goldenrod; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 12px; padding: 6px;")
        
        hlay.addSpacing(30)
        hlay.addWidget(self.attend)
        hlay.addWidget(self.score)
        hlay.addSpacing(30)
        hlay.setAlignment(Qt.AlignHCenter)
        hlayout.addSpacing(30)
        hlayout.addWidget(self.attBtn)
        hlayout.addSpacing(15)
        hlayout.addWidget(self.examBtn)
        hlayout.addSpacing(15)
        hlayout.addWidget(self.viewBtn)
        hlayout.addSpacing(30)
        hlayout2.setAlignment(Qt.AlignHCenter)
        hlayout2.addSpacing(30)
        hlayout2.addWidget(self.code)
        hlayout2.addSpacing(60)
        hlayout2.addWidget(self.week)
        hlayout2.addSpacing(30)
        hlayout0.addSpacing(30)
        hlayout0.addWidget(self.backBtn)
        hlayout0.addSpacing(30)
        hlayout1.addSpacing(120)
        hlayout1.addWidget(self.active)
        hlayout1.addSpacing(120)
        vlay.addSpacing(15)
        vlay.addLayout(hlayout2)
        vlay.addLayout(hlay)
        vlay.addSpacing(15)
        vlay.addLayout(hlayout1)
        vlay.addSpacing(15)
        vlay.addLayout(hlayout)
        vlay.addLayout(hlayout0)
        vlay.addSpacing(30)
        self.setLayout(vlay)
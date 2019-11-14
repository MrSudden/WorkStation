from PyQt5.QtGui import QBrush, QPixmap, QPalette, QFont
from PyQt5.QtWidgets import QApplication, QStackedWidget, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGraphicsWidget, QPushButton, QListWidget, QListWidgetItem, QLineEdit, QFormLayout
from PyQt5.QtCore import Qt
        
class Course():
    def __init__(self, data):
        self.__title = 'Dummy Dummy'
        self.__code = 'Dummy Dummy'
        self.__day = 'Dummy Dummy'
        self.__period = 'Dummy Dummy'
        self.__students = []
        self.setTitle(data['title'])
        self.setCode(data['code'])
        self.setDay(data['day'])
        self.setPeriod(data['period'])
        self.setStudents(data['students'])

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
        
    def addStudents(self, data):
        if not data in self.__students:
            self.__students.append(data)
    
    def setStudents(self, lst):
        self.__students = lst

    def getStudents(self):
        return self.__students

class Courses(QWidget):
    def __init__(self, cour):
        super().__init__()
        self._course = cour
        self.title = QLabel(self._course.getTitle())
        self.code = QLabel(self._course.getCode())
        self.day = QLabel(self._course.getDay())
        self.period = QLabel(self._course.getPeriod())
        self.studBtn = QPushButton('Student(s)')
        self.attdBtn = QPushButton('Attendance')
        self.backBtn = QPushButton('Back')

        self.title.setAlignment(Qt.AlignHCenter)
        self.title.setFont(QFont("Open Sans Regular", 16, QFont.Bold))
        self.title.setFixedWidth(self.width() * 0.75)
        self.title.setWordWrap(True)
        self.title.setStyleSheet("color: goldenrod")
        self.code.setFont(QFont("Open Sans Regular", 12, QFont.Bold))
        self.code.setStyleSheet("color: goldenrod")
        self.day.setFont(QFont("Open Sans Regular", 12, QFont.Bold))
        self.day.setStyleSheet("color: goldenrod")
        self.period.setFont(QFont("Open Sans Regular", 12, QFont.Bold))
        self.period.setStyleSheet("color: goldenrod")
        self.attdBtn.setStyleSheet("background-color: goldenrod; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 12px; padding: 6px;")
        self.backBtn.setStyleSheet("background-color: goldenrod; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 12px; padding: 6px;")
        self.studBtn.setStyleSheet("background-color: goldenrod; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 12px; padding: 6px;")
        
        vlay = QVBoxLayout()
        hlay = QHBoxLayout()
        hlayout = QHBoxLayout()
        hlayout1 = QHBoxLayout()
        
        hlay.addSpacing(30)
        hlay.addWidget(self.code)
        hlay.addSpacing(60)
        hlay.addWidget(self.day)
        hlay.addSpacing(60)
        hlay.addWidget(self.period)
        hlay.addSpacing(30)
        hlayout.addSpacing(30)
        hlayout.addWidget(self.studBtn)
        hlayout.addSpacing(60)
        hlayout.addWidget(self.attdBtn)
        hlayout.addSpacing(30)
        hlayout1.addSpacing(30)
        hlayout1.addWidget(self.backBtn)
        hlayout1.addSpacing(30)
        vlay.addSpacing(30)
        vlay.addWidget(self.title)
        vlay.addLayout(hlay)
        vlay.addLayout(hlayout)
        vlay.addLayout(hlayout1)
        vlay.addSpacing(30)
        self.setLayout(vlay)
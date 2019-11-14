import sys
import os
import ctypes
import copy as cp
import json as j
import welcome as wl
import register as rg
import selection as sl
import courses as cs
import attendances as at
import student as st
from ast import literal_eval as le
from PyQt5.QtGui import QBrush, QPixmap, QPalette, QFont, QColor
from PyQt5.QtWidgets import QApplication, QStackedWidget, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGraphicsWidget, QPushButton, QListWidget, QListWidgetItem, QLineEdit, QFormLayout
from PyQt5.QtCore import Qt
from pyfingerprint.pyfingerprint import PyFingerprint
from time import sleep
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Students(Base):
    __tablename__ = 'students'
    matric = Column(String, primary_key = True)
    name = Column(String(250))
    leftprint = Column(String(250))
    rightprint = Column(String(250))

class Attendances(Base):
    __tablename__ = 'attendances'
    code = Column(String(12), primary_key = True)
    week = Column(Integer)
    count = Column(Integer)
    students = Column(String())

class Courses(Base):
    __tablename__ = 'courses'
    code = Column(String(12), primary_key = True)
    title = Column(String(250))
    day = Column(String(12))
    period = Column(String(12))
    students = Column(String())

engine = create_engine('sqlite:///attendance.db')
Base.metadata.create_all(engine)
session = Session(engine)

class ViewAttendance(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel('View Attendance')
        self.backBtn = QPushButton('Back')
        self.list = QListWidget()

class Controller():
    def __init__(self):
        self._leftPrint = ''
        self._rightPrint = ''

    def getStudentIDS(self):
        lst = []
        for row in session.query(Students).all():
            lst.append(row.matric)
        return lst

    def  getStudent(self, id):
        data = {}
        row = session.query(Students).filter(Students.matric == id).one()
        data['matric'] = row.matric
        data['name'] = row.name
        data['leftprint'] = row.leftprint
        data['rightprint'] = row.rightprint
        return data

    def saveStudent(self, data):
        session.add(Students(matric = data['matric'], name = data['name'], leftprint = data['leftprint'], rightprint = data['rightprint']))
        session.commit()

    def getCourseCodes(self):
        lst = []
        for row in session.query(Courses).all():
            lst.append(row.code)
        return lst

    def getCourse(self, code):
        data = {}
        row = session.query(Courses).filter(Courses.code == code).one()
        data['code'] = row.code
        data['title'] = row.title
        data['day'] = row.day
        data['period'] = row.period
        if row.students == '':
            data['students'] = []
        else:
            data['students'] = le(row.students)
        return data

    def updateCourseStudents(self, data, datum):
        row = session.query(Courses).filter(Courses.code == str(datum['code']), Courses.students == str(datum['students'])).one()
        row.students = str(data['students'])
        session.commit()

    def saveCourse(self, data):
        session.add(Courses(code = data['code'], title = data['title'], day = data['day'], period = data['period'], students = data['students']))
        session.commit()

    def getCourseAttendance(self, code):
        data = {}
        try:
            row = session.query(Attendances).filter(Attendances.code == code).one()
            data['code'] = row.code
            data['week'] = row.week
            data['count'] = row.count
            data['students'] = le(row.students)
        except Exception as e:
            data['code'] = ''
            data['week'] = ''
            data['count'] = ''
            data['students'] = []
        return data

    def setLeftPrintData(self, data):
        self._leftPrint = data

    def getLeftPrint(self):
        return self._leftPrint

    def setRightPrintData(self, data):
        self._rightPrint = data

    def getRightPrint(self):
        return self._rightPrint

    def searchPrint(self):
        try:
            f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)        

            if ( f.verifyPassword() == False ):
                raise ValueError('The given fingerprint sensor password is wrong!')

        except Exception as e:
            print('The fingerprint sensor could not be initialized!')
            print('Exception message: ' + str(e))
            exit(1)

        ## Gets some sensor information
        print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))       

        while True:
            try:
                print('Waiting for finger...')      

                ## Wait that finger is read
                while ( f.readImage() == False ):
                    pass        

                ## Converts read image to characteristics and stores it in charbuffer 1
                f.convertImage(0x01)        

                ## Searchs template
                result = f.searchTemplate()     

                positionNumber = result[0]
                accuracyScore = result[1]       

                if ( positionNumber == -1 ):
                    print('No match found!')
                else:
                    print('Found template at position #' + str(positionNumber))     

            except Exception as e:
                print('Operation failed!')
                print('Exception message: ' + str(e))       

            sleep(2)

    def enrollPrint(self, typ):
        try:
            f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

            if ( f.verifyPassword() == False ):
                raise ValueError('The given fingerprint sensor password is wrong!')

        except Exception as e:
            print('The fingerprint sensor could not be initialized!')
            print('Exception message: ' + str(e))
            exit(1)

        ## Gets some sensor information
        print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

        ## Tries to enroll new finger
        try:
            print('Waiting for finger...')

            ## Wait that finger is read
            while ( f.readImage() == False ):
                pass

            ## Converts read image to characteristics and stores it in charbuffer 1
            f.convertImage(0x01)

            ## Checks if finger is already enrolled
            result = f.searchTemplate()
            positionNumber = result[0]

            if ( positionNumber >= 0 ):
                print('Template already exists at position #' + str(positionNumber))
                exit(0)

            print('Remove finger...')
            sleep(2)

            print('Waiting for same finger again...')

            ## Wait that finger is read again
            while ( f.readImage() == False ):
                pass

            ## Converts read image to characteristics and stores it in charbuffer 2
            f.convertImage(0x02)

            ## Compares the charbuffers
            if ( f.compareCharacteristics() == 0 ):
                raise Exception('Fingers do not match')

            ## Creates a template
            f.createTemplate()

            ## Saves template at new position number
            positionNumber = f.storeTemplate()
            print('Finger enrolled successfully!')
            print('New template position #' + str(positionNumber))
            if typ == 'left':
                self.setLeftPrintData(str(positionNumber))
            elif typ == 'right':
                self.setRightPrintData(str(positionNumber))

        except Exception as e:
            print('Operation failed!')
            print('Exception message: ' + str(e))
            exit(1)

class StackedWidgetUI(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.con = Controller()
        welcome = wl.WelcomePage()

        pal = QPalette()
        pal.setBrush(QPalette.Window, QBrush(QPixmap("background_dark.jpeg")))
        self.setPalette(pal)

        welcome.regBtn.clicked.connect(self.regBtnClicked)
        welcome.selBtn.clicked.connect(self.selBtnClicked)

        self.addWidget(welcome)

    def regBtnClicked(self):
        self.regist = rg.RegisterPage()
        self.regist.backBtn.clicked.connect(self.backRegBtnClicked)
        self.regist.regBtn.clicked.connect(self.regRegBtnClicked)
        self.addWidget(self.regist)
        self.setCurrentWidget(self.regist)

    def selBtnClicked(self):
        ll = self.con.getCourseCodes()
        self.select = sl.SelectPage(ll)
        self.select.backBtn.clicked.connect(self.backSelBtnClicked)
        self.select.selBtn.clicked.connect(self.selSelBtnClicked)
        self.addWidget(self.select)
        self.setCurrentWidget(self.select)

    def selSelBtnClicked(self):
        if self.select.list.currentItem():
            d = self.con.getCourse(self.select.list.currentItem().text())
            self.data = {}
            self.data['code'] = d['code']
            self.data['title'] = d['title']
            self.data['day'] = d['day']
            self.data['period'] = d['period']
            self.data['students'] = d['students']
            cour = cs.Course(self.data)
            self.course = cs.Courses(cour)
            self.course.backBtn.clicked.connect(self.backCouBtnClicked)
            self.course.attdBtn.clicked.connect(self.attBtnClicked)
            self.course.studBtn.clicked.connect(self.stuBtnClicked)
            self.addWidget(self.course)
            self.setCurrentWidget(self.course)

    def regRegBtnClicked(self):
        data = {}
        if (len(self.regist.titleLineEdit.text()) > 5 and len(self.regist.codeLineEdit.text()) > 3 and len(self.regist.periodLineEdit.text()) > 4  and len(self.regist.dayLineEdit.text()) >  4):
            data['title'] = self.regist.titleLineEdit.text()
            data['code'] = self.regist.codeLineEdit.text()
            data['day'] = self.regist.dayLineEdit.text()
            data['period'] = self.regist.periodLineEdit.text()
            data['students'] = ''
            self.con.saveCourse(data)
        self.setCurrentIndex(0)

    def stuBtnClicked(self):
        self.stud = st.Students(self.data)
        self.stud.addBtn.clicked.connect(self.addBtnClicked)
        self.stud.backBtn.clicked.connect(self.backStuBtnClicked)
        self.stud.delBtn.clicked.connect(self.delBtnClicked)
        self.addWidget(self.stud)
        self.setCurrentWidget(self.stud)

    def attBtnClicked(self):
        att = self.con.getCourseAttendance(self.data['code'])
        newData = {}
        newData['code'] = att['code']
        newData['week'] = att['week']
        newData['count'] = att['count']
        newData['students'] = att['students']
        self.attend = at.Attendances(self.data, newData)
        self.attend.backBtn.clicked.connect(self.backAttBtnClicked)
        self.attend.attBtn.clicked.connect(self.attAttBtnClicked)
        self.addWidget(self.attend)
        self.setCurrentWidget(self.attend)

    def attAttBtnClicked(self):
        # Not defined
        pass

    def viewBtnClicked(self):
        self.setCurrentIndex(7)

    def addBtnClicked(self):
        data = self.con.getStudentIDS()
        i = 0
        newdata = []
        while i < len(data):
            count = self.data['students'].count(data[i])
            if not count > 0:
                newdata.append(data[i])
            i += 1
        self.stuList = st.StudentListForm(newdata)
        self.stuList.list.setSelectionMode(QListWidget.MultiSelection)
        self.stuList.list.itemDoubleClicked.connect(self.stuListItemDoubleClicked)
        self.stuList.addBtn.clicked.connect(self.addStuListBtnClicked)
        self.stuList.enroBtn.clicked.connect(self.enroStuListBtnClicked)
        self.stuList.backBtn.clicked.connect(self.backStuListBtnClicked)
        self.addWidget(self.stuList)
        self.setCurrentWidget(self.stuList)

    def stuListItemDoubleClicked(self, item):
        if not item.isSelected:
            item.setSelected(True)
        else:
            item.setSelected(False)

    def delBtnClicked(self):
        data = {}
        data['code'] = self.data['code']
        item = self.stud.list.currentItem().text()
        if self.data['students'] == []:
            return
        else:
            data['students'] = cp.copy(self.data['students'])
        self.data['students'].remove(item)
        self.con.updateCourseStudents(self.data, data)
        d = self.con.getCourse(self.data['code'])
        self.data['code'] = d['code']
        self.data['title'] = d['title']
        self.data['day'] = d['day']
        self.data['period'] = d['period']
        self.data['students'] = d['students']
        self.removeWidget(self.stud)
        self.stuBtnClicked()

    def addStuListBtnClicked(self):
        data = {}
        data['code'] = self.data['code']
        items = []
        items = self.stuList.list.selectedItems()
        if self.data['students'] == []:
            data['students'] = ''
        else:
            data['students'] = cp.copy(self.data['students'])
        for item in items:
            self.data['students'].append(item.text())
        self.con.updateCourseStudents(self.data, data)
        d = self.con.getCourse(self.data['code'])
        self.data['code'] = d['code']
        self.data['title'] = d['title']
        self.data['day'] = d['day']
        self.data['period'] = d['period']
        self.data['students'] = d['students']
        self.removeWidget(self.stud)
        self.removeWidget(self.stuList)
        self.stuBtnClicked()

    def enroStuListBtnClicked(self):
        self.studForm = st.StudentForm()
        self.studForm.backBtn.clicked.connect(self.backStuFormBtnClicked)
        self.studForm.addLFPBtn.clicked.connect(self.leftPrintBtnClicked)
        self.studForm.addRFPBtn.clicked.connect(self.rightPrintBtnClicked)
        self.studForm.nxtBtn.clicked.connect(self.nxtBtnClicked)
        self.addWidget(self.studForm)
        self.setCurrentWidget(self.studForm)

    def backStuListBtnClicked(self):
        self.removeWidget(self.stud)
        self.removeWidget(self.stuList)
        self.setCurrentWidget(self.course)

    def backAttBtnClicked(self):
        self.removeWidget(self.attend)
        self.setCurrentWidget(self.course)

    def backBtnClicked(self):
        self.setCurrentIndex(0)

    def backCouBtnClicked(self):
        self.removeWidget(self.course)
        self.setCurrentIndex(0)

    def backSelBtnClicked(self):
        self.removeWidget(self.select)
        self.setCurrentIndex(0)

    def backRegBtnClicked(self):
        self.removeWidget(self.regist)
        self.setCurrentIndex(0)

    def backStuBtnClicked(self):
        self.removeWidget(self.stud)
        self.setCurrentWidget(self.course)

    def backStuFormBtnClicked(self):
        self.removeWidget(self.stud)
        self.removeWidget(self.stuList)
        self.removeWidget(self.studForm)
        self.stuBtnClicked()

    # def backVewBtnClicked(self):
    #     self.setCurrentIndex(4)


    def nxtBtnClicked(self):
        data = {}
        if (len(self.con.getLeftPrint()) > 0 and len(self.con.getRightPrint()) > 0):
            data['name'] = self.studForm.nameLineEdit.text()
            data['matric'] = self.studForm.matricLineEdit.text()
            data['leftprint'] = self.con.getLeftPrint()
            data['rightprint'] = self.con.getRightPrint()
            datum = {}
            datum['code'] = self.data['code']
            self.studen = st.Student(data)
            if self.data['students'] == []:
                datum['students'] = ''
            else:
                datum['students'] = cp.copy(self.data['students'])
            self.data['students'].append(data['matric'])
            self.con.updateCourseStudents(self.data, datum)
            self.con.saveStudent(data)
            d = self.con.getCourse(self.data['code'])
            self.data['code'] = d['code']
            self.data['title'] = d['title']
            self.data['day'] = d['day']
            self.data['period'] = d['period']
            self.data['students'] = d['students']
            self.removeWidget(self.stud)
            self.removeWidget(self.studForm)
            self.stuBtnClicked()
        else:
            data['name'] = ''
            data['matric'] = ''
            data['leftprint'] = ''
            data['rightprint'] = ''
            self.studen = st.Student(data)


    def leftPrintBtnClicked(self):
        if (len(self.studForm.nameLineEdit.text()) > 6 and len(self.studForm.matricLineEdit.text()) > 13):
            self.con.enrollPrint('left')

    def rightPrintBtnClicked(self):
        if (len(self.studForm.nameLineEdit.text()) > 6 and len(self.studForm.matricLineEdit.text()) > 13):
            self.con.enrollPrint('right')

def main():
    app = QApplication(sys.argv)
    stack = StackedWidgetUI()
    stack.resize(420, 300)
    stack.show()
    # stack.showMaximized()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
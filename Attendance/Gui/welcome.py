from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class WelcomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel('Biometric Attendance Management System for Lecture and Examination ')
        self.regBtn = QPushButton('Register\nCourse')
        self.selBtn = QPushButton('Select\nCourse')
        hlayout = QHBoxLayout()
        vlayout = QVBoxLayout()

        self.title.setAlignment(Qt.AlignHCenter)
        self.title.setFont(QFont("Open Sans Regular", 20, QFont.Bold))
        self.title.setFixedWidth(self.width() * 0.75)
        self.title.setWordWrap(True)
        self.title.setStyleSheet("color: goldenrod")
        self.regBtn.setFont(QFont("Open Sans Regular", 20, QFont.Light))
        self.selBtn.setFont(QFont("Open Sans Regular", 20, QFont.Light))
        self.regBtn.setMinimumWidth(100)
        self.regBtn.setMinimumHeight(100)
        self.selBtn.setMinimumWidth(100)
        self.selBtn.setMinimumHeight(100)
        self.regBtn.setStyleSheet("background-color: goldenrod; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 18px; padding: 6px;")
        self.selBtn.setStyleSheet("background-color: goldenrod; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 18px; padding: 6px;")

        hlayout.addSpacing(30)
        hlayout.addWidget(self.regBtn)
        hlayout.addSpacing(60)
        hlayout.addWidget(self.selBtn)
        hlayout.addSpacing(30)
        vlayout.addSpacing(15)
        vlayout.addWidget(self.title)
        vlayout.addLayout(hlayout)
        vlayout.addSpacing(45)
        self.setLayout(vlayout)
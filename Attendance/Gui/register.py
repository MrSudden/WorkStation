
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QListWidgetItem, QLineEdit, QFormLayout
from PyQt5.QtCore import Qt

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
        hlay0 = QHBoxLayout()
        vlay = QVBoxLayout()

        self.title.setAlignment(Qt.AlignHCenter)
        self.title.setFont(QFont("Open Sans Regular", 16, QFont.Bold))
        self.title.setFixedWidth(self.width() * 0.75)
        self.title.setWordWrap(True)
        self.title.setStyleSheet("color: goldenrod")
        self.regBtn.setFont(QFont("Open Sans Regular", 12, QFont.Light))
        self.backBtn.setFont(QFont("Open Sans Regular", 12, QFont.Light))
        self.regBtn.setMinimumWidth(100)
        self.regBtn.setMaximumHeight(40)
        self.backBtn.setMinimumWidth(100)
        self.backBtn.setMaximumHeight(40)
        self.regBtn.setStyleSheet("background-color: goldenrod; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 12px; padding: 6px;")
        self.backBtn.setStyleSheet("background-color: goldenrod; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 12px; padding: 6px;")
        
        formLayout.addRow(self.tr('<font color="gold" size=10>&Course Title:</font>'), self.titleLineEdit)
        formLayout.addRow(self.tr('<font color="gold" size=10> &Course Code:</font>'), self.codeLineEdit)
        formLayout.addRow(self.tr('<font color="gold" size=10>    &Week Day:</font>'), self.dayLineEdit)
        formLayout.addRow(self.tr('<font color="gold" size=10>      &Period:</font>'), self.periodLineEdit)

        hlay.addSpacing(30)
        hlay.addWidget(self.backBtn)
        hlay.addSpacing(30)
        hlay.addWidget(self.regBtn)
        hlay.addSpacing(30)
        hlay0.addSpacing(30)
        hlay0.addLayout(formLayout)
        hlay0.addSpacing(30)
        vlay.addSpacing(15)
        vlay.addWidget(self.title)
        vlay.addLayout(hlay0)
        vlay.addSpacing(15)
        vlay.addLayout(hlay)
        vlay.addSpacing(30)
        self.setLayout(vlay)
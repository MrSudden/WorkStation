from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt

class SelectPage(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel('Select a course')
        self.list = QListWidget()
        self.backBtn = QPushButton('Back')
        self.selBtn = QPushButton('select')
        hlayout = QHBoxLayout()
        vlayout = QVBoxLayout()
        hlay = QHBoxLayout()

        self.title.setAlignment(Qt.AlignHCenter)
        self.title.setFont(QFont("Open Sans Regular", 18, QFont.Bold))
        self.title.setFixedWidth(self.width() * 0.75)
        self.title.setWordWrap(True)
        self.title.setStyleSheet("color: goldenrod")
        self.selBtn.setFont(QFont("Open Sans Regular", 12, QFont.Light))
        self.backBtn.setFont(QFont("Open Sans Regular", 12, QFont.Light))
        self.selBtn.setStyleSheet("background-color: goldenrod; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 12px; padding: 6px;")
        self.backBtn.setStyleSheet("background-color: goldenrod; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 12px; padding: 6px;")
        
        hlayout.addSpacing(30)
        hlayout.addWidget(self.backBtn)
        hlayout.addSpacing(60)
        hlayout.addWidget(self.selBtn)
        hlayout.addSpacing(30)
        hlay.addSpacing(30)
        hlay.addWidget(self.list)
        hlay.addSpacing(30)
        vlayout.addWidget(self.title)
        vlayout.addLayout(hlay)
        vlayout.addLayout(hlayout)
        self.setLayout(vlayout)
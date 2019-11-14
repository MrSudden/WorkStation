from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QLabel, QLineEdit, QFormLayout, QWidget, QListWidget, QListWidgetItem, QScrollArea
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class AddVoterForm1(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel('Fill in the voter\'s personal form:')
        self.nxtBtn = QPushButton('Next')
        self.backBtn = QPushButton('Back')

        self.nameLineEdit = QLineEdit()
        self.ageLineEdit = QLineEdit()
        self.lgaLineEdit = QLineEdit()
        self.stateLineEdit = QLineEdit()
        
        hlay = QHBoxLayout()
        vlay = QVBoxLayout()
        flay = QFormLayout()

        self.title.setAlignment(Qt.AlignHCenter)
        self.title.setFont(QFont("Open Sans Regular", 20, QFont.Bold))
        self.title.setFixedWidth(self.width() * 0.75)
        self.title.setStyleSheet('color: peru')
        self.title.setWordWrap(True)
        self.nxtBtn.setFont(QFont("Open Sans Regular", 16, QFont.Light))
        self.backBtn.setFont(QFont("Open Sans Regular", 16, QFont.Light))
        self.nxtBtn.setMinimumWidth(100)
        self.nxtBtn.setMinimumHeight(40)
        self.backBtn.setMinimumWidth(100)
        self.backBtn.setMinimumHeight(40)
        self.nxtBtn.setStyleSheet("background-color: navajowhite; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 14px; color: darkslategrey; padding: 6px;")
        self.backBtn.setStyleSheet("background-color: navajowhite; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 14px; color: darkslategrey; padding: 6px;")
        
        flay.addRow(self.tr('<font color="gold" size=12>  &Name:</font>'), self.nameLineEdit)
        flay.addRow(self.tr('<font color="gold" size=12>   &Age:</font>'), self.ageLineEdit)
        flay.addRow(self.tr('<font color="gold" size=12> &State:</font>'), self.stateLineEdit)
        flay.addRow(self.tr('<font color="gold" size=12>   &LGA:</font>'), self.lgaLineEdit)
        hlay.addSpacing(30)
        hlay.addWidget(self.backBtn)
        hlay.addSpacing(60)
        hlay.addWidget(self.nxtBtn)
        hlay.addSpacing(30)
        vlay.addSpacing(15)
        vlay.addLayout(hlay)
        vlay.addSpacing(15)
        vlay.addWidget(self.title)
        vlay.addLayout(flay)
        vlay.addSpacing(30)
        self.setLayout(vlay)

class AddVoterForm2(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel('Fill in the voter\'s station form:')
        self.nxtBtn = QPushButton('Next')
        self.backBtn = QPushButton('Back')

        staidLineEdit = QLineEdit()
        regstaCBox = QComboBox()
        lastpoolCBox = QComboBox()
        hlay = QHBoxLayout()
        vlay = QVBoxLayout()
        formLayout = QFormLayout()

        self.title.setAlignment(Qt.AlignHCenter)
        self.title.setFont(QFont("Open Sans Regular", 20, QFont.Bold))
        self.title.setFixedWidth(self.width() * 0.75)
        self.title.setStyleSheet('color: peru')
        self.title.setWordWrap(True)
        self.nxtBtn.setFont(QFont("Open Sans Regular", 16, QFont.Light))
        self.backBtn.setFont(QFont("Open Sans Regular", 16, QFont.Light))
        self.nxtBtn.setMinimumWidth(100)
        self.nxtBtn.setMinimumHeight(40)
        self.backBtn.setMinimumWidth(100)
        self.backBtn.setMinimumHeight(40)
        self.nxtBtn.setStyleSheet("background-color: navajowhite; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 14px; color: darkslategrey; padding: 6px;")
        self.backBtn.setStyleSheet("background-color: navajowhite; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 14px; color: darkslategrey; padding: 6px;")
        
        formLayout.addRow(self.tr('<font color="gold" size=12>&Station ID:</font>'), staidLineEdit)
        formLayout.addRow(self.tr('<font color="gold" size=12>       &Age:</font>'), regstaCBox)
        formLayout.addRow(self.tr('<font color="gold" size=12>     &State:</font>'), lastpoolCBox)
        hlay.addSpacing(30)
        hlay.addWidget(self.backBtn)
        hlay.addSpacing(60)
        hlay.addWidget(self.nxtBtn)
        hlay.addSpacing(30)
        vlay.addSpacing(15)
        vlay.addLayout(hlay)
        vlay.addSpacing(15)
        vlay.addWidget(self.title)
        vlay.addLayout(formLayout)
        vlay.addSpacing(30)
        self.setLayout(vlay)

class AddVoterForm3(QWidget):
    def __init__(self):
        super().__init__()
        self.nxtBtn = QPushButton('Next')
        self.backBtn = QPushButton('Back')
        self.addLIRBtn = QPushButton('Add')
        self.addRIRBtn = QPushButton('Add')
        self.addLFPBtn = QPushButton('Add')
        self.addRFPBtn = QPushButton('Add')
        self.statLIR = QLabel('Status: NULL')
        self.statRIR = QLabel('Status: NULL')
        self.statLFP = QLabel('Status: NULL')
        self.statRFP = QLabel('Status: NULL')
        self.title = QLabel('Fill in the voter\'s Biometric form:')
        self.left = QLabel('Left')
        self.right = QLabel('Right')
        self.iris = QLabel('Iris')
        self.fingerprint = QLabel('Fingerprint')
        # self.rfid = QLabel('Voter\'s Card')

        hlay = QHBoxLayout()
        hlay0 = QHBoxLayout()
        hlay1 = QHBoxLayout()
        hlay2 = QHBoxLayout()
        vlay2 = QVBoxLayout()
        vlay3 = QVBoxLayout()
        vlay4 = QVBoxLayout()
        vlay5 = QVBoxLayout()
        vlay = QVBoxLayout()
        vlay0 = QVBoxLayout()
        vlay1 = QVBoxLayout()

        self.title.setAlignment(Qt.AlignHCenter)
        self.title.setFont(QFont("Open Sans Regular", 16, QFont.Bold))
        self.title.setFixedWidth(self.width() * 0.675)
        self.title.setStyleSheet('color: peru')
        self.title.setWordWrap(True)
        self.addLIRBtn.setFont(QFont("Open Sans Regular", 20, QFont.Light))
        self.addRIRBtn.setFont(QFont("Open Sans Regular", 20, QFont.Light))
        self.addLFPBtn.setFont(QFont("Open Sans Regular", 20, QFont.Light))
        self.addRFPBtn.setFont(QFont("Open Sans Regular", 20, QFont.Light))
        self.nxtBtn.setFont(QFont("Open Sans Regular", 20, QFont.Light))
        self.backBtn.setFont(QFont("Open Sans Regular", 20, QFont.Light))
        self.left.setFont(QFont("Open Sans Regular", 10, QFont.Bold))
        self.left.setStyleSheet('color: navajowhite')
        self.right.setFont(QFont("Open Sans Regular", 10, QFont.Bold))
        self.right.setStyleSheet('color: navajowhite')
        self.iris.setFont(QFont("Open Sans Regular", 10, QFont.Bold))
        self.iris.setStyleSheet('color: navajowhite')
        self.fingerprint.setFont(QFont("Open Sans Regular", 10, QFont.Bold))
        self.fingerprint.setStyleSheet('color: navajowhite')
        self.statLFP.setFont(QFont("Open Sans Regular", 10, QFont.Bold))
        self.statLFP.setStyleSheet('color: navajowhite')
        self.statRFP.setFont(QFont("Open Sans Regular", 10, QFont.Bold))
        self.statRFP.setStyleSheet('color: navajowhite')
        self.statRIR.setFont(QFont("Open Sans Regular", 10, QFont.Bold))
        self.statRIR.setStyleSheet('color: navajowhite')
        self.statLIR.setFont(QFont("Open Sans Regular", 10, QFont.Bold))
        self.statLIR.setStyleSheet('color: navajowhite')

        self.nxtBtn.setMinimumWidth(100)
        self.nxtBtn.setMinimumHeight(40)
        self.backBtn.setMinimumWidth(100)
        self.backBtn.setMinimumHeight(40)
        self.addLIRBtn.setMaximumWidth(50)
        self.addLIRBtn.setMaximumHeight(40)
        self.addRIRBtn.setMaximumWidth(50)
        self.addRIRBtn.setMaximumHeight(40)
        self.addRFPBtn.setMaximumWidth(50)
        self.addRFPBtn.setMaximumHeight(40)
        self.addLFPBtn.setMaximumWidth(50)
        self.addLFPBtn.setMaximumHeight(40)
        self.backBtn.setStyleSheet("background-color: navajowhite; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 14px; color: darkslategrey; padding: 6px;")
        self.nxtBtn.setStyleSheet("background-color: navajowhite; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 14px; color: darkslategrey; padding: 6px;")
        self.addRIRBtn.setStyleSheet("background-color: navajowhite; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 14px; color: darkslategrey; padding: 6px;")
        self.addLIRBtn.setStyleSheet("background-color: navajowhite; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 14px; color: darkslategrey; padding: 6px;")
        self.addLFPBtn.setStyleSheet("background-color: navajowhite; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 14px; color: darkslategrey; padding: 6px;")
        self.addRFPBtn.setStyleSheet("background-color: navajowhite; border-style: outset;"
                " border-width: 1px; border-radius: 10px; border-color: gold;"
                " font: bold 14px; color: darkslategrey; padding: 6px;")
        
        hlay.addSpacing(30)
        hlay.addWidget(self.backBtn)
        hlay.addSpacing(60)
        hlay.addWidget(self.nxtBtn)
        hlay.addSpacing(30)

        vlay2.addWidget(self.left)
        vlay2.addWidget(self.statLFP)
        vlay2.addWidget(self.addLFPBtn)

        vlay3.addWidget(self.right)
        vlay3.addWidget(self.statRFP)
        vlay3.addWidget(self.addRFPBtn)

        vlay0.addWidget(self.fingerprint)
        hlay0.addLayout(vlay2)
        hlay0.addLayout(vlay3)
        vlay0.addLayout(hlay0)

        vlay4.addWidget(self.left)
        vlay4.addWidget(self.statLIR)
        vlay4.addWidget(self.addLIRBtn)

        vlay5.addWidget(self.right)
        vlay5.addWidget(self.statRIR)
        vlay5.addWidget(self.addRIRBtn)

        vlay1.addWidget(self.iris)
        hlay1.addLayout(vlay4)
        hlay1.addLayout(vlay5)
        vlay1.addLayout(hlay1)

        hlay2.addSpacing(30)
        hlay2.addLayout(vlay0)
        hlay2.addSpacing(30)
        hlay2.addLayout(vlay1)
        hlay2.addSpacing(30)
        vlay.addSpacing(15)
        vlay.addLayout(hlay)
        vlay.addSpacing(15)
        vlay.addWidget(self.title)
        vlay.addLayout(hlay2)
        vlay.addSpacing(30)
        self.setLayout(vlay)

class VoterPage(QWidget):
    def __init__(self):
        super().__init__()
        self.name = QLabel('Dumm Dummy')
        self.id = QLabel('Dummy')
        self.age = QLabel('123')
        self.state = QLabel('Dummy State')
        self.lga = QLabel('Kpakungu')
        self.statid = QLabel('STAD123')
        self.biom = QLabel('Biometrics:')
        self.biostat = QLabel('False')
        self.editBtn = QPushButton('Edit')
        self.backBtn = QPushButton('Back')

        vlay = QVBoxLayout()
        hlay0 = QHBoxLayout()
        hlay1 = QHBoxLayout()
        hlay2 = QHBoxLayout()
        hlay3 = QHBoxLayout()

        hlay0.addWidget(self.backBtn)
        hlay0.addSpacing(50)
        hlay0.addWidget(self.editBtn)
        hlay1.addWidget(self.id)
        hlay1.addSpacing(25)
        hlay1.addWidget(self.age)
        hlay2.addWidget(self.state)
        hlay2.addSpacing(25)
        hlay2.addWidget(self.lga)
        hlay3.addWidget(self.biom)
        hlay3.addWidget(self.biostat)
        vlay.addSpacing(15)
        vlay.addLayout(hlay0)
        vlay.addWidget(self.name)
        vlay.addLayout(hlay1)
        vlay.addLayout(hlay2)
        vlay.addLayout(hlay3)
        vlay.addSpacing(15)
        self.setLayout(vlay)

class DeleteVoters(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel('View/Edit/Delete Voters')
        self.info = QLabel('Double Click to Delete a Voter!')
        self.list = QListWidget()
        self.backBtn = QPushButton('Back')

        self.list.resize(256, 192)

        vlay = QVBoxLayout()
        
        vlay.addSpacing(15)
        vlay.addWidget(self.backBtn)
        vlay.addWidget(self.title)
        vlay.addWidget(self.info)
        vlay.addWidget(self.list)
        vlay.addSpacing(20)
        self.setLayout(vlay)
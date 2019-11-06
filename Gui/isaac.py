import sys
from PyQt5.QtGui import QBrush, QPixmap, QPalette, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QComboBox, QLabel, QLineEdit, QFormLayout
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton,  QListWidget, QListWidgetItem, QScrollArea
from PyQt5.QtCore import Qt, pyqtSignal

class ManagerPage(QWidget):

    def __init__(self):
        super().__init__()
        self.title = QLabel('Voting System using RFID, Fingerprint and Iris')
        self.voteBtn = QPushButton('Voter\nManager')
        self.elecBtn = QPushButton('Election\nManager')
        hlayout = QHBoxLayout()
        vlayout = QVBoxLayout()
        vlayout1 = QVBoxLayout()

        self.title.setAlignment(Qt.AlignHCenter)
        self.title.setFont(QFont("Open Sans Regular", 24, QFont.Bold))
        self.title.setFixedWidth(self.width() * 0.75)
        self.title.setWordWrap(True)
        self.voteBtn.setFont(QFont("Open Sans Regular", 20, QFont.Light))
        self.elecBtn.setFont(QFont("Open Sans Regular", 20, QFont.Light))

        self.voteBtn.setMinimumWidth(160)
        self.voteBtn.setMinimumHeight(160)
        self.elecBtn.setMinimumWidth(160)
        self.elecBtn.setMinimumHeight(160)
        hlayout.addWidget(self.voteBtn)
        hlayout.addWidget(self.elecBtn)
        vlayout1.addWidget(self.title)
        vlayout.addLayout(vlayout1)
        vlayout.addLayout(hlayout)
        vlayout.addSpacing(15)
        self.setLayout(vlayout)

class VotersPage(QWidget):

    def __init__(self):
        super().__init__()
        self.title = QLabel('Select Activity')
        self.addBtn = QPushButton('Add\nVoter')
        self.vewedBtn = QPushButton('View/Edit\nVoter')
        self.delBtn = QPushButton('Delete\nVoter')
        self.backBtn = QPushButton('Back')
        
        hlay = QHBoxLayout()
        hlayout = QHBoxLayout()
        vlay = QVBoxLayout()

        self.title.setAlignment(Qt.AlignHCenter)
        self.title.setFont(QFont("Open Sans Regular", 20, QFont.Bold))
        self.title.setFixedWidth(self.width() * 0.75)
        self.title.setWordWrap(True)
        self.addBtn.setFont(QFont("Open Sans Regular", 20, QFont.Light))
        self.vewedBtn.setFont(QFont("Open Sans Regular", 20, QFont.Light))
        self.delBtn.setFont(QFont("Open Sans Regular", 20, QFont.Light))
        self.backBtn.setFont(QFont("Open Sans Regular", 16, QFont.Light))
        self.addBtn.setMinimumWidth(160)
        self.addBtn.setMinimumHeight(160)
        self.vewedBtn.setMinimumWidth(160)
        self.vewedBtn.setMinimumHeight(160)
        self.delBtn.setMinimumWidth(160)
        self.delBtn.setMinimumHeight(160)
        self.backBtn.setFixedWidth(160)
        self.backBtn.setMinimumHeight(40)
        
        hlay.addWidget(self.addBtn)
        hlay.addWidget(self.vewedBtn)
        hlay.addWidget(self.delBtn)
        hlayout.addWidget(self.backBtn)
        vlay.addLayout(hlayout)
        vlay.addSpacing(12.5)
        vlay.addWidget(self.title)
        vlay.addLayout(hlay)
        vlay.addSpacing(25)
        self.setLayout(vlay)
        
class ElectionPage(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel('Select Activity')
        self.parBtn = QPushButton('Party\nManager')
        self.eleBtn = QPushButton('Election\nManager')
        self.backBtn = QPushButton('Back')

        hlay = QHBoxLayout()
        hlayout = QHBoxLayout()
        vlay = QVBoxLayout()

        self.title.setAlignment(Qt.AlignHCenter)
        self.title.setFont(QFont("Open Sans Regular", 20, QFont.Bold))
        self.title.setFixedWidth(self.width() * 0.75)
        self.title.setWordWrap(True)
        self.parBtn.setFont(QFont("Open Sans Regular", 20, QFont.Light))
        self.eleBtn.setFont(QFont("Open Sans Regular", 20, QFont.Light))
        self.backBtn.setFont(QFont("Open Sans Regular", 16, QFont.Light))
        self.parBtn.setMinimumWidth(160)
        self.parBtn.setMinimumHeight(160)
        self.eleBtn.setMinimumWidth(160)
        self.eleBtn.setMinimumHeight(160)
        self.backBtn.setFixedWidth(160)
        self.backBtn.setMinimumHeight(40)

        hlay.addWidget(self.parBtn)
        hlay.addWidget(self.eleBtn)
        hlayout.addWidget(self.backBtn)
        vlay.addLayout(hlayout)
        vlay.addSpacing(12.5)
        vlay.addWidget(self.title)
        vlay.addLayout(hlay)
        vlay.addSpacing(25)
        self.setLayout(vlay)

class PartyPage(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel('Parties')
        self.backBtn = QPushButton('Back')
        self.procBtn = QPushButton('Create')
        self.list = QListWidget()

        l = ["PDP", "APC", "APNN"]
        i = 0
        while(i < len(l)):
            QListWidgetItem(self.tr(l[i]), self.list)
            i += 1

        hlay = QHBoxLayout()
        vlay = QVBoxLayout()

        self.title.setAlignment(Qt.AlignHCenter)
        self.title.setFont(QFont("Open Sans Regular", 20, QFont.Bold))
        self.title.setFixedWidth(self.width() * 0.75)
        self.title.setWordWrap(True)
        self.procBtn.setFont(QFont("Open Sans Regular", 16, QFont.Light))
        self.backBtn.setFont(QFont("Open Sans Regular", 16, QFont.Light))
        self.procBtn.setFixedWidth(160)
        self.procBtn.setMinimumHeight(40)
        self.backBtn.setFixedWidth(160)
        self.backBtn.setMinimumHeight(40)

        hlay.addWidget(self.backBtn)
        hlay.addSpacing(25)
        hlay.addWidget(self.procBtn)
        vlay.addLayout(hlay)
        vlay.addWidget(self.title)
        vlay.addWidget(self.list)
        vlay.addSpacing(25)
        self.setLayout(vlay)

class PartyForm1(QWidget):
    def __init__(self):
        super().__init__()
        self.backBtn = QPushButton('Back')
        self.nxtBtn = QPushButton('Next')
        self.title = QLabel('Fill form for ')
        self.type = QLabel('Dummy')
        self.item1 = ''
        self.item2 = ''
        self.item3 = ''
        self.item4 = ''

        self.item1LineEdit = QLineEdit()
        self.item2LineEdit = QLineEdit()
        self.item3LineEdit = QLineEdit()
        self.item4LineEdit = QLineEdit()

        flay = QFormLayout()
        hlay0 = QHBoxLayout()
        hlay1 = QHBoxLayout()
        vlay = QVBoxLayout()

        hlay0.addWidget(self.backBtn)
        hlay0.addSpacing(15)
        hlay0.addWidget(self.nxtBtn)
        hlay1.addWidget(self.title)
        hlay1.addWidget(self.type)
        flay.addRow(self.tr(self.item1), self.item1LineEdit)
        flay.addRow(self.tr(self.item2), self.item2LineEdit)
        flay.addRow(self.tr(self.item3), self.item3LineEdit)
        flay.addRow(self.tr(self.item4), self.item4LineEdit)
        vlay.addSpacing(10)
        vlay.addLayout(hlay0)
        vlay.addLayout(hlay1)
        vlay.addLayout(flay)
        vlay.addSpacing(10)
        self.setLayout(vlay)

class PartyForm2(QWidget):
    def __init__(self):
        super().__init__()
        self.backBtn = QPushButton('Back')
        self.nxtBtn = QPushButton('Next')
        self.title = QLabel('Fill form for ')
        self.type = QLabel('Dummy')
        self.item1 = ''
        self.item2 = ''

        self.item1LineEdit = QLineEdit()
        self.item2LineEdit = QLineEdit()

        flay = QFormLayout()
        hlay0 = QHBoxLayout()
        hlay1 = QHBoxLayout()
        vlay = QVBoxLayout()

        hlay0.addWidget(self.backBtn)
        hlay0.addSpacing(15)
        hlay0.addWidget(self.nxtBtn)
        hlay1.addWidget(self.title)
        hlay1.addWidget(self.type)
        flay.addRow(self.tr(self.item1), self.item1LineEdit)
        flay.addRow(self.tr(self.item2), self.item2LineEdit)
        vlay.addSpacing(10)
        vlay.addLayout(hlay0)
        vlay.addLayout(hlay1)
        vlay.addLayout(flay)
        vlay.addSpacing(10)
        self.setLayout(vlay)

class Election():
    def __init__(self):
        self.__title = ''
        self.__id = ''
        self.__date = ''
        self.__datetaken = ''
        self.__start = ''
        self.__end = ''
        self.__parties = []
        self.__result = {}
        self.__station = ''
        self.__type = ''
        self.__commenced = False

    def setTitle(self, name):
        self.__title = name

    def getTitle(self):
        return self.__title

    def setID(self, name):
        self.__id = name

    def getID(self):
        return self.__id

    def setType(self, name):
        self.__type = name

    def getType(self):
        return self.__type

    def setStation(self, name):
        self.__station = name

    def getStation(self):
        return self.__station

    def setStart(self, name):
        self.__start = name

    def getStart(self):
        return self.__start

    def setEnd(self, name):
        self.__end = name

    def getEnd(self):
        return self.__end

    def setDate(self, name):
        self.__date = name

    def getDate(self):
        return self.__date

    def setDateTaken(self, name):
        self.__dateTaken = name

    def getDateTaken(self):
        return self.__dateTaken

    def setParties(self, name):
        self.__parties = name

    def getParties(self):
        return self.__parties

    def setResult(self, name):
        self.__result = name

    def getResult(self):
        return self.__result

class Elections(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel('Dummy')
        self.backBtn = QPushButton('Back')
        self.crtBtn = QPushButton('Create')
        self.list = QListWidget()
        self.elections = []

        hlay0 = QHBoxLayout()
        vlay = QVBoxLayout()

        hlay0.addWidget(self.backBtn)
        hlay0.addSpacing(15)
        hlay0.addWidget(self.crtBtn)
        vlay.addSpacing(10)
        vlay.addLayout(hlay0)
        vlay.addWidget(self.list)
        vlay.addSpacing(10)
        self.setLayout(vlay)

class ElectionForm(QWidget):
    def __init__(self):
        super().__init__()
        self.backBtn = QPushButton('Back')
        self.crtBtn = QPushButton('Create')
        self._election = Election()
        self.idLabel = QLabel('&ID: ')
        self.typeLabel = QLabel('&Type: ')
        self.dateLabel = QLabel('&Date: ')
        self.stationLabel = QLabel('&Station: ')
        self.startLabel = QLabel('&Start Period: ')
        self.titleLabel = QLabel('&Title: ')
        self.endLabel = QLabel('&End Period: ')
        self.titleLineEdit = QLineEdit()
        self.idLineEdit = QLineEdit()
        self.startLineEdit = QLineEdit()
        self.stationLineEdit = QLineEdit()
        self.endLineEdit = QLineEdit()
        self.dateLineEdit = QLineEdit()
        self.typeLineEdit = QLineEdit()

        hlay0 = QHBoxLayout()
        hlay1 = QHBoxLayout()
        hlay2 = QHBoxLayout()
        hlay3 = QHBoxLayout()
        hlay4 = QHBoxLayout()
        hlay5 = QHBoxLayout()
        hlay6 = QHBoxLayout()
        hlay7 = QHBoxLayout()
        hlay8 = QHBoxLayout()
        hlay9 = QHBoxLayout()
        vlay = QVBoxLayout()

        hlay0.addWidget(self.backBtn)
        hlay0.addSpacing(15)
        hlay0.addWidget(self.nxtBtn)
        hlay3.addWidget(self.typeLabel)
        hlay3.addWidget(self.typeLineEdit)
        hlay4.addWidget(self.titleLabel)
        hlay4.addWidget(self.titleLineEdit)
        hlay5.addWidget(self.idLabel)
        hlay5.addWidget(self.idLineEdit)
        hlay6.addWidget(self.stationLabel)
        hlay6.addWidget(self.stationLineEdit)
        hlay7.addWidget(self.startLabel)
        hlay7.addWidget(self.startLineEdit)
        hlay8.addWidget(self.dateLabel)
        hlay8.addWidget(self.dateLineEdit)
        hlay9.addWidget(self.endLabel)
        hlay9.addWidget(self.endLineEdit)
        hlay3.addLayout(hlay7)
        hlay3.addSpacing(10)
        hlay3.addLayout(hlay9)
        hlay1.addLayout(hlay3)
        hlay1.addSpacing(10)
        hlay1.addLayout(hlay8)
        hlay2.addLayout(hlay5)
        hlay2.addSpacing(10)
        hlay2.addLayout(hlay6)
        vlay.addSpacing(10)
        vlay.addLayout(hlay0)
        vlay.addWidget(self.title)
        vlay.addLayout(hlay1)
        vlay.addLayout(hlay2)
        vlay.addLayout(hlay3)
        vlay.addSpacing(10)
        self.setLayout(vlay)

class NewElection(QWidget):
    def __init__(self):
        super().__init__()
        self.backBtn = QPushButton('Back')
        self.addBtn = QPushButton('Add Party')
        self.startBtn = QPushButton('Start Attendance')
        self.title = QLabel('Dummy')
        self._election = Election()
        self.type = QLabel('Dummy')
        self.date = QLabel('Dummy')
        self.station = QLabel('Dummy')
        self.start = QLabel('Dummy')
        self.list = QListWidget()

        hlay0 = QHBoxLayout()
        hlay1 = QHBoxLayout()
        hlay2 = QHBoxLayout()
        vlay0 = QHBoxLayout()
        vlay1 = QHBoxLayout()

        hlay2.addWidget(self.backBtn)
        hlay2.addSpacing(12)
        hlay2.addWidget(self.addBtn)
        hlay2.addWidget(self.startBtn)
        hlay0.addWidget(self.date)
        hlay0.addSpacing(15)
        hlay0.addWidget(self.start)
        hlay1.addWidget(self.station)
        hlay1.addSpacing(15)
        hlay1.addWidget(self.type)
        vlay0.addWidget(self.title)
        vlay0.addLayout(hlay0)
        vlay0.addLayout(hlay1)
        vlay1.addSpacing(10)
        vlay1.addLayout(hlay2)
        vlay1.addLayout(vlay0)
        vlay1.addWidget(self.list)
        self.setLayout(vlay1)

class AddElectionParty(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel('Dummy')
        self.list = QListWidget()
        self._election = Election()
        self.backBtn = QPushButton('Back')
        self.addBtn = QPushButton('Add Party')
        self.ls = []

        vlay = QVBoxLayout()
        hlay = QHBoxLayout()

        hlay.addWidget(self.backBtn)
        hlay.addSpacing(15)
        hlay.addWidget(self.addBtn)
        vlay.addSpacing(15)
        vlay.addLayout(hlay)
        vlay.addWidget(self.list)
        vlay.addSpacing(15)
        self.setLayout(vlay)

class VotePage(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel('Dummy')
        self.info = QLabel('Dummy')
        self.backBtn = QPushButton('Back')
        self.begBtn = QPushButton('Start Voting\nSession')
        
        vlay = QVBoxLayout()
        vlay.addSpacing(10)
        vlay.addWidget(self.backBtn)
        vlay.addWidget(self.title)
        vlay.addWidget(self.info)
        vlay.addWidget(self.begBtn)
        vlay.addSpacing(10)
        self.setLayout(vlay)

class GeneralVote(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel('Dummy')
        self.info = QLabel('Dummy')
        self._voter = Voter()
        self._election = Election()
        self.pres = QLabel('President')
        self.vpres = QLabel('Vice President')
        self.sent = QLabel('Senator')
        self.dsent = QLabel('Deputy Senator')
        self.clerk = QLabel('Clerk')
        self.whip = QLabel('Chief Whip')
        self.speak = QLabel('Speaker')
        self.dspeak = QLabel('Deputy Speaker')
        self.govn = QLabel('Governor')
        self.dgovn = QLabel('Deputy Governor')
        self.scroll = QScrollArea()
        self.backBtn = QPushButton('Back')
        self.nxtBtn = QPushButton('Next')
        self.select = QLabel('Selection: ')
        self.options = True

        self.scroll.resize(360, 240)

        vlay = QVBoxLayout()
        hlay = QHBoxLayout()
        
        hlay.addWidget(self.backBtn)
        hlay.addSpacing(15)
        hlay.addWidget(self.nxtBtn)
        vlay.addSpacing(15)
        vlay.addWidget(hlay)
        vlay.addWidget(self.title)
        vlay.addWidget(self.info)
        vlay.addWidget(self.scroll)
        self.setLayout(vlay)

class FinishVote(QWidget):
    def __init__(self):
        super().__init__()
        self.info = QLabel('Ensure that you have select your heartfelt, if so\ncomplete the voting session by clicking the \n\'Vote\' button')
        self.backBtn = QPushButton('Back')
        self.voteBtn = QPushButton('Vote')
        self._voter = Voter()
        self.pres = QLabel('President')
        self.vpres = QLabel('Vice President')
        self.sent = QLabel('Senator')
        self.dsent = QLabel('Deputy Senator')
        self.clerk = QLabel('Clerk')
        self.whip = QLabel('Chief Whip')
        self.speak = QLabel('Speaker')
        self.dspeak = QLabel('Deputy Speaker')
        self.govn = QLabel('Governor')
        self.dgovn = QLabel('Deputy Governor')
        self.select = QLabel('Your selection >>>')
        self.type = ''
        self.pres = QLabel('Dummy')
        self.vpres = QLabel('Dummy')
        self.sent = QLabel('Dummy')
        self.dsent = QLabel('Dummy')
        self.clerk = QLabel('Dummy')
        self.whip = QLabel('Dummy')
        self.govn = QLabel('Dummy')
        self.dgovn = QLabel('Dummy')

        hlay = QHBoxLayout()
        vlay = QVBoxLayout()

        hlay.addWidget(self.backBtn)
        hlay.addSpacing(15)
        hlay.addWidget(self.voteBtn)
        vlay.addLayout(hlay)
        vlay.addWidget(self.info)
        vlay.addSpacing(10)

class EndElection(QWidget):
    def __init__(self):
        super().__init__()
        self.doneBtn = QPushButton('Done')
        self.info = QLabel('Election Finish')
        self.total = QLabel('Total voters: ')
        self.nums = QLabel('00')
        self.res = QLabel('Result >>>')
        self.list = QListWidget()

        vlay = QVBoxLayout()
        hlay = QHBoxLayout()

        hlay.addWidget(self.total)
        hlay.addWidget(self.nums)
        vlay.addSpacing(10)
        vlay.addWidget(self.doneBtn)
        vlay.addWidget(self.info)
        vlay.addLayout(hlay)
        vlay.addWidget(self.res)
        vlay.addWidget(self.list)
        vlay.addSpacing(10)
        self.setLayout(vlay)

class Voter():
    def __init__(self):
        self.__name = ''
        self.__age = ''
        self.__lga = ''
        self.__state = ''
        self.__staid = ''
        self.__regstat = ''
        self.__lastpooling = ''
        self.__rfid = ''
        self.__rightprint = ''
        self.__leftprint = ''
        self.__leftiris = ''
        self.__rightiris = ''
        self.__selection = {
            "president": "Dummy",
            "govern": "Dummy",
            "senator": "Dummy",
            "houseofreps": "Dummy"
        }

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self, name):
        self.__age = name

    def getAge(self):
        return self.__age

    def setLGA(self, name):
        self.__lga = name

    def getLGA(self):
        return self.__lga

    def setState(self, name):
        self.__state = name

    def getState(self):
        return self.__state

    def setStaID(self, name):
        self.__staid = name

    def getStaID(self):
        return self.__staid

    def setRegStat(self, name):
        self.__regstat = name

    def getRegStat(self):
        return self.__regstat

    def setLastPooling(self, name):
        self.__lastpooling = name

    def getLastPooling(self):
        return self.__lastpooling

    def setRfid(self, name):
        self.__rfid = name

    def getRfid(self):
        return self.__rfid

    def setLeftPrint(self, name):
        self.__leftprint = name

    def getLeftPrint(self):
        return self.__leftprint

    def setRightPrint(self, name):
        self.__rightprint = name

    def getRightPrint(self):
        return self.__rightprint

    def setLeftIris(self, naame):
        self.__leftiris = naame

    def getLeftIris(self):
        return self.__leftiris

    def setRightIris(self, name):
        self.__rightiris = name

    def getRightIris(self):
        return self.__rightiris

    def setSelection(self, name):
        self.__selection = name

    def getSelection(self):
        return self.__selection

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
        self.title.setWordWrap(True)
        self.nxtBtn.setFont(QFont("Open Sans Regular", 16, QFont.Light))
        self.backBtn.setFont(QFont("Open Sans Regular", 16, QFont.Light))
        self.nxtBtn.setFixedWidth(160)
        self.nxtBtn.setMinimumHeight(40)
        self.backBtn.setFixedWidth(160)
        self.backBtn.setMinimumHeight(40)
        
        flay.addRow(self.tr('  &Name:'), self.nameLineEdit)
        flay.addRow(self.tr('   &Age:'), self.ageLineEdit)
        flay.addRow(self.tr(' &State:'), self.stateLineEdit)
        flay.addRow(self.tr('   &LGA:'), self.lgaLineEdit)
        hlay.addWidget(self.backBtn)
        hlay.addSpacing(50)
        hlay.addWidget(self.nxtBtn)
        vlay.addLayout(hlay)
        vlay.addSpacing(25)
        vlay.addWidget(self.title)
        vlay.addLayout(flay)
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
        
        formLayout.addRow(self.tr('&Station ID:'), staidLineEdit)
        formLayout.addRow(self.tr('       &Age:'), regstaCBox)
        formLayout.addRow(self.tr('     &State:'), lastpoolCBox)
        hlay.addWidget(self.backBtn)
        hlay.addSpacing(50)
        hlay.addWidget(self.nxtBtn)
        vlay.addLayout(hlay)
        vlay.addSpacing(25)
        vlay.addWidget(self.title)
        vlay.addLayout(formLayout)
        self.setLayout(vlay)

class AddVoterForm3():
    def __init__(self):
        super().__init__()
        self.nxtBtn = QPushButton('Next')
        self.backBtn = QPushButton('Back')
        self.title = ''
        self.left = QLabel('Left')
        self.right = QLabel('Right')
        self.iris = QLabel('Iris')
        self.fingerprint = QLabel('Fingerprint')
        self.rfid = QLabel('Voter\'s Card')
        

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
        self.title = QLabel('Dummy Dummy')
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

class Party(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel('Dummy')
        self._presidential = PresidentialCrew()
        self._governors = GovernorCrew()
        self._senators = SenatorialCrew()
        self._houseofreps = HouseOfRepsCrew()
        self.backBtn = QPushButton('Back')
        self.pres = QLabel('President')
        self.vpres = QLabel('Vice President')
        self.sent = QLabel('Senator')
        self.dsent = QLabel('Deputy Senator')
        self.clerk = QLabel('Clerk')
        self.whip = QLabel('Chief Whip')
        self.speak = QLabel('Speaker')
        self.dspeak = QLabel('Deputy Speaker')
        self.govn = QLabel('Governor')
        self.dgovn = QLabel('Deputy Governor')

        vlay0 = QVBoxLayout()
        vlay1 = QVBoxLayout()
        vlay2 = QVBoxLayout()
        vlay3 = QVBoxLayout()
        vlay4 = QVBoxLayout()
        vlay5 = QVBoxLayout()
        vlay6 = QVBoxLayout()
        hlay = QHBoxLayout()

        vlay3.addWidget(QLabel('Presidential'))
        vlay3.addWidget(self.pres)
        vlay3.addWidget(QLabel(self._presidential.getPres()))
        vlay3.addWidget(self.vpres)
        vlay3.addWidget(QLabel(self._presidential.getVPres()))
        vlay3.addWidget(self.sent)
        vlay3.addWidget(QLabel(self._senators.getSent()))
        vlay4.addWidget(QLabel('Senatorial'))
        vlay4.addWidget(self.sent)
        vlay4.addWidget(QLabel(self._senators.getSent()))
        vlay4.addWidget(self.dsent)
        vlay4.addWidget(QLabel(self._senators.getDSent()))
        vlay4.addWidget(self.clerk)
        vlay4.addWidget(QLabel(self._senators.getClerk()))
        vlay4.addWidget(self.whip)
        vlay4.addWidget(QLabel(self._senators.getWhip()))
        vlay5.addWidget(QLabel('House of Reps'))
        vlay5.addWidget(self.speak)
        vlay5.addWidget(QLabel(self._houseofreps.getSpeak()))
        vlay5.addWidget(self.dspeak)
        vlay5.addWidget(QLabel(self._houseofreps.getDSpeak()))
        vlay5.addWidget(self.clerk)
        vlay5.addWidget(QLabel(self._houseofreps.getClerk()))
        vlay5.addWidget(self.whip)
        vlay5.addWidget(QLabel(self._houseofreps.getWhip()))
        vlay6.addWidget(QLabel('Governors'))
        vlay6.addWidget(self.govn)
        vlay6.addWidget(QLabel(self._governors.getGovr()))
        vlay6.addWidget(self.dgovn)
        vlay6.addWidget(QLabel(self._governors.getDGovr()))
        vlay1.addLayout(vlay3)
        vlay1.addSpacing(10)
        vlay1.addLayout(vlay5)
        vlay2.addLayout(vlay4)
        vlay2.addSpacing(10)
        vlay2.addLayout(vlay6)
        hlay.addLayout(vlay1)
        hlay.addSpacing(10)
        hlay.addLayout(vlay2)
        vlay0.addWidget(self.backBtn)
        vlay0.addWidget(self.title)
        vlay0.addLayout(hlay)
        self.setLayout(vlay0)

class PresidentialCrew():
    def __init__(self):
        self.__pres = 'Dummy Dummy'
        self.__vpres = 'Dummy Dummy'
        self.__sent = 'Dummy Dummy'

    def setPres(self, name):
        self.__pres = name

    def getPres(self):
        return self.__pres

    def setVPres(self, name):
        self.__vpres = name

    def getVPres(self):
        return self.__vpres

    def setSent(self, name):
        self.__sent = name

    def getSent(self):
        return self.__sent

class SenatorialCrew():
    def __init__(self):
        self.__sent = 'Dummy Dummy'
        self.__dsent = 'Dummy Dummy'
        self.__clerk = 'Dummy Dummy'
        self.__whip = 'Dummy Dummy'

    def setSent(self, name):
        self.__sent = name

    def getSent(self):
        return self.__sent

    def setdsent(self, name):
        self.__dsent = name

    def getDSent(self):
        return self.__dsent

    def setClerk(self, name):
        self.__clerk = name

    def getClerk(self):
        return self.__clerk

    def setWhip(self, name):
        self.__Whip = name

    def getWhip(self):
        return self.__whip

class GovernorCrew():
    def __init__(self):
        self.__govr = 'Dummy Dummy'
        self.__dgovr = 'Dummy Dummy'
    
    def setGovr(self, name):
        self.__govr = name

    def getGovr(self):
        return self.__govr
    
    def setDGovr(self, name):
        self.__dgovr = name

    def getDGovr(self):
        return self.__dgovr

class HouseOfRepsCrew():
    def __init__(self):
        self.__speak = 'Dummy Dummy'
        self.__dspeak = 'Dummy Dummy'
        self.__clerk = 'Dummy Dummy'
        self.__whip = 'Dummy Dummy'
        
    def setSpeak(self, name):
        self.__speak = name

    def getSpeak(self):
        return self.__speak
        
    def setDSpeak(self, name):
        self.__dspeak = name

    def getDSpeak(self):
        return self.__dspeak

    def setClerk(self, name):
        self.__clerk = name

    def getClerk(self):
        return self.__clerk

    def setWhip(self, name):
        self.__Whip = name

    def getWhip(self):
        return self.__whip

class Controller:
    def __init__(self):
        pass

    def show_voter(self):
        self.voter = VotersPage()
        self.voter.setGeometry(0, 0, 480, 320)
        self.voter.switch_window.connect(self.show_main)
        return self.voter

    def show_main(self):
        self.widget = ManagerPage()
        self.widget.setGeometry(0, 0, 480, 320)
        self.widget.switch_window.connect(self.show_voter)
        return self.widget

class StackedWidgetUI(QStackedWidget):
    def __init__(self):
        super().__init__()
        manager = ManagerPage()
        voters = VotersPage()
        election = ElectionPage()
        avf1 = AddVoterForm1()
        avf2 = AddVoterForm2()
        avf3 = AddVoterForm3()
        voter = VoterPage()
        delete = DeleteVoters()
        parties = PartyPage()
        pf1 = PartyForm1()
        pf2 = PartyForm2()
        party = Party()
        elections = Elections()
        electform = ElectionForm()
        newelect = NewElection()
        aep = AddElectionParty()
        vote = VotePage()
        general = GeneralVote()
        finish = FinishVote()
        endelect = EndElection()

        manager.voteBtn.clicked.connect(self.voteBtnClicked)
        manager.elecBtn.clicked.connect(self.elecBtnCLicked)
        voters.addBtn.clicked.connect(self.addBtnClicked)
        voters.vewedBtn.clicked.connect(self.vewedBtnClicked)
        voters.delBtn.clicked.connect(self.delBtnClicked)
        voters.backBtn.clicked.connect(self.backBtnClicked)
        election.parBtn.clicked.connect(self.parBtnClicked)
        election.eleBtn.clicked.connect(self.eleBtnCLicked)
        election.backBtn.clicked.connect(self.backBtnClicked)
        parties.procBtn.clicked.connect(self.procBtnclicked)
        parties.backBtn.clicked.connect(self.backParBtnClicked)
        pf1.backBtn.clicked.connect(self.backPF1BtnClicked)
        pf1.nxtBtn.clicked.connect(self.nxtPF1BtnClicked)
        pf2.backBtn.clicked.connect(self.backPF2BtnClicked)
        pf2.nxtBtn.clicked.connect(self.nxtPF2BtnClicked)
        elections.backBtn.clicked.connect(self.backEltsBtnClicked)
        elections.crtBtn.clicked.connect(self.crtEltsBtnClicked)
        electform.backBtn.clicked.connect(self.backEltfBtnClicked)
        electform.crtBtn.clicked.connect(self.crtEltfBtnClicked)
        newelect.backBtn.clicked.connect(self.backNewBtnClicked)
        newelect.addBtn.clicked.connect(self.addNewBtnClicked)
        newelect.startBtn.clicked.connect(self.startNewBtnClicked)
        aep.backBtn.clicked.connect(self.backAEPBtnClicked)
        aep.addBtn.clicked.connect(self.addAEPBtnClicked)
        vote.backBtn.clicked.connect(self.backVoteBtnClicked)
        vote.begBtn.clicked.connect(self.begVoteBtnClicked)
        general.backBtn.clicked.connect(self.backGenBtnClicked)
        general.nxtBtn.clicked.connect(self.nxtGenBtnClicked)
        finish.backBtn.clicked.connect(self.backFinBtnClicked)
        finish.voteBtn.clicked.connect(self.voteFinBtnClicked)
        endelect.doneBtn.clicked.connect(self.doneBtnClicked)
        avf1.nxtBtn.clicked.connect(self.nxtADF1BtnClicked)
        avf1.backBtn.clicked.connect(self.backADF1BtnClicked)
        avf2.nxtBtn.clicked.connect(self.nxtADF2BtnClicked)
        avf2.backBtn.clicked.connect(self.backADF2BtnClicked)
        avf3.nxtBtn.clicked.connect(self.nxtADF3BtnClicked)
        avf3.backBtn.clicked.connect(self.backADF3BtnClicked)
        voter.editBtn.clicked.connect(self.editVoterBtnClicked)
        voter.backBtn.clicked.connect(self.backVoterBtnClicked)
        delete.backBtn.clicked.connect(self.backDelBtnClicked)
        party.backBtn.clicked.connect(self.backPartyBtnClicked)

        self.addWidget(manager)
        self.addWidget(voters)
        self.addWidget(election)
        self.addWidget(avf1)
        self.addWidget(avf2)
        self.addWidget(avf3)
        self.addWidget(voter)
        self.addWidget(delete)
        self.addWidget(parties)
        self.addWidget(pf1)
        self.addWidget(pf2)
        self.addWidget(party)
        self.addWidget(elections)
        self.addWidget(electform)
        self.addWidget(newelect)
        self.addWidget(aep)
        self.addWidget(vote)
        self.addWidget(general)
        self.addWidget(finish)
        self.addWidget(endelect)
    
        self.setGeometry(0, 0, 480, 320)

    def voteBtnClicked(self):
        self.setCurrentIndex(1)

    def elecBtnCLicked(self):
        self.setCurrentIndex(2)

    def addBtnClicked(self):
        # self.setCurrentIndex(0)
        pass

    def vewedBtnClicked(self):
        # self.setCurrentIndex(2)
        pass

    def delBtnClicked(self):
        # Not defined
        pass

    def backBtnClicked(self):
        self.setCurrentIndex(0)

    def parBtnClicked(self):
        self.setCurrentIndex(3)
        pass

    def eleBtnCLicked(self):
        # Not defined
        pass

    def backParBtnClicked(self):
        self.setCurrentIndex(2)
        pass

    def procBtnclicked(self):
        # Not defined
        pass

def main():
    app = QApplication(sys.argv)
    stack = StackedWidgetUI()
    stack.show()    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
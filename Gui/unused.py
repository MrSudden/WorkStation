

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
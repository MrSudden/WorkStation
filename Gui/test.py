import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class PresidentialCrew():
    def __init__(self):
        super().__init__()
        self.pres = 'Dummy Dummy'
        self.vpres = 'Dummy Dummy'
        self.sent = 'Dummy Dummy'

    def setPres(self, name):
        self.pres = name

    def getPres(self):
        return self.pres

    def setVPres(self, name):
        self.vpres = name

    def getVPres(self):
        return self.vpres

    def setSent(self, name):
        self.sent = name

    def getSent(self):
        return self.sent

def main():
    app = QApplication(sys.argv)
    prescrew = PresidentialCrew()
    prescrew.setPres('Isaac Wilson')
    prescrew.setVPres('Abdullahi Yaba')
    prescrew.setSent('Patricia Patrick')

    print('Presidential Candidates are:>>>')
    print('President: ' + prescrew.getPres())
    print('Vice President: ' + prescrew.getVPres())
    print('Senator: ' + prescrew.getSent())

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
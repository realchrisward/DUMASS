import DUMASS
from PyQt5.QtCore import QTimer, QCoreApplication
import sys

class dumass_doer():
    def __init__(self, app):
        self.app = app
        self.d = DUMASS.run_dumass()
        self.t = QTimer.singleShot(15000,self.timer_action)

    def timer_action(self):
        self.d.scrape()
        self.d.night_mode()
        self.e = QTimer.singleShot(60000,self.exit_action)

    def exit_action(self):
        self.app.exit()
def main():
    app = QCoreApplication(sys.argv)
    dd = dumass_doer(app)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

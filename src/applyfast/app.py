"""
CV and Cover Letter Creator
"""
import sys
from PySide2 import QtWidgets


class ApplyFast(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('applyfast')
        self.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = ApplyFast()
    sys.exit(app.exec_())

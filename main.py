from gui import Ui_MainWindow
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QFileDialog
)
from PyQt5 import QtCore, QtGui
import sys

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.browseButton.clicked.connect(self.browseFolders)

    def browseFolders(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.Directory)
        dlg.exec_()
        self.dname=dlg.selectedFiles()
        self.dirLine.setText(self.dname[0])

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
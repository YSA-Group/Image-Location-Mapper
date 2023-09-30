import sys
import os
from gui import Ui_MainWindow
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog, QVBoxLayout)
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtCore import QUrl

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.browseButton.clicked.connect(self.browseFolders)
        self.current_directory = os.path.dirname(__file__)
        self.mappath = os.path.join(self.current_directory, "Map", "index.html")
        self.loadMap()

    def loadMap(self):
        self.web = QWebEngineView(self.MapW)
        layout = QVBoxLayout(self.MapW)
        layout.addWidget(self.web)
        self.web.load(QUrl.fromLocalFile(self.mappath))

    def browseFolders(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.Directory)
        dlg.exec_()
        self.dname=dlg.selectedFiles()
        self.dname=self.dname[0]
        self.dirLine.setText(self.dname)       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
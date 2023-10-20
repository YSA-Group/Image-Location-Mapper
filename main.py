import sys
import os
from flask import Flask, jsonify
from gui import Ui_MainWindow
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog, QVBoxLayout)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from metadata import Image

app = Flask(__name__)
win = None

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.browseButton.clicked.connect(self.browseFolders)
        self.current_directory = os.path.dirname(__file__)
        self.mappath = os.path.join(self.current_directory, "Map", "index.html")
        self.loadMap()
        self.images = []
        self.longitude = 0
        self.latitude = 0

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
        self.images = []
        for file in os.listdir(self.dname):
            self.filename = os.fsdecode(file)
            if self.filename.endswith(".jpg"):
                self.img = Image(self.dname + "/" + file)
                self.images.append(self.img.returnData())
        self.longitude = self.images[0]["lon"]
        self.latitude = win.images[0]["lat"]

# Collecting data to be imported into the JavaScript
@app.route('/get_data')
def get_data():
    win = Window()
    js_longitude = win.longitude
    js_latitude = win.latitude
    return jsonify({"longitude": js_longitude, "latitude": js_latitude})
    
def run_flask_app():
    app.run()

if __name__ == "__main__":
    from multiprocessing import Process
    import time
    
    flask_process = Process(target=run_flask_app)
    flask_process.start()

    time.sleep(2)

    windows_app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(windows_app.exec())
import sys
import os
from flask import Flask, jsonify
from flask_cors import CORS
from gui import Ui_MainWindow
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog, QVBoxLayout)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from metadata import Image

app = Flask(__name__)
CORS(app)

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
        from threading import Thread

        def run_flask():
            app.run()

        flask_thread = Thread(target=run_flask)
        flask_thread.start()

    # Implement the route for getting data
    @app.route('/get_data')
    def get_data():
        js_longitude = win.longitude
        js_latitude = win.latitude
        return jsonify({"longitude": js_longitude, "latitude": js_latitude})


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
                self.web.load(QUrl.fromLocalFile(self.mappath))
        self.longitude = self.images[0]["lon"]
        self.latitude = win.images[0]["lat"]


if __name__ == "__main__":
    windows_app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(windows_app.exec_())
    
from gui import Ui_MainWindow
from PyQt5.QtWidgets import (
    QApplication, QMainWindow
)
import sys

class Window(Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
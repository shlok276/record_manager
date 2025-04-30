# gui/main_window.py
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Record Manager - Dashboard")
        self.setGeometry(100, 100, 800, 600)

        label = QLabel("Welcome to the Record Manager Dashboard", self)
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

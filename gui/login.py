# gui/login.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
from services.auth_service import create_user, authenticate_user

class LoginWindow(QWidget):
    def __init__(self, switch_to_main_callback):
        super().__init__()
        self.setWindowTitle("Login - Record Manager")
        self.setGeometry(100, 100, 400, 300)
        self.switch_to_main = switch_to_main_callback

        layout = QVBoxLayout()

        self.title = QLabel("Login to Record Manager")
        self.title.setAlignment(Qt.AlignCenter)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_btn = QPushButton("Login")
        self.signup_btn = QPushButton("Sign Up")

        layout.addWidget(self.title)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_btn)
        layout.addWidget(self.signup_btn)

        self.setLayout(layout)

        self.login_btn.clicked.connect(self.login)
        self.signup_btn.clicked.connect(self.signup)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if authenticate_user(username, password):
            self.switch_to_main()
            self.close()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

    def signup(self):
        username = self.username_input.text()
        password = self.password_input.text()
        success, msg = create_user(username, password)
        QMessageBox.information(self, "Sign Up", msg)

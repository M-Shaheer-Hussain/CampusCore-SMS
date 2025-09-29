from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
)
from src.modules.auth import verify_receptionist
from src.gui.receptionist_panel import ReceptionistPanel

class ReceptionistLoginPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Receptionist Login")
        self.init_ui()

    def init_ui(self):
        # Input fields
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        # Labels
        username_label = QLabel("Username (First Name)")
        password_label = QLabel("Password")

        # Login button
        login_btn = QPushButton("Login")
        login_btn.clicked.connect(self.handle_login)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(login_btn)

        self.setLayout(layout)

    def handle_login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Missing Info", "Please enter both username and password.")
            return

        if verify_receptionist(username, password):
            QMessageBox.information(self, "Success", "Login successful.")
            self.hide()
            self.panel = ReceptionistPanel()
            self.panel.show()
        else:
            QMessageBox.critical(self, "Login Failed", "Invalid username or password.")
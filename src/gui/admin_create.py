from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QTextEdit, QComboBox, QPushButton,
    QVBoxLayout, QFormLayout, QMessageBox
)
from src.modules.admin_manager import add_admin
from src.modules.emailer import send_verification_code

class AdminCreatePanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create Admin")
        self.verification_code = None   # ✅ Initialize here
        self.init_ui()

    def init_ui(self):
        layout = QFormLayout()

        #Adding Code Generating Button
        self.send_code_button=QPushButton("Send Code")
        self.send_code_button.clicked.connect(self.send_code)

        self.first_name = QLineEdit()
        self.middle_name = QLineEdit()
        self.last_name = QLineEdit()
        self.father_name = QLineEdit()
        self.mother_name = QLineEdit()
        self.dob = QLineEdit()
        self.gender = QComboBox()
        self.gender.addItems(["Male", "Female", "Other"])
        self.address = QTextEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)

        self.contact_type = QComboBox()
        self.contact_type.addItems(["phone", "email"])
        self.contact_value = QLineEdit()
        self.contact_label = QLineEdit()

        submit_btn = QPushButton("Create Admin")
        submit_btn.clicked.connect(self.handle_submit)

        self.code_input=QLineEdit()

        layout.addRow(self.send_code_button)
        layout.addRow("First Name", self.first_name)
        layout.addRow("Middle Name", self.middle_name)
        layout.addRow("Last Name", self.last_name)
        layout.addRow("Father Name", self.father_name)
        layout.addRow("Mother Name", self.mother_name)
        layout.addRow("DOB", self.dob)
        layout.addRow("Gender", self.gender)
        layout.addRow("Address", self.address)
        layout.addRow("Password", self.password)
        layout.addRow("Contact Type", self.contact_type)
        layout.addRow("Contact Value", self.contact_value)
        layout.addRow("Contact Label", self.contact_label)
        layout.addRow("Enter Verification Code",self.code_input)
        layout.addRow(submit_btn)


        self.setLayout(layout)

    def send_code(self):

        self.verification_code = send_verification_code("to add an admin ")

        if self.verification_code:
            QMessageBox.information(self, "Code Sent", "Verification code sent to admin email.")
        else:
            QMessageBox.information(self, "No Email Found", "No admin email found. Skipping email verification.")


    def handle_submit(self):

        if not self.verification_code:
            QMessageBox.critical(self, "Error", "You must request and enter a verification code before creating an admin.")
            return

        if self.code_input.text() != self.verification_code:
            QMessageBox.critical(self, "Error", "Invalid verification code.")
            return
        

        try:
            data = {
                'first_name': self.first_name.text(),
                'middle_name': self.middle_name.text(),
                'last_name': self.last_name.text(),
                'fathername': self.father_name.text(),
                'mothername': self.mother_name.text(),
                'dob': self.dob.text(),
                'gender': self.gender.currentText(),
                'address': self.address.toPlainText(),
                'password': self.password.text(),
                'contact': [{
                    'type': self.contact_type.currentText(),
                    'value': self.contact_value.text(),
                    'label': self.contact_label.text()
                }]
            }

            add_admin(data)
            QMessageBox.information(self, "Success", "Admin created successfully.")
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
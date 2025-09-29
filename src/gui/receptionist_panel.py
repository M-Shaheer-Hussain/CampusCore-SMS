from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QTextEdit, QComboBox, QPushButton,
    QVBoxLayout, QFormLayout, QHBoxLayout, QMessageBox
)
from src.modules.student_manager import add_student

class ReceptionistPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Student")
        self.init_ui()

    def init_ui(self):
        layout = QFormLayout()

        # Name fields
        self.first_name = QLineEdit()
        self.middle_name = QLineEdit()
        self.last_name = QLineEdit()

        # Parent names
        self.father_name = QLineEdit()
        self.mother_name = QLineEdit()

        # DOB, Gender, Address
        self.dob = QLineEdit()  # You can later use QDateEdit
        self.gender = QComboBox()
        self.gender.addItems(["Male", "Female", "Other"])

        self.address = QTextEdit()

        # Contact
        self.contact_type = QComboBox()
        self.contact_type.addItems(["phone", "email"])
        self.contact_value = QLineEdit()
        self.contact_label = QLineEdit()

        # Admission info
        self.admission_date = QLineEdit()
        self.monthly_fee = QLineEdit()
        self.annual_fund = QLineEdit()
        self.class_name = QLineEdit()

        # Submit button
        self.submit_btn = QPushButton("Add Student")
        self.submit_btn.clicked.connect(self.handle_submit)

        # Add widgets to layout
        layout.addRow("First Name", self.first_name)
        layout.addRow("Middle Name", self.middle_name)
        layout.addRow("Last Name", self.last_name)
        layout.addRow("Father Name", self.father_name)
        layout.addRow("Mother Name", self.mother_name)
        layout.addRow("Date of Birth", self.dob)
        layout.addRow("Gender", self.gender)
        layout.addRow("Address", self.address)
        layout.addRow("Contact Type", self.contact_type)
        layout.addRow("Contact Value", self.contact_value)
        layout.addRow("Contact Label", self.contact_label)
        layout.addRow("Admission Date", self.admission_date)
        layout.addRow("Monthly Fee", self.monthly_fee)
        layout.addRow("Annual Fund", self.annual_fund)
        layout.addRow("Class", self.class_name)
        layout.addRow(self.submit_btn)

        self.setLayout(layout)

    def handle_submit(self):
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
                'contact': [{
                    'type': self.contact_type.currentText(),
                    'value': self.contact_value.text(),
                    'label': self.contact_label.text()
                }],
                'date_of_admission': self.admission_date.text(),
                'monthly_fee': float(self.monthly_fee.text()),
                'annual_fund': float(self.annual_fund.text()),
                'class': self.class_name.text()
            }

            add_student(data)
            QMessageBox.information(self, "Success", "Student added successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout
from src.gui.receptionist_login import ReceptionistLoginPanel
from src.gui.receptionist_create import ReceptionistCreatePanel
from src.gui.admin_create import AdminCreatePanel

class RoleSelector(QWidget):
    def __init__(self):
        super().__init__()
        #Window Name can be changed from here!
        self.setWindowTitle("Select Role")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        receptionist_login = QPushButton("Receptionist Login")
        receptionist_create = QPushButton("Add Receptionist")
        admin_create = QPushButton("Add Admin")

        receptionist_login.clicked.connect(self.open_login)
        receptionist_create.clicked.connect(self.open_create)
        admin_create.clicked.connect(self.open_admin_create)

        layout.addWidget(receptionist_login)
        layout.addWidget(receptionist_create)
        layout.addWidget(admin_create)

        self.setLayout(layout)

    def open_login(self):
        self.hide()
        self.login_panel = ReceptionistLoginPanel()
        self.login_panel.show()

    def open_create(self):
        self.hide()
        self.create_panel = ReceptionistCreatePanel()
        self.create_panel.show()

    def open_admin_create(self):
        self.hide()
        self.admin_panel = AdminCreatePanel()
        self.admin_panel.show()
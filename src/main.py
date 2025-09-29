# src/main.py

from src.modules.init_db import initialize_db
from src.gui.receptionist_panel import ReceptionistPanel
from PyQt5.QtWidgets import QApplication
import sys

def main():
    print("🔧 Initializing database...")
    initialize_db()

    print("🚀 Launching CampusCore GUI...")
    app = QApplication(sys.argv)
    window = ReceptionistPanel()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
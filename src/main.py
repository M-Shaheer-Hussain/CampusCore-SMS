from PyQt5.QtWidgets import QApplication
from src.gui.role_selector import RoleSelector
import sys

def main():
    app = QApplication(sys.argv)
    selector = RoleSelector()
    selector.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
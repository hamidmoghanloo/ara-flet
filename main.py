import os
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from db import init_db
from login_page import LoginPage
from register_page import RegisterPage
from dashboard_page import DashboardPage

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AdminPanel — Login")
        self.setMinimumSize(1200, 800)
        self.resize(1280, 820)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.login_page = LoginPage(self.handle_login_success, self.show_register)
        self.register_page = RegisterPage(self.show_login, self.show_login)

        self.stack.addWidget(self.login_page)
        self.stack.addWidget(self.register_page)
        self.dashboard_page = None

        self.stack.setCurrentWidget(self.login_page)

    def show_register(self):
        self.stack.setCurrentWidget(self.register_page)
        self.setWindowTitle("AdminPanel — Register")

    def show_login(self):
        self.stack.setCurrentWidget(self.login_page)
        self.setWindowTitle("AdminPanel — Login")

    def handle_login_success(self, user):
        self.dashboard_page = DashboardPage(user, self.handle_logout)
        self.stack.addWidget(self.dashboard_page)
        self.stack.setCurrentWidget(self.dashboard_page)
        self.setWindowTitle("AdminPanel — Dashboard")

    def handle_logout(self):
        self.stack.setCurrentWidget(self.login_page)
        self.setWindowTitle("AdminPanel — Login")
        if self.dashboard_page is not None:
            self.stack.removeWidget(self.dashboard_page)
            self.dashboard_page.deleteLater()
            self.dashboard_page = None


def main():
    init_db()

    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    qss_path = os.path.join(BASE_DIR, "style.qss")
    with open(qss_path, "r", encoding="utf-8") as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

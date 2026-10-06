from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QFrame, QMessageBox
)

from animated_background import AnimatedBackground
from db import verify_login


class LoginPage(QWidget):
    def __init__(self, on_login_success, on_go_register):
        super().__init__()
        self.on_login_success = on_login_success
        self.on_go_register = on_go_register

        self.bg = AnimatedBackground(self)

        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)

        card = QFrame()
        card.setObjectName("card")
        card.setFixedWidth(420)
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(40, 40, 40, 40)
        card_layout.setSpacing(14)

        title = QLabel("Welcome Back")
        title.setObjectName("title")
        subtitle = QLabel("Sign in to continue to your dashboard")
        subtitle.setObjectName("subtitle")

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email address")
        self.email_input.returnPressed.connect(self.handle_login)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.returnPressed.connect(self.handle_login)

        login_btn = QPushButton("LOG IN")
        login_btn.setObjectName("primaryBtn")
        login_btn.clicked.connect(self.handle_login)

        register_row = QHBoxLayout()
        register_label = QLabel("Don't have an account?")
        register_label.setObjectName("mutedLabel")
        register_btn = QPushButton("Create Account")
        register_btn.setObjectName("linkBtn")
        register_btn.clicked.connect(self.on_go_register)
        register_row.addWidget(register_label)
        register_row.addWidget(register_btn)
        register_row.addStretch()

        card_layout.addWidget(title)
        card_layout.addWidget(subtitle)
        card_layout.addSpacing(8)
        card_layout.addWidget(self.email_input)
        card_layout.addWidget(self.password_input)
        card_layout.addSpacing(4)
        card_layout.addWidget(login_btn)
        card_layout.addLayout(register_row)

        outer.addStretch()
        center_row = QHBoxLayout()
        center_row.addStretch()
        center_row.addWidget(card)
        center_row.addStretch()
        outer.addLayout(center_row)
        outer.addStretch()

    def resizeEvent(self, event):
        self.bg.setGeometry(0, 0, self.width(), self.height())
        self.bg.lower()
        super().resizeEvent(event)

    def clear_fields(self):
        self.email_input.clear()
        self.password_input.clear()

    def handle_login(self):
        email = self.email_input.text().strip()
        password = self.password_input.text()

        if not email or not password:
            QMessageBox.warning(self, "Missing info", "Please enter both email and password.")
            return

        user = verify_login(email, password)
        if user:
            self.clear_fields()
            self.on_login_success(user)
        else:
            QMessageBox.critical(self, "Login failed", "Incorrect email or password.")

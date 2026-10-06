from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QFrame, QMessageBox
)

from animated_background import AnimatedBackground
from db import add_user
from captcha import generate_captcha_text, render_captcha_pixmap


class RegisterPage(QWidget):
    def __init__(self, on_register_success, on_go_login):
        super().__init__()
        self.on_register_success = on_register_success
        self.on_go_login = on_go_login
        self.captcha_text = generate_captcha_text()

        self.bg = AnimatedBackground(self)

        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)

        card = QFrame()
        card.setObjectName("card")
        card.setFixedWidth(460)
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(40, 30, 40, 30)
        card_layout.setSpacing(10)

        title = QLabel("Create Account")
        title.setObjectName("title")
        subtitle = QLabel("Fill in your details to get started")
        subtitle.setObjectName("subtitle")

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Full name")

        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Age")

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email address")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.confirm_input = QLineEdit()
        self.confirm_input.setPlaceholderText("Confirm password")
        self.confirm_input.setEchoMode(QLineEdit.Password)

        captcha_row = QHBoxLayout()
        self.captcha_label = QLabel()
        self.captcha_label.setFixedSize(160, 60)
        self._refresh_captcha_image()

        refresh_btn = QPushButton("\u27f3")
        refresh_btn.setObjectName("refreshBtn")
        refresh_btn.setFixedSize(36, 36)
        refresh_btn.setToolTip("Get a new code")
        refresh_btn.clicked.connect(self.refresh_captcha)

        captcha_row.addWidget(self.captcha_label)
        captcha_row.addWidget(refresh_btn)
        captcha_row.addStretch()

        self.captcha_input = QLineEdit()
        self.captcha_input.setPlaceholderText("Enter the code shown above")

        register_btn = QPushButton("CREATE ACCOUNT")
        register_btn.setObjectName("primaryBtn")
        register_btn.clicked.connect(self.handle_register)

        login_row = QHBoxLayout()
        login_label = QLabel("Already have an account?")
        login_label.setObjectName("mutedLabel")
        login_btn = QPushButton("Log In")
        login_btn.setObjectName("linkBtn")
        login_btn.clicked.connect(self.on_go_login)
        login_row.addWidget(login_label)
        login_row.addWidget(login_btn)
        login_row.addStretch()

        card_layout.addWidget(title)
        card_layout.addWidget(subtitle)
        card_layout.addWidget(self.name_input)
        card_layout.addWidget(self.age_input)
        card_layout.addWidget(self.email_input)
        card_layout.addWidget(self.password_input)
        card_layout.addWidget(self.confirm_input)
        card_layout.addLayout(captcha_row)
        card_layout.addWidget(self.captcha_input)
        card_layout.addWidget(register_btn)
        card_layout.addLayout(login_row)

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

    def _refresh_captcha_image(self):
        pixmap = render_captcha_pixmap(self.captcha_text)
        self.captcha_label.setPixmap(pixmap)

    def refresh_captcha(self):
        self.captcha_text = generate_captcha_text()
        self._refresh_captcha_image()
        self.captcha_input.clear()

    def handle_register(self):
        name = self.name_input.text().strip()
        age_text = self.age_input.text().strip()
        email = self.email_input.text().strip()
        password = self.password_input.text()
        confirm = self.confirm_input.text()
        captcha_entry = self.captcha_input.text().strip()

        if not all([name, age_text, email, password, confirm, captcha_entry]):
            QMessageBox.warning(self, "Missing info", "Please fill in every field.")
            return

        if not age_text.isdigit():
            QMessageBox.warning(self, "Invalid age", "Age must be a whole number.")
            return

        if "@" not in email or "." not in email:
            QMessageBox.warning(self, "Invalid email", "Please enter a valid email address.")
            return

        if password != confirm:
            QMessageBox.warning(self, "Password mismatch", "Passwords do not match.")
            return

        if captcha_entry.upper() != self.captcha_text.upper():
            QMessageBox.critical(self, "Captcha failed", "The captcha code is incorrect.")
            self.refresh_captcha()
            return

        ok, message = add_user(name, int(age_text), email, password)
        if ok:
            QMessageBox.information(self, "Success", message)
            self._clear_fields()
            self.on_register_success()
        else:
            QMessageBox.critical(self, "Registration failed", message)
            self.refresh_captcha()

    def _clear_fields(self):
        self.name_input.clear()
        self.age_input.clear()
        self.email_input.clear()
        self.password_input.clear()
        self.confirm_input.clear()
        self.refresh_captcha()

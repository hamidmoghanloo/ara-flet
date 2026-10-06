from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QFrame, QMessageBox
)
from PySide6.QtCore import Qt

from animated_background import AnimatedBackground
from db import verify_login
from widgets import PasswordField
from language_manager import language_manager
from translations import t


class LoginPage(QWidget):
    def __init__(self, on_login_success, on_go_register):
        super().__init__()
        self.on_login_success = on_login_success
        self.on_go_register = on_go_register

        self.bg = AnimatedBackground(self)

        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)

        self.card = QFrame()
        self.card.setObjectName("card")
        self.card.setFixedWidth(420)
        card_layout = QVBoxLayout(self.card)
        card_layout.setContentsMargins(40, 40, 40, 40)
        card_layout.setSpacing(14)

        self.title = QLabel()
        self.title.setObjectName("title")
        self.subtitle = QLabel()
        self.subtitle.setObjectName("subtitle")

        self.email_input = QLineEdit()
        self.email_input.returnPressed.connect(self.handle_login)

        self.password_field = PasswordField()
        self.password_field.input.returnPressed.connect(self.handle_login)

        self.login_btn = QPushButton()
        self.login_btn.setObjectName("primaryBtn")
        self.login_btn.clicked.connect(self.handle_login)

        register_row = QHBoxLayout()
        self.register_label = QLabel()
        self.register_label.setObjectName("mutedLabel")
        self.register_btn = QPushButton()
        self.register_btn.setObjectName("linkBtn")
        self.register_btn.clicked.connect(self.on_go_register)
        register_row.addWidget(self.register_label)
        register_row.addWidget(self.register_btn)
        register_row.addStretch()

        card_layout.addWidget(self.title)
        card_layout.addWidget(self.subtitle)
        card_layout.addSpacing(8)
        card_layout.addWidget(self.email_input)
        card_layout.addWidget(self.password_field)
        card_layout.addSpacing(4)
        card_layout.addWidget(self.login_btn)
        card_layout.addLayout(register_row)

        outer.addStretch()
        center_row = QHBoxLayout()
        center_row.addStretch()
        center_row.addWidget(self.card)
        center_row.addStretch()
        outer.addLayout(center_row)
        outer.addStretch()

        # Language switch button, pinned to the bottom of the page
        lang_row = QHBoxLayout()
        lang_row.addStretch()
        self.lang_btn = QPushButton()
        self.lang_btn.setObjectName("langBtn")
        self.lang_btn.setCursor(Qt.PointingHandCursor)
        self.lang_btn.clicked.connect(self._toggle_language)
        lang_row.addWidget(self.lang_btn)
        lang_row.addStretch()
        outer.addLayout(lang_row)
        outer.addSpacing(24)

        language_manager.language_changed.connect(self.retranslate_ui)
        self.retranslate_ui(language_manager.current)

    def _toggle_language(self):
        language_manager.toggle()

    def retranslate_ui(self, lang):
        self.setLayoutDirection(Qt.RightToLeft if lang == "fa" else Qt.LeftToRight)
        self.title.setText(t("login_title", lang))
        self.subtitle.setText(t("login_subtitle", lang))
        self.email_input.setPlaceholderText(t("email_ph", lang))
        self.password_field.setPlaceholderText(t("password_ph", lang))
        self.login_btn.setText(t("login_btn", lang))
        self.register_label.setText(t("no_account", lang))
        self.register_btn.setText(t("create_account_link", lang))
        self.lang_btn.setText(t("lang_switch", lang))

    def resizeEvent(self, event):
        self.bg.setGeometry(0, 0, self.width(), self.height())
        self.bg.lower()
        super().resizeEvent(event)

    def clear_fields(self):
        self.email_input.clear()
        self.password_field.clear()

    def handle_login(self):
        lang = language_manager.current
        email = self.email_input.text().strip()
        password = self.password_field.text()

        if not email or not password:
            QMessageBox.warning(self, t("missing_info_title", lang), t("missing_info_msg", lang))
            return

        user = verify_login(email, password)
        if user:
            self.clear_fields()
            self.on_login_success(user)
        else:
            QMessageBox.critical(self, t("login_failed_title", lang), t("login_failed_msg", lang))

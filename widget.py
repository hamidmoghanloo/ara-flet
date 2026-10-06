from PySide6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QPushButton


class PasswordField(QWidget):
    """A QLineEdit in password mode with a small eye button beside it that
    toggles between hidden and visible text."""

    def __init__(self, placeholder="", parent=None):
        super().__init__(parent)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(6)

        self.input = QLineEdit()
        self.input.setPlaceholderText(placeholder)
        self.input.setEchoMode(QLineEdit.Password)

        self.toggle_btn = QPushButton("\U0001F441")  # eye
        self.toggle_btn.setObjectName("eyeBtn")
        self.toggle_btn.setFixedSize(36, 36)
        self.toggle_btn.setCheckable(True)
        self.toggle_btn.setToolTip("Show / hide password")
        self.toggle_btn.clicked.connect(self._toggle_visibility)

        layout.addWidget(self.input)
        layout.addWidget(self.toggle_btn)

    def _toggle_visibility(self):
        if self.toggle_btn.isChecked():
            self.input.setEchoMode(QLineEdit.Normal)
            self.toggle_btn.setText("\U0001F648")  # monkey covering eyes
        else:
            self.input.setEchoMode(QLineEdit.Password)
            self.toggle_btn.setText("\U0001F441")

    def text(self):
        return self.input.text()

    def clear(self):
        self.input.clear()
        self.toggle_btn.setChecked(False)
        self.input.setEchoMode(QLineEdit.Password)
        self.toggle_btn.setText("\U0001F441")

    def setPlaceholderText(self, text):
        self.input.setPlaceholderText(text)

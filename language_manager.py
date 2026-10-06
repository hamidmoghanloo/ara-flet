from PySide6.QtCore import QObject, Signal


class LanguageManager(QObject):
    """Tiny global signal so every page can react when the language changes."""

    language_changed = Signal(str)

    def __init__(self):
        super().__init__()
        self.current = "en"

    def toggle(self):
        self.set_language("fa" if self.current == "en" else "en")

    def set_language(self, lang):
        self.current = lang
        self.language_changed.emit(lang)


# Single shared instance used across the whole app
language_manager = LanguageManager()

import random
import string

from PySide6.QtGui import QPixmap, QPainter, QColor, QFont, QPen
from PySide6.QtCore import Qt


def generate_captcha_text(length=5):
    chars = string.ascii_uppercase + string.digits
    return "".join(random.choice(chars) for _ in range(length))


def render_captcha_pixmap(text, width=160, height=60):
    """Draw a distorted captcha image with noise lines, dots and rotated letters."""
    pixmap = QPixmap(width, height)
    pixmap.fill(QColor("#0d1117"))

    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.Antialiasing)

    # noise lines
    for _ in range(6):
        pen = QPen(QColor(
            random.randint(30, 80),
            random.randint(80, 150),
            random.randint(180, 255),
            120,
        ))
        pen.setWidth(2)
        painter.setPen(pen)
        x1, y1 = random.randint(0, width), random.randint(0, height)
        x2, y2 = random.randint(0, width), random.randint(0, height)
        painter.drawLine(x1, y1, x2, y2)

    # noise dots
    for _ in range(50):
        painter.setPen(QColor(
            random.randint(60, 120), random.randint(140, 200), 255, 90
        ))
        painter.drawPoint(random.randint(0, width), random.randint(0, height))

    # characters, each rotated a little and jittered
    n = len(text)
    spacing = width / (n + 1)
    colors = ["#4fa3ff", "#7ec8ff", "#a3d5ff", "#ffffff"]
    for i, ch in enumerate(text):
        painter.save()
        cx = spacing * (i + 1)
        cy = height / 2 + random.randint(-5, 5)
        painter.translate(cx, cy)
        painter.rotate(random.randint(-25, 25))
        font = QFont("Consolas", random.randint(20, 26), QFont.Bold)
        painter.setFont(font)
        painter.setPen(QColor(random.choice(colors)))
        painter.drawText(-10, 10, ch)
        painter.restore()

    painter.end()
    return pixmap

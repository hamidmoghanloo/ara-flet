import random

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPainter, QColor, QRadialGradient, QBrush


class AnimatedBackground(QWidget):
    """A widget that paints a dark blue/black gradient with slowly floating
    glowing particles, used as an animated background layer behind the UI."""

    def __init__(self, parent=None, particle_count=40):
        super().__init__(parent)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.particles = [self._make_particle() for _ in range(particle_count)]

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._tick)
        self.timer.start(30)

    @staticmethod
    def _make_particle():
        return {
            "x": random.uniform(0, 1),
            "y": random.uniform(0, 1),
            "r": random.uniform(4, 22),
            "speed": random.uniform(0.0003, 0.0013),
            "drift": random.uniform(-0.0004, 0.0004),
            "alpha": random.uniform(40, 140),
        }

    def _tick(self):
        for p in self.particles:
            p["y"] -= p["speed"]
            p["x"] += p["drift"]
            if p["y"] < -0.05:
                p["y"] = 1.05
                p["x"] = random.uniform(0, 1)
            if p["x"] < -0.05 or p["x"] > 1.05:
                p["x"] = random.uniform(0, 1)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        w, h = max(self.width(), 1), max(self.height(), 1)

        painter.fillRect(self.rect(), QColor("#050810"))

        glow = QRadialGradient(w * 0.5, h * 0.35, max(w, h) * 0.85)
        glow.setColorAt(0, QColor(20, 45, 90, 255))
        glow.setColorAt(1, QColor(5, 8, 16, 255))
        painter.fillRect(self.rect(), QBrush(glow))

        painter.setPen(Qt.NoPen)
        for p in self.particles:
            x, y, r = p["x"] * w, p["y"] * h, p["r"]
            grad = QRadialGradient(x, y, r)
            grad.setColorAt(0, QColor(80, 160, 255, int(p["alpha"])))
            grad.setColorAt(1, QColor(80, 160, 255, 0))
            painter.setBrush(QBrush(grad))
            painter.drawEllipse(x - r, y - r, r * 2, r * 2)

        painter.end()

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QFrame, QTableWidget, QTableWidgetItem, QHeaderView, QLineEdit
)

from db import get_all_users, count_users


class Sidebar(QFrame):
    def __init__(self, on_nav_users, on_logout):
        super().__init__()
        self.setObjectName("sidebar")
        self.setFixedWidth(220)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 30, 20, 20)
        layout.setSpacing(8)

        logo = QLabel("\u2b21  AdminPanel")
        logo.setObjectName("logo")
        layout.addWidget(logo)
        layout.addSpacing(30)

        section_label = QLabel("MAIN")
        section_label.setObjectName("navSection")
        layout.addWidget(section_label)

        users_btn = QPushButton("  Registered Users")
        users_btn.setObjectName("navBtn")
        users_btn.setCheckable(True)
        users_btn.setChecked(True)
        users_btn.clicked.connect(on_nav_users)
        layout.addWidget(users_btn)

        layout.addStretch()

        logout_btn = QPushButton("  Log Out")
        logout_btn.setObjectName("logoutBtn")
        logout_btn.clicked.connect(on_logout)
        layout.addWidget(logout_btn)


class Header(QFrame):
    def __init__(self, user_name):
        super().__init__()
        self.setObjectName("header")
        self.setFixedHeight(70)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(28, 0, 28, 0)

        title = QLabel("Dashboard")
        title.setObjectName("headerTitle")

        welcome = QLabel(f"Signed in as {user_name}")
        welcome.setObjectName("headerWelcome")

        layout.addWidget(title)
        layout.addStretch()
        layout.addWidget(welcome)


class Footer(QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("footer")
        self.setFixedHeight(36)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(28, 0, 28, 0)

        label = QLabel("\u00a9 2026 AdminPanel \u2014 Built with PySide6")
        label.setObjectName("footerLabel")

        layout.addWidget(label)
        layout.addStretch()


class DashboardPage(QWidget):
    def __init__(self, current_user, on_logout):
        super().__init__()
        self.current_user = current_user
        self.on_logout = on_logout
        self.all_rows = []

        root = QHBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        self.sidebar = Sidebar(self.load_users, on_logout)
        root.addWidget(self.sidebar)

        right_container = QWidget()
        right = QVBoxLayout(right_container)
        right.setContentsMargins(0, 0, 0, 0)
        right.setSpacing(0)

        display_name = current_user[1] if current_user else "Admin"
        self.header = Header(display_name)
        right.addWidget(self.header)

        central = QFrame()
        central.setObjectName("central")
        central_layout = QVBoxLayout(central)
        central_layout.setContentsMargins(28, 24, 28, 24)
        central_layout.setSpacing(14)

        top_row = QHBoxLayout()
        self.stats_label = QLabel()
        self.stats_label.setObjectName("statsLabel")
        top_row.addWidget(self.stats_label)
        top_row.addStretch()

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search by name or email...")
        self.search_input.setFixedWidth(260)
        self.search_input.textChanged.connect(self.filter_table)
        top_row.addWidget(self.search_input)

        refresh_btn = QPushButton("Refresh")
        refresh_btn.setObjectName("secondaryBtn")
        refresh_btn.clicked.connect(self.load_users)
        top_row.addWidget(refresh_btn)

        central_layout.addLayout(top_row)

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Name", "Age", "Email", "Password", "Registered At"]
        )
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setVisible(False)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setAlternatingRowColors(True)
        central_layout.addWidget(self.table)

        right.addWidget(central)

        self.footer = Footer()
        right.addWidget(self.footer)

        root.addWidget(right_container)

        self.load_users()

    def load_users(self):
        self.all_rows = get_all_users()
        self.stats_label.setText(f"Total registered users: {count_users()}")
        self._populate_table(self.all_rows)

    def _populate_table(self, rows):
        self.table.setRowCount(len(rows))
        for r, row in enumerate(rows):
            for c, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.table.setItem(r, c, item)

    def filter_table(self, text):
        text = text.lower().strip()
        if not text:
            self._populate_table(self.all_rows)
            return
        filtered = [
            row for row in self.all_rows
            if text in row[1].lower() or text in row[3].lower()
        ]
        self._populate_table(filtered)

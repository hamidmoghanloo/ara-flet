import flet as ft

from database.db import engine, Base
from database.models import User

from pages.login import login_page


def main(page: ft.Page):

    page.title = "Admin Panel"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#080D1B"
    page.padding = 0

    page.window.width = 1100
    page.window.height = 750

    try:
        # Create database tables if they don't exist
        Base.metadata.create_all(bind=engine)

        # Open Login Page
        login_page(page)

    except Exception as error:

        page.add(
            ft.Text(
                "Application Startup Failed!",
                color="#EF4444",
                size=20
            )
        )

        page.add(
            ft.Text(
                str(error),
                color="#FCA5A5"
            )
        )

        print("Startup Error:", error)


ft.run(main)
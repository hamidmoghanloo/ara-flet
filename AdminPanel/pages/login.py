import flet as ft
import bcrypt

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from database.db import SessionLocal
from database.models import User


def login_page(page: ft.Page):

    page.title = "Admin Panel | Welcome Back"
    page.bgcolor = "#080F20"
    page.padding = 0
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK

    message_text = ft.Text(
        value="",
        size=13,
        color="#65A8FF",
        text_align=ft.TextAlign.CENTER,
    )

    def show_message(message, color="#65A8FF"):
        message_text.value = message
        message_text.color = color
        page.update()

    # Email
    email_field = ft.TextField(
        label="Email Address",
        hint_text="Enter your email",
        prefix_icon=ft.Icons.EMAIL_OUTLINED,
        border_radius=12,
        border_color="#263B5B",
        focused_border_color="#3585FF",
        bgcolor="#111D33",
        color="white",
        cursor_color="#3585FF",
        width=320,
    )

    # Password
    password_field = ft.TextField(
        label="Password",
        hint_text="Enter your password",
        prefix_icon=ft.Icons.LOCK_OUTLINE,
        password=True,
        can_reveal_password=True,
        border_radius=12,
        border_color="#263B5B",
        focused_border_color="#3585FF",
        bgcolor="#111D33",
        color="white",
        cursor_color="#3585FF",
        width=320,
    )

    # Login function
    def login_click(e):

        email = (email_field.value or "").strip().lower()
        password = password_field.value or ""

        if not email:
            show_message(
                "Please enter your email.",
                "#FF6B6B"
            )
            return

        if not password:
            show_message(
                "Please enter your password.",
                "#FF6B6B"
            )
            return

        db = SessionLocal()

        try:
            user = db.scalar(
                select(User).where(User.email == email)
            )

            if user is None:
                show_message(
                    "Invalid email or password.",
                    "#FF6B6B"
                )
                return

            password_is_valid = bcrypt.checkpw(
                password.encode("utf-8"),
                user.password_hash.encode("utf-8")
            )

            if not password_is_valid:
                show_message(
                    "Invalid email or password.",
                    "#FF6B6B"
                )
                return

            # Save user information before closing database
            user_id = user.id

            # Open user dashboard
            page.clean()

            from pages.dashboard import dashboard_page

            dashboard_page(page, user)

        except SQLAlchemyError as error:
            print("Database Error:", error)

            show_message(
                "Database error! Please try again.",
                "#FF6B6B"
            )

        except Exception as error:
            print("Login Error:", error)

            show_message(
                "Something went wrong.",
                "#FF6B6B"
            )

        finally:
            db.close()

    # Go to Register page
    def register_click(e):

        page.clean()

        from pages.register import register_page

        register_page(page)

    # Login Button
    login_button = ft.Button(
        content="LOGIN",
        width=320,
        height=50,
        bgcolor="#2878F0",
        color="white",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12)
        ),
        on_click=login_click,
    )

    # Register Link
    register_link = ft.TextButton(
        content=ft.Text(
            "Create Account",
            color="#4C9AFF",
            weight=ft.FontWeight.BOLD,
        ),
        on_click=register_click,
    )

    # Login Card
    login_card = ft.Container(
        width=420,
        padding=35,
        border_radius=22,
        bgcolor="#101B30",
        border=ft.Border.all(1, "#263B5B"),

        shadow=ft.BoxShadow(
            blur_radius=35,
            spread_radius=2,
            color="#182F60",
            offset=ft.Offset(0, 8),
        ),

        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=18,

            controls=[
                ft.Container(
                    width=65,
                    height=65,
                    border_radius=18,
                    bgcolor="#193B70",
                    alignment=ft.Alignment.CENTER,

                    content=ft.Icon(
                        ft.Icons.ADMIN_PANEL_SETTINGS,
                        size=35,
                        color="#65A8FF",
                    ),
                ),

                ft.Text(
                    "Welcome Back",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color="white",
                ),

                ft.Text(
                    "Sign in to continue to your account",
                    size=13,
                    color="#91A3BD",
                ),

                ft.Container(height=5),

                email_field,
                password_field,

                ft.Container(height=5),

                login_button,
                message_text,

                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=4,

                    controls=[
                        ft.Text(
                            "Don't have an account?",
                            color="#91A3BD",
                            size=12,
                        ),

                        register_link,
                    ],
                ),
            ],
        ),
    )

    # Background
    background = ft.Container(
        expand=True,
        alignment=ft.Alignment.CENTER,
        padding=20,

        gradient=ft.LinearGradient(
            begin=ft.Alignment.TOP_LEFT,
            end=ft.Alignment.BOTTOM_RIGHT,

            colors=[
                "#080F20",
                "#101E38",
                "#080F20",
            ],
        ),

        content=login_card,
    )

    page.add(background)


def main(page: ft.Page):
    login_page(page)


if __name__ == "__main__":
    ft.run(main)
import flet as ft
import bcrypt

from assets.captcha.captcha import generate_captcha

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from database.db import SessionLocal
from database.models import User


def register_page(page: ft.Page):

    page.title = "Admin Panel | Create Account"
    page.bgcolor = "#080F20"
    page.padding = 0
    page.theme_mode = ft.ThemeMode.DARK

    # Message displayed inside the form
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

    # Generate CAPTCHA image
    captcha_code, captcha_image_path = generate_captcha()

    # Full Name
    name_field = ft.TextField(
        label="Full Name",
        hint_text="Enter your full name",
        prefix_icon=ft.Icons.PERSON_OUTLINE,
        width=320,
        border_radius=12,
        border_color="#263B5B",
        focused_border_color="#3585FF",
        bgcolor="#111D33",
    )

    # Age
    age_field = ft.TextField(
        label="Age",
        hint_text="Enter your age",
        prefix_icon=ft.Icons.CALENDAR_TODAY,
        keyboard_type=ft.KeyboardType.NUMBER,
        width=320,
        border_radius=12,
        border_color="#263B5B",
        focused_border_color="#3585FF",
        bgcolor="#111D33",
    )

    # Email
    email_field = ft.TextField(
        label="Email Address",
        hint_text="Enter your email",
        prefix_icon=ft.Icons.EMAIL_OUTLINED,
        width=320,
        border_radius=12,
        border_color="#263B5B",
        focused_border_color="#3585FF",
        bgcolor="#111D33",
    )

    # Password
    password_field = ft.TextField(
        label="Password",
        hint_text="Create a password",
        prefix_icon=ft.Icons.LOCK_OUTLINE,
        password=True,
        can_reveal_password=True,
        width=320,
        border_radius=12,
        border_color="#263B5B",
        focused_border_color="#3585FF",
        bgcolor="#111D33",
    )

    # CAPTCHA input
    captcha_input = ft.TextField(
        label="Enter CAPTCHA",
        hint_text="Type the code shown above",
        prefix_icon=ft.Icons.VERIFIED_USER_OUTLINED,
        width=320,
        border_radius=12,
        border_color="#263B5B",
        focused_border_color="#3585FF",
        bgcolor="#111D33",
    )

    # CAPTCHA display
    captcha_display = ft.Container(
        width=180,
        height=60,
        alignment=ft.Alignment.CENTER,
        border_radius=10,
        bgcolor="#193B70",
        border=ft.Border.all(1, "#3585FF"),
        content=ft.Image(
            src=captcha_image_path,
            width=180,
            height=60,
            fit=ft.BoxFit.FILL,
        ),
    )

    # Refresh CAPTCHA
    def refresh_captcha(e):
        nonlocal captcha_code, captcha_image_path

        captcha_code, captcha_image_path = generate_captcha()

        captcha_display.content = ft.Image(
            src=captcha_image_path,
            width=180,
            height=60,
            fit=ft.BoxFit.FILL,
        )

        captcha_input.value = ""

        show_message("New CAPTCHA generated!")

        page.update()

    # CREATE ACCOUNT BUTTON FUNCTION
    def create_account(e):

        nonlocal captcha_code, captcha_image_path

        # Check name
        if not name_field.value or not name_field.value.strip():
            show_message(
                "Please enter your full name",
                "#FF6B6B"
            )
            return

        full_name = name_field.value.strip()

        if len(full_name) > 100:
            show_message(
                "Full name must be at most 100 characters",
                "#FF6B6B"
            )
            return

        # Check age
        if not age_field.value:
            show_message(
                "Please enter your age",
                "#FF6B6B"
            )
            return

        try:
            age = int(age_field.value)

            if age < 1 or age > 120:
                show_message(
                    "Age must be between 1 and 120",
                    "#FF6B6B"
                )
                return

        except ValueError:
            show_message(
                "Age must be a number",
                "#FF6B6B"
            )
            return

        # Check email
        if not email_field.value:
            show_message(
                "Please enter your email",
                "#FF6B6B"
            )
            return

        email = email_field.value.strip().lower()

        if (
            len(email) > 150
            or email.count("@") != 1
            or "." not in email.split("@")[-1]
        ):
            show_message(
                "Please enter a valid email",
                "#FF6B6B"
            )
            return

        # Check password
        if not password_field.value:
            show_message(
                "Please enter your password",
                "#FF6B6B"
            )
            return

        password = password_field.value

        if len(password) < 8:
            show_message(
                "Password must be at least 8 characters",
                "#FF6B6B"
            )
            return

        if len(password.encode("utf-8")) > 72:
            show_message(
                "Password is too long (maximum 72 bytes)",
                "#FF6B6B"
            )
            return

        # Check CAPTCHA
        if not captcha_input.value:
            show_message(
                "Please enter CAPTCHA",
                "#FF6B6B"
            )
            return

        if captcha_input.value.strip().upper() != captcha_code:

            captcha_code, captcha_image_path = generate_captcha()

            captcha_display.content = ft.Image(
                src=captcha_image_path,
                width=180,
                height=60,
                fit=ft.BoxFit.FILL,
            )

            captcha_input.value = ""

            show_message(
                "Incorrect CAPTCHA! Please try again.",
                "#FF6B6B"
            )

            page.update()
            return

        # Start database operation
        show_message(
            "Saving your account...",
            "#65A8FF"
        )

        db = SessionLocal()

        try:
            # Check duplicate email
            existing_user = db.scalar(
                select(User).where(User.email == email)
            )

            if existing_user:
                show_message(
                    "This email is already registered!",
                    "#FF6B6B"
                )
                return

            # Hash password using bcrypt
            hashed_password = bcrypt.hashpw(
                password.encode("utf-8"),
                bcrypt.gensalt()
            ).decode("utf-8")

            # Create new user
            new_user = User(
                full_name=full_name,
                age=age,
                email=email,
                password_hash=hashed_password,
            )

            # Save user in PostgreSQL
            db.add(new_user)
            db.commit()

            # Clear fields after successful registration
            name_field.value = ""
            age_field.value = ""
            email_field.value = ""
            password_field.value = ""
            captcha_input.value = ""

            # Generate new CAPTCHA
            captcha_code, captcha_image_path = generate_captcha()

            captcha_display.content = ft.Image(
                src=captcha_image_path,
                width=180,
                height=60,
                fit=ft.BoxFit.FILL,
            )

            show_message(
                "Account created successfully!",
                "#39D98A"
            )

        except IntegrityError:
            db.rollback()

            show_message(
                "This email is already registered!",
                "#FF6B6B"
            )

        except SQLAlchemyError as error:
            db.rollback()

            print("Database Error:", error)

            show_message(
                "Database error! Please try again.",
                "#FF6B6B"
            )

        except Exception as error:
            db.rollback()

            print("Unexpected Error:", error)

            show_message(
                "Something went wrong. Please try again.",
                "#FF6B6B"
            )

        finally:
            db.close()

    # Go to Login
    def go_to_login(e):

        page.clean()

        from pages.login import login_page

        login_page(page)

    # Create Account Button
    register_button = ft.Button(
        content="CREATE ACCOUNT",
        width=320,
        height=50,
        bgcolor="#2878F0",
        color="white",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12)
        ),
        on_click=create_account,
    )

    # Main Card
    register_card = ft.Container(
        width=420,
        padding=25,
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
            spacing=13,

            controls=[

                ft.Icon(
                    ft.Icons.PERSON_ADD_ALT_1,
                    size=45,
                    color="#65A8FF",
                ),

                ft.Text(
                    "Create Account",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color="white",
                ),

                ft.Text(
                    "Create your account to get started",
                    size=12,
                    color="#91A3BD",
                ),

                name_field,
                age_field,
                email_field,
                password_field,

                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        captcha_display,

                        ft.IconButton(
                            icon=ft.Icons.REFRESH,
                            icon_color="#65A8FF",
                            tooltip="Refresh CAPTCHA",
                            on_click=refresh_captcha,
                        ),
                    ],
                ),

                captcha_input,

                register_button,

                message_text,

                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=3,

                    controls=[
                        ft.Text(
                            "Already have an account?",
                            size=12,
                            color="#91A3BD",
                        ),

                        ft.TextButton(
                            content=ft.Text(
                                "Log In",
                                color="#4C9AFF",
                                weight=ft.FontWeight.BOLD,
                            ),
                            on_click=go_to_login,
                        ),
                    ],
                ),
            ],
        ),
    )

    # Page background
    page.add(
        ft.Container(
            expand=True,
            alignment=ft.Alignment.CENTER,
            padding=10,

            content=ft.Column(
                scroll=ft.ScrollMode.AUTO,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,

                controls=[
                    register_card,
                ],
            ),
        )
    )


def main(page: ft.Page):
    register_page(page)


if __name__ == "__main__":
    ft.run(main)
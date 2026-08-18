import flet as ft


# =========================
# In-Memory Users
# =========================

users = {
    "admin": "1234"
}


def main(page: ft.Page):

    page.title = "Authentication App"
    page.window_width = 400
    page.window_height = 650
    page.window_resizable = False
    page.padding = 30

    # =========================
    # Helper
    # =========================

    def show_message(text, color=ft.Colors.RED):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(text),
            bgcolor=color
        )
        page.snack_bar.open = True
        page.update()

    # =========================
    # Welcome Page
    # =========================

    def welcome_page(username):

        page.clean()

        page.add(
            ft.Column(
                controls=[
                    ft.Container(height=80),

                    ft.Text(
                        "خوش آمدید 🎉",
                        size=32,
                        weight=ft.FontWeight.BOLD,
                    ),

                    ft.Text(
                        f"سلام {username} 👋",
                        size=22,
                    ),

                    ft.Text(
                        "با موفقیت وارد حساب کاربری شدید.",
                        size=16,
                    ),

                    ft.Container(height=30),

                    ft.ElevatedButton(
                        "خروج",
                        width=250,
                        height=50,
                        on_click=lambda e: login_page(),
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            )
        )

        page.update()

    # =========================
    # Login Page
    # =========================

    def login_page():

        page.clean()

        username = ft.TextField(
            label="نام کاربری",
            hint_text="نام کاربری خود را وارد کنید",
            width=300,
        )

        password = ft.TextField(
            label="رمز عبور",
            hint_text="رمز عبور خود را وارد کنید",
            password=True,
            can_reveal_password=True,
            width=300,
        )

        def login(e):

            user = username.value.strip()
            passw = password.value

            if not user or not passw:
                show_message("لطفاً همه فیلدها را پر کنید.")
                return

            if user in users and users[user] == passw:

                welcome_page(user)

            else:

                show_message(
                    "نام کاربری یا رمز عبور اشتباه است."
                )

        page.add(
            ft.Column(
                controls=[
                    ft.Container(height=50),

                    ft.Text(
                        "ورود",
                        size=32,
                        weight=ft.FontWeight.BOLD,
                    ),

                    ft.Text(
                        "به حساب کاربری خود وارد شوید",
                        size=16,
                    ),

                    ft.Container(height=30),

                    username,
                    password,

                    ft.Container(height=10),

                    ft.ElevatedButton(
                        "ورود",
                        width=300,
                        height=50,
                        on_click=login,
                    ),

                    ft.TextButton(
                        "حساب کاربری ندارید؟ ثبت نام کنید",
                        on_click=lambda e: register_page(),
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15,
            )
        )

        page.update()

    # =========================
    # Register Page
    # =========================

    def register_page():

        page.clean()

        username = ft.TextField(
            label="نام کاربری",
            hint_text="یک نام کاربری انتخاب کنید",
            width=300,
        )

        password = ft.TextField(
            label="رمز عبور",
            hint_text="رمز عبور خود را وارد کنید",
            password=True,
            can_reveal_password=True,
            width=300,
        )

        confirm_password = ft.TextField(
            label="تکرار رمز عبور",
            hint_text="رمز عبور را دوباره وارد کنید",
            password=True,
            can_reveal_password=True,
            width=300,
        )

        def register(e):

            user = username.value.strip()
            passw = password.value
            confirm = confirm_password.value

            # بررسی خالی نبودن
            if not user or not passw or not confirm:
                show_message(
                    "لطفاً همه فیلدها را پر کنید."
                )
                return

            # بررسی تکراری نبودن username
            if user in users:
                show_message(
                    "این نام کاربری قبلاً ثبت شده است."
                )
                return

            # بررسی رمز عبور
            if passw != confirm:
                show_message(
                    "رمزهای عبور یکسان نیستند."
                )
                return

            # ذخیره در حافظه
            users[user] = passw

            # رفتن به Welcome
            welcome_page(user)

        page.add(
            ft.Column(
                controls=[
                    ft.Container(height=30),

                    ft.Text(
                        "ثبت نام",
                        size=32,
                        weight=ft.FontWeight.BOLD,
                    ),

                    ft.Text(
                        "ساخت حساب کاربری جدید",
                        size=16,
                    ),

                    ft.Container(height=25),

                    username,
                    password,
                    confirm_password,

                    ft.Container(height=10),

                    ft.ElevatedButton(
                        "ثبت نام",
                        width=300,
                        height=50,
                        on_click=register,
                    ),

                    ft.TextButton(
                        "قبلاً حساب دارید؟ ورود",
                        on_click=lambda e: login_page(),
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15,
            )
        )

        page.update()

    # =========================
    # Start App
    # =========================

    login_page()


ft.app(target=main)
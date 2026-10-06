import flet as ft

from dashboard import dashboard_page


def register_page(page):
    page.controls.clear()

    name = ft.TextField(
        label="نام",
        width=350,
    )

    username = ft.TextField(
        label="Username",
        width=350,
    )

    password = ft.TextField(
        label="رمز عبور",
        password=True,
        can_reveal_password=True,
        width=350,
    )

    confirm_password = ft.TextField(
        label="تکرار رمز عبور",
        password=True,
        can_reveal_password=True,
        width=350,
    )

    message = ft.Text("")

    def register(e):

        if not name.value:
            message.value = "نام را وارد کنید."
            message.color = ft.Colors.RED
            page.update()
            return

        if not username.value:
            message.value = "Username را وارد کنید."
            message.color = ft.Colors.RED
            page.update()
            return

        if not password.value:
            message.value = "رمز عبور را وارد کنید."
            message.color = ft.Colors.RED
            page.update()
            return

        if password.value != confirm_password.value:
            message.value = "رمزهای عبور یکسان نیستند."
            message.color = ft.Colors.RED
            page.update()
            return

        # ثبت نام موفق
        dashboard_page(
            page,
            name.value,
            username.value,
        )

    def back_to_login(e):
        from login import login_page
        login_page(page)

    page.add(
        ft.Container(
            expand=True,
            alignment=ft.Alignment(0, 0),
            content=ft.Container(
                width=450,
                padding=40,
                bgcolor=ft.Colors.WHITE,
                border_radius=20,
                content=ft.Column(
                    [
                        ft.Text(
                            "Fin3an",
                            size=36,
                            weight=ft.FontWeight.BOLD,
                        ),

                        ft.Text(
                            "ساخت حساب کاربری",
                            size=22,
                            weight=ft.FontWeight.BOLD,
                        ),

                        name,
                        username,
                        password,
                        confirm_password,

                        message,

                        ft.ElevatedButton(
                            "ثبت نام",
                            width=350,
                            height=50,
                            on_click=register,
                        ),

                        ft.TextButton(
                            "قبلاً حساب دارم | ورود",
                            on_click=back_to_login,
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=12,
                ),
            ),
        )
    )

    page.update()
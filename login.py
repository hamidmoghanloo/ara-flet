import flet as ft

from register import register_page
from dashboard import dashboard_page


def login_page(page):
    page.controls.clear()

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

    message = ft.Text("")

    def login(e):

        if username.value == "Fin3an" and password.value == "1234":
            dashboard_page(
                page,
                "پریسان",
                "Fin3an",
            )

        else:
            message.value = "Username یا رمز عبور اشتباه است."
            message.color = ft.Colors.RED
            page.update()

    def go_register(e):
        register_page(page)

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
                            "ورود به حساب کاربری",
                            size=22,
                            weight=ft.FontWeight.BOLD,
                        ),

                        username,
                        password,
                        message,

                        ft.ElevatedButton(
                            "ورود",
                            width=350,
                            height=50,
                            on_click=login,
                        ),

                        ft.TextButton(
                            "حساب ندارم | ثبت نام",
                            on_click=go_register,
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=15,
                ),
            ),
        )
    )

    page.update()
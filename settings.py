import flet as ft

from theme import (
    NAVY,
    WHITE,
    BLACK,
    GRAY,
    LIGHT_GRAY,
    card,
)


def settings_page(page):

    def back(e):
        from dashboard import dashboard_page
        dashboard_page(page, "پریسان", "Fin3an")

    notifications = ft.Switch(
        label="اعلان‌ها",
        value=True,
    )

    dark_mode = ft.Switch(
        label="حالت تاریک",
        value=False,
    )

    language = ft.Dropdown(
        label="زبان",
        width=250,
        options=[
            ft.dropdown.Option("فارسی"),
            ft.dropdown.Option("English"),
        ],
        value="فارسی",
    )

    def save(e):
        message.value = "تنظیمات ذخیره شد."
        message.color = "#16A34A"
        page.update()

    message = ft.Text("")

    page.controls.clear()

    page.add(
        ft.Container(
            expand=True,
            bgcolor=LIGHT_GRAY,
            padding=30,
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.IconButton(
                                icon=ft.Icons.ARROW_BACK,
                                on_click=back,
                            ),

                            ft.Text(
                                "تنظیمات",
                                size=30,
                                weight=ft.FontWeight.BOLD,
                                color=BLACK,
                            ),
                        ]
                    ),

                    ft.Text(
                        "تنظیمات حساب و برنامه",
                        color=GRAY,
                    ),

                    ft.Container(height=20),

                    card(
                        ft.Column(
                            [
                                ft.Text(
                                    "عمومی",
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                    color=BLACK,
                                ),

                                ft.Divider(),

                                notifications,
                                dark_mode,
                                language,

                                ft.Container(height=10),

                                message,

                                ft.ElevatedButton(
                                    "ذخیره تنظیمات",
                                    icon=ft.Icons.SAVE,
                                    on_click=save,
                                ),
                            ],
                            spacing=15,
                        )
                    ),
                ],
                scroll=ft.ScrollMode.AUTO,
            ),
        )
    )

    page.update()
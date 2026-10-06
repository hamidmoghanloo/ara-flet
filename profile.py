import flet as ft

from theme import (
    NAVY,
    WHITE,
    BLACK,
    GRAY,
    LIGHT_GRAY,
    card,
)


def profile_page(page, user_name="پریسان", username="Fin3an"):

    def back(e):
        from dashboard import dashboard_page
        dashboard_page(page, user_name, username)

    name = ft.TextField(
        label="نام",
        value=user_name,
        width=350,
    )

    user = ft.TextField(
        label="Username",
        value=username,
        width=350,
    )

    email = ft.TextField(
        label="ایمیل",
        value="example@email.com",
        width=350,
    )

    message = ft.Text("")

    def save(e):
        message.value = "اطلاعات با موفقیت ذخیره شد."
        message.color = "#16A34A"
        page.update()

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
                                "پروفایل من",
                                size=30,
                                weight=ft.FontWeight.BOLD,
                                color=BLACK,
                            ),
                        ]
                    ),

                    ft.Container(height=20),

                    card(
                        ft.Column(
                            [
                                ft.Container(
                                    width=90,
                                    height=90,
                                    bgcolor=NAVY,
                                    border_radius=50,
                                    alignment=ft.Alignment(0, 0),
                                    content=ft.Text(
                                        user_name[0],
                                        size=40,
                                        color=WHITE,
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                ),

                                ft.Text(
                                    user_name,
                                    size=24,
                                    weight=ft.FontWeight.BOLD,
                                    color=BLACK,
                                ),

                                ft.Text(
                                    f"@{username}",
                                    color=GRAY,
                                ),

                                ft.Divider(),

                                name,
                                user,
                                email,

                                message,

                                ft.ElevatedButton(
                                    "ذخیره تغییرات",
                                    icon=ft.Icons.SAVE,
                                    width=350,
                                    on_click=save,
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=12,
                        ),
                        padding=30,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.AUTO,
            ),
        )
    )

    page.update()
import flet as ft

from theme import (
    NAVY,
    WHITE,
    BLACK,
    GRAY,
    LIGHT_GRAY,
    GREEN,
    ORANGE,
    card,
)


def notifications_page(page):

    def back(e):
        from dashboard import dashboard_page
        dashboard_page(page, "پریسان", "Fin3an")

    notifications = [
        (
            "پروژه جدید ایجاد شد",
            "یک پروژه جدید با موفقیت ثبت شد.",
            ft.Icons.FOLDER,
            NAVY,
        ),
        (
            "گزارش آماده است",
            "گزارش فعالیت‌های اخیر آماده مشاهده است.",
            ft.Icons.INSERT_CHART,
            GREEN,
        ),
        (
            "یادآوری",
            "اطلاعات پروفایل خود را بررسی کنید.",
            ft.Icons.NOTIFICATIONS,
            ORANGE,
        ),
    ]

    items = []

    for title, subtitle, icon, color in notifications:

        items.append(
            card(
                ft.ListTile(
                    leading=ft.Container(
                        width=45,
                        height=45,
                        bgcolor=color,
                        border_radius=12,
                        alignment=ft.Alignment(0, 0),
                        content=ft.Icon(
                            icon,
                            color=WHITE,
                        ),
                    ),
                    title=ft.Text(
                        title,
                        weight=ft.FontWeight.BOLD,
                        color=BLACK,
                    ),
                    subtitle=ft.Text(
                        subtitle,
                        color=GRAY,
                    ),
                )
            )
        )

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
                                "اعلان‌ها",
                                size=30,
                                weight=ft.FontWeight.BOLD,
                                color=BLACK,
                            ),
                        ]
                    ),

                    ft.Text(
                        "آخرین اطلاعیه‌های حساب شما",
                        color=GRAY,
                    ),

                    ft.Container(height=20),

                    *items,
                ],
                scroll=ft.ScrollMode.AUTO,
            ),
        )
    )

    page.update()
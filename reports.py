import flet as ft
from theme import NAVY, WHITE, BLACK, GRAY, LIGHT_GRAY


def reports_page(page):

    page.controls.clear()

    # -----------------------------
    # عنوان صفحه
    # -----------------------------

    title = ft.Text(
        "گزارش‌ها",
        size=30,
        weight=ft.FontWeight.BOLD,
        color=BLACK,
    )

    subtitle = ft.Text(
        "گزارش فعالیت‌ها و وضعیت پروژه‌ها",
        size=14,
        color=GRAY,
    )

    # -----------------------------
    # کارت آماری
    # -----------------------------

    def report_card(title, value, icon):

        return ft.Container(
            expand=True,
            padding=20,
            bgcolor=WHITE,
            border_radius=15,
            content=ft.Row(
                [
                    ft.Container(
                        width=55,
                        height=55,
                        bgcolor=NAVY,
                        border_radius=12,
                        alignment=ft.Alignment(0, 0),
                        content=ft.Icon(
                            icon,
                            color=WHITE,
                            size=28,
                        ),
                    ),

                    ft.Column(
                        [
                            ft.Text(
                                title,
                                size=13,
                                color=GRAY,
                            ),

                            ft.Text(
                                value,
                                size=25,
                                weight=ft.FontWeight.BOLD,
                                color=BLACK,
                            ),
                        ],
                        spacing=3,
                    ),
                ],
                spacing=15,
            ),
        )

    # -----------------------------
    # کارت گزارش‌ها
    # -----------------------------

    report_list = ft.Container(
        padding=20,
        bgcolor=WHITE,
        border_radius=15,
        content=ft.Column(
            [
                ft.Text(
                    "گزارش‌های اخیر",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color=BLACK,
                ),

                ft.Divider(),

                ft.ListTile(
                    leading=ft.Icon(
                        ft.Icons.INSERT_CHART,
                        color=NAVY,
                    ),
                    title=ft.Text(
                        "گزارش فعالیت",
                        color=BLACK,
                    ),
                    subtitle=ft.Text(
                        "آخرین بروزرسانی: امروز",
                        color=GRAY,
                    ),
                    trailing=ft.Icon(
                        ft.Icons.ARROW_FORWARD_IOS,
                        size=18,
                        color=GRAY,
                    ),
                ),

                ft.Divider(),

                ft.ListTile(
                    leading=ft.Icon(
                        ft.Icons.FOLDER,
                        color=NAVY,
                    ),
                    title=ft.Text(
                        "گزارش پروژه‌ها",
                        color=BLACK,
                    ),
                    subtitle=ft.Text(
                        "۱۲ پروژه ثبت شده",
                        color=GRAY,
                    ),
                    trailing=ft.Icon(
                        ft.Icons.ARROW_FORWARD_IOS,
                        size=18,
                        color=GRAY,
                    ),
                ),

                ft.Divider(),

                ft.ListTile(
                    leading=ft.Icon(
                        ft.Icons.BAR_CHART,
                        color=NAVY,
                    ),
                    title=ft.Text(
                        "گزارش عملکرد",
                        color=BLACK,
                    ),
                    subtitle=ft.Text(
                        "وضعیت کلی فعالیت‌ها",
                        color=GRAY,
                    ),
                    trailing=ft.Icon(
                        ft.Icons.ARROW_FORWARD_IOS,
                        size=18,
                        color=GRAY,
                    ),
                ),
            ],
            spacing=5,
        ),
    )

    # -----------------------------
    # صفحه گزارش‌ها
    # -----------------------------

    page.add(
        ft.Container(
            expand=True,
            bgcolor=LIGHT_GRAY,
            padding=30,
            content=ft.Column(
                [
                    title,
                    subtitle,

                    ft.Container(height=15),

                    ft.Row(
                        [
                            report_card(
                                "کل پروژه‌ها",
                                "12",
                                ft.Icons.FOLDER,
                            ),

                            report_card(
                                "گزارش‌ها",
                                "24",
                                ft.Icons.INSERT_CHART,
                            ),

                            report_card(
                                "فعالیت‌ها",
                                "38",
                                ft.Icons.TRENDING_UP,
                            ),
                        ],
                        spacing=15,
                    ),

                    ft.Container(height=20),

                    report_list,
                ],
                spacing=5,
                scroll=ft.ScrollMode.AUTO,
            ),
        )
    )

    page.update()
import flet as ft

from theme import (
    NAVY,
    NAVY_LIGHT,
    WHITE,
    BLACK,
    GRAY,
    LIGHT_GRAY,
    GREEN,
    ORANGE,
    card,
)

from projects import projects_page
from reports import reports_page
from profile import profile_page
from notifications import notifications_page
from settings import settings_page


def dashboard_page(page, user_name="پریسان", username="Fin3an"):

    def show_dashboard(e=None):
        page.controls.clear()
        page.add(build_dashboard())
        page.update()

    def show_projects(e):
        projects_page(page, user_name, username)

    def show_reports(e):
        reports_page(page)

    def show_profile(e):
        profile_page(page, user_name, username)

    def show_notifications(e):
        notifications_page(page)

    def show_settings(e):
        settings_page(page)

    def logout(e):
        from login import login_page
        login_page(page)

    sidebar = ft.Container(
        width=230,
        bgcolor=NAVY,
        padding=20,
        content=ft.Column(
            [
                ft.Text(
                    "Fin3an",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color=WHITE,
                ),

                ft.Text(
                    "پنل مدیریت",
                    size=12,
                    color="#B8C2D9",
                ),

                ft.Container(height=30),

                ft.TextButton(
                    "داشبورد",
                    icon=ft.Icons.DASHBOARD,
                    on_click=show_dashboard,
                    style=ft.ButtonStyle(color=WHITE),
                ),

                ft.TextButton(
                    "پروژه‌ها",
                    icon=ft.Icons.FOLDER,
                    on_click=show_projects,
                    style=ft.ButtonStyle(color=WHITE),
                ),

                ft.TextButton(
                    "گزارش‌ها",
                    icon=ft.Icons.INSERT_CHART,
                    on_click=show_reports,
                    style=ft.ButtonStyle(color=WHITE),
                ),

                ft.TextButton(
                    "پروفایل",
                    icon=ft.Icons.PERSON,
                    on_click=show_profile,
                    style=ft.ButtonStyle(color=WHITE),
                ),

                ft.TextButton(
                    "اعلان‌ها",
                    icon=ft.Icons.NOTIFICATIONS,
                    on_click=show_notifications,
                    style=ft.ButtonStyle(color=WHITE),
                ),

                ft.TextButton(
                    "تنظیمات",
                    icon=ft.Icons.SETTINGS,
                    on_click=show_settings,
                    style=ft.ButtonStyle(color=WHITE),
                ),

                ft.Container(expand=True),

                ft.TextButton(
                    "خروج از حساب",
                    icon=ft.Icons.LOGOUT,
                    on_click=logout,
                    style=ft.ButtonStyle(color=WHITE),
                ),
            ],
            spacing=8,
        ),
    )

    def stat_box(title, value, icon, color):
        return ft.Container(
            expand=True,
            bgcolor=WHITE,
            border_radius=16,
            padding=20,
            content=ft.Row(
                [
                    ft.Container(
                        width=50,
                        height=50,
                        bgcolor=color,
                        border_radius=12,
                        alignment=ft.Alignment(0, 0),
                        content=ft.Icon(
                            icon,
                            color=WHITE,
                            size=25,
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
                                size=27,
                                weight=ft.FontWeight.BOLD,
                                color=BLACK,
                            ),
                        ],
                        spacing=4,
                    ),
                ],
                spacing=15,
            ),
        )

    def build_dashboard():

        welcome = ft.Container(
            bgcolor=NAVY,
            border_radius=18,
            padding=25,
            content=ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text(
                                f"سلام {user_name} 👋",
                                size=27,
                                weight=ft.FontWeight.BOLD,
                                color=WHITE,
                            ),
                            ft.Text(
                                "به داشبورد Fin3an خوش اومدی",
                                size=14,
                                color="#C7D2E8",
                            ),
                        ],
                        spacing=5,
                    ),

                    ft.Container(expand=True),

                    ft.Container(
                        width=55,
                        height=55,
                        bgcolor=WHITE,
                        border_radius=30,
                        alignment=ft.Alignment(0, 0),
                        content=ft.Text(
                            user_name[0],
                            size=25,
                            weight=ft.FontWeight.BOLD,
                            color=NAVY,
                        ),
                    ),
                ]
            ),
        )

        stats = ft.Row(
            [
                stat_box(
                    "کل پروژه‌ها",
                    "12",
                    ft.Icons.FOLDER,
                    NAVY,
                ),
                stat_box(
                    "پروژه‌های فعال",
                    "5",
                    ft.Icons.TRENDING_UP,
                    GREEN,
                ),
                stat_box(
                    "گزارش‌ها",
                    "24",
                    ft.Icons.INSERT_CHART,
                    ORANGE,
                ),
            ],
            spacing=15,
        )

        activities = card(
            ft.Column(
                [
                    ft.Text(
                        "آخرین فعالیت‌ها",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=BLACK,
                    ),

                    ft.Divider(),

                    ft.ListTile(
                        leading=ft.Icon(
                            ft.Icons.FOLDER_OPEN,
                            color=NAVY,
                        ),
                        title=ft.Text(
                            "پروژه جدید ایجاد شد"
                        ),
                        subtitle=ft.Text(
                            "امروز - ساعت ۱۰:۳۰"
                        ),
                    ),

                    ft.ListTile(
                        leading=ft.Icon(
                            ft.Icons.EDIT,
                            color=GREEN,
                        ),
                        title=ft.Text(
                            "اطلاعات پروفایل ویرایش شد"
                        ),
                        subtitle=ft.Text(
                            "امروز - ساعت ۹:۱۵"
                        ),
                    ),

                    ft.ListTile(
                        leading=ft.Icon(
                            ft.Icons.INSERT_CHART,
                            color=ORANGE,
                        ),
                        title=ft.Text(
                            "گزارش جدید آماده شد"
                        ),
                        subtitle=ft.Text(
                            "دیروز - ساعت ۱۸:۲۰"
                        ),
                    ),
                ],
                spacing=3,
            )
        )

        quick = card(
            ft.Column(
                [
                    ft.Text(
                        "دسترسی سریع",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=BLACK,
                    ),

                    ft.Container(height=10),

                    ft.Row(
                        [
                            ft.ElevatedButton(
                                "پروژه جدید",
                                icon=ft.Icons.ADD,
                                on_click=show_projects,
                            ),

                            ft.ElevatedButton(
                                "مشاهده گزارش‌ها",
                                icon=ft.Icons.BAR_CHART,
                                on_click=show_reports,
                            ),
                        ],
                        spacing=10,
                    ),
                ]
            )
        )

        return ft.Container(
            expand=True,
            bgcolor=LIGHT_GRAY,
            padding=30,
            content=ft.Column(
                [
                    welcome,
                    ft.Container(height=20),
                    stats,
                    ft.Container(height=20),
                    activities,
                    ft.Container(height=15),
                    quick,
                ],
                scroll=ft.ScrollMode.AUTO,
            ),
        )

    page.controls.clear()

    page.add(
        ft.Row(
            [
                sidebar,
                ft.Container(
                    expand=True,
                    content=build_dashboard(),
                ),
            ],
            spacing=0,
            expand=True,
        )
    )

    page.update()
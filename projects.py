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


def projects_page(page, user_name="پریسان", username="Fin3an"):

    projects = [
        ["طراحی وب‌سایت", "در حال انجام", "75%"],
        ["پروژه مدرسه", "تکمیل شده", "100%"],
        ["تحقیق و گزارش", "در حال انجام", "50%"],
        ["پروژه شخصی", "شروع نشده", "0%"],
    ]

    def go_dashboard(e):
        from dashboard import dashboard_page
        dashboard_page(page, user_name, username)

    def add_project(e):
        name = project_name.value

        if name:
            projects.append(
                [name, "شروع نشده", "0%"]
            )

            project_name.value = ""
            dialog.open = False
            page.update()

            render()

    project_name = ft.TextField(
        label="نام پروژه",
        width=350,
    )

    dialog = ft.AlertDialog(
        title=ft.Text("ایجاد پروژه جدید"),
        content=project_name,
        actions=[
            ft.TextButton(
                "لغو",
                on_click=lambda e: close_dialog(),
            ),
            ft.ElevatedButton(
                "ایجاد",
                on_click=add_project,
            ),
        ],
    )

    def close_dialog():
        dialog.open = False
        page.update()

    def open_dialog(e):
        dialog.open = True
        page.update()

    page.dialog = dialog

    def project_card(item):

        name, status, progress = item

        if status == "تکمیل شده":
            color = GREEN
        elif status == "در حال انجام":
            color = ORANGE
        else:
            color = GRAY

        return card(
            ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text(
                                name,
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color=BLACK,
                            ),

                            ft.Container(expand=True),

                            ft.Container(
                                bgcolor=color,
                                border_radius=10,
                                padding=8,
                                content=ft.Text(
                                    status,
                                    size=11,
                                    color=WHITE,
                                ),
                            ),
                        ]
                    ),

                    ft.Container(height=10),

                    ft.ProgressBar(
                        value=int(progress.replace("%", "")) / 100,
                    ),

                    ft.Container(height=5),

                    ft.Text(
                        f"پیشرفت: {progress}",
                        size=12,
                        color=GRAY,
                    ),
                ]
            )
        )

    def render():

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
                                    on_click=go_dashboard,
                                ),

                                ft.Text(
                                    "پروژه‌ها",
                                    size=30,
                                    weight=ft.FontWeight.BOLD,
                                    color=BLACK,
                                ),

                                ft.Container(expand=True),

                                ft.ElevatedButton(
                                    "پروژه جدید",
                                    icon=ft.Icons.ADD,
                                    on_click=open_dialog,
                                ),
                            ]
                        ),

                        ft.Text(
                            "مدیریت و پیگیری پروژه‌های شما",
                            color=GRAY,
                        ),

                        ft.Container(height=20),

                        *[
                            project_card(project)
                            for project in projects
                        ],
                    ],
                    scroll=ft.ScrollMode.AUTO,
                ),
            )
        )

        page.update()

    render()
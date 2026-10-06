import flet as ft

from user_data import get_profile


def show_dashboard(page, username, on_profile, on_logout):
    """
    صفحه داشبورد
    """

    profile = get_profile(username)

    name = profile.get("name", "")
    phone = profile.get("phone", "")

    def logout(_):
        on_logout()

    def edit_profile(_):
        on_profile()

    # جدول اطلاعات کاربر
    user_table = ft.DataTable(
        column_spacing=35,
        horizontal_margin=15,
        heading_row_height=55,
        data_row_min_height=58,
        data_row_max_height=65,
        columns=[
            ft.DataColumn(
                ft.Text(
                    "عنوان",
                    weight=ft.FontWeight.BOLD,
                    color="#334155",
                )
            ),
            ft.DataColumn(
                ft.Text(
                    "اطلاعات",
                    weight=ft.FontWeight.BOLD,
                    color="#334155",
                )
            ),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(
                        ft.Text(
                            "نام",
                            weight=ft.FontWeight.BOLD,
                            color="#475569",
                        )
                    ),
                    ft.DataCell(
                        ft.Text(
                            name,
                            color="#0F172A",
                        )
                    ),
                ]
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(
                        ft.Text(
                            "نام کاربری",
                            weight=ft.FontWeight.BOLD,
                            color="#475569",
                        )
                    ),
                    ft.DataCell(
                        ft.Text(
                            username,
                            color="#0F172A",
                        )
                    ),
                ]
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(
                        ft.Text(
                            "شماره همراه",
                            weight=ft.FontWeight.BOLD,
                            color="#475569",
                        )
                    ),
                    ft.DataCell(
                        ft.Text(
                            phone,
                            color="#0F172A",
                        )
                    ),
                ]
            ),
        ],
    )

    # هدر داشبورد
    header = ft.Container(
        padding=ft.padding.symmetric(
            horizontal=30,
            vertical=18,
        ),
        bgcolor="#FFFFFF",
        border=ft.border.only(
            bottom=ft.BorderSide(
                width=1,
                color="#E2E8F0",
            )
        ),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    spacing=12,
                    controls=[
                        ft.Container(
                            width=45,
                            height=45,
                            border_radius=23,
                            bgcolor="#EEF2FF",
                            alignment=ft.Alignment.CENTER,
                            content=ft.Icon(
                                ft.Icons.DASHBOARD,
                                color="#4F46E5",
                                size=25,
                            ),
                        ),
                        ft.Column(
                            tight=True,
                            spacing=2,
                            controls=[
                                ft.Text(
                                    "داشبورد",
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                    color="#0F172A",
                                ),
                                ft.Text(
                                    "مدیریت اطلاعات حساب",
                                    size=12,
                                    color="#64748B",
                                ),
                            ],
                        ),
                    ],
                ),

                ft.IconButton(
                    icon=ft.Icons.LOGOUT,
                    tooltip="خروج",
                    icon_color="#DC2626",
                    on_click=logout,
                ),
            ],
        ),
    )

    # کارت خوش آمدگویی
    welcome_card = ft.Container(
        padding=25,
        border_radius=20,
        bgcolor="#EEF2FF",
        content=ft.Row(
            spacing=18,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    width=65,
                    height=65,
                    border_radius=33,
                    bgcolor="#4F46E5",
                    alignment=ft.Alignment.CENTER,
                    content=ft.Icon(
                        ft.Icons.PERSON,
                        color="#FFFFFF",
                        size=34,
                    ),
                ),

                ft.Column(
                    expand=True,
                    spacing=5,
                    controls=[
                        ft.Text(
                            f"سلام {name} 👋",
                            size=22,
                            weight=ft.FontWeight.BOLD,
                            color="#1E1B4B",
                        ),
                        ft.Text(
                            "به داشبورد کاربری خود خوش آمدید.",
                            size=14,
                            color="#475569",
                        ),
                    ],
                ),
            ],
        ),
    )

    # عنوان جدول
    table_header = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        controls=[
            ft.Text(
                "اطلاعات حساب کاربری",
                size=19,
                weight=ft.FontWeight.BOLD,
                color="#0F172A",
            ),

            ft.TextButton(
                content="ویرایش پروفایل",
                icon=ft.Icons.EDIT,
                on_click=edit_profile,
                style=ft.ButtonStyle(
                    color="#4F46E5",
                ),
            ),
        ],
    )

    table_card = ft.Container(
        width=float("inf"),
        padding=20,
        bgcolor="#FFFFFF",
        border_radius=20,
        border=ft.border.all(
            width=1,
            color="#E2E8F0",
        ),
        shadow=ft.BoxShadow(
            blur_radius=15,
            spread_radius=0,
            color="#120F172A",
            offset=ft.Offset(0, 5),
        ),
        content=ft.Column(
            tight=True,
            spacing=15,
            controls=[
                table_header,

                ft.Divider(
                    height=1,
                    color="#E2E8F0",
                ),

                ft.Row(
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                        user_table,
                    ],
                ),
            ],
        ),
    )

    page.controls.clear()

    page.add(
        ft.Container(
            expand=True,
            bgcolor="#F8FAFC",
            content=ft.Column(
                expand=True,
                spacing=0,
                controls=[
                    header,

                    ft.Container(
                        expand=True,
                        padding=30,
                        content=ft.Column(
                            expand=True,
                            scroll=ft.ScrollMode.AUTO,
                            spacing=22,
                            controls=[
                                welcome_card,
                                table_card,
                            ],
                        ),
                    ),
                ],
            ),
        )
    )

    page.update()
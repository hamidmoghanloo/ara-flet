import flet as ft


# =========================================================
# Dashboard Page
# =========================================================

def dashboard_page(page, user, email, show_message):

    # =====================================================
    # User Information
    # =====================================================

    first_name = user.get("first_name", "")
    last_name = user.get("last_name", "")
    username = user.get("username", "")
    phone = user.get("phone", "")
    age = user.get("age", "")

    # =====================================================
    # Colors
    # =====================================================

    PRIMARY = "#4F46E5"
    DARK = "#111827"
    SIDEBAR = "#111827"
    BACKGROUND = "#F3F4F6"
    WHITE = "#FFFFFF"
    GRAY = "#6B7280"
    LIGHT_BORDER = "#E5E7EB"
    RED = "#EF4444"
    GREEN = "#16A34A"
    ORANGE = "#F59E0B"

    # =====================================================
    # Central Content
    # =====================================================

    content_area = ft.Container(
        expand=True,
        bgcolor=BACKGROUND,
        padding=25,
    )

    # =====================================================
    # Dashboard Page
    # =====================================================

    def show_dashboard(e=None):

        # -----------------------------------------------
        # User Table
        # -----------------------------------------------

        user_table = ft.DataTable(
            column_spacing=60,

            columns=[
                ft.DataColumn(
                    ft.Text(
                        "عنوان",
                        weight=ft.FontWeight.BOLD,
                    )
                ),

                ft.DataColumn(
                    ft.Text(
                        "اطلاعات کاربر",
                        weight=ft.FontWeight.BOLD,
                    )
                ),
            ],

            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Text("نام")
                        ),
                        ft.DataCell(
                            ft.Text(first_name)
                        ),
                    ]
                ),

                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Text("نام خانوادگی")
                        ),
                        ft.DataCell(
                            ft.Text(last_name)
                        ),
                    ]
                ),

                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Text("نام کاربری")
                        ),
                        ft.DataCell(
                            ft.Text(username)
                        ),
                    ]
                ),

                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Text("سن")
                        ),
                        ft.DataCell(
                            ft.Text(str(age))
                        ),
                    ]
                ),

                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Text("شماره تماس")
                        ),
                        ft.DataCell(
                            ft.Text(phone)
                        ),
                    ]
                ),
            ],
        )

        # -----------------------------------------------
        # Card 1
        # -----------------------------------------------

        card1 = ft.Container(
            expand=True,
            padding=20,
            bgcolor=WHITE,
            border_radius=15,

            shadow=ft.BoxShadow(
                blur_radius=10,
                color="#20000000",
            ),

            content=ft.Column(
                controls=[
                    ft.Icon(
                        ft.Icons.PERSON,
                        size=35,
                        color=PRIMARY,
                    ),

                    ft.Text(
                        "نام",
                        color=GRAY,
                    ),

                    ft.Text(
                        first_name,
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=DARK,
                    ),
                ]
            ),
        )

        # -----------------------------------------------
        # Card 2
        # -----------------------------------------------

        card2 = ft.Container(
            expand=True,
            padding=20,
            bgcolor=WHITE,
            border_radius=15,

            shadow=ft.BoxShadow(
                blur_radius=10,
                color="#20000000",
            ),

            content=ft.Column(
                controls=[
                    ft.Icon(
                        ft.Icons.ACCOUNT_CIRCLE,
                        size=35,
                        color=GREEN,
                    ),

                    ft.Text(
                        "نام کاربری",
                        color=GRAY,
                    ),

                    ft.Text(
                        username,
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=DARK,
                    ),
                ]
            ),
        )

        # -----------------------------------------------
        # Card 3
        # -----------------------------------------------

        card3 = ft.Container(
            expand=True,
            padding=20,
            bgcolor=WHITE,
            border_radius=15,

            shadow=ft.BoxShadow(
                blur_radius=10,
                color="#20000000",
            ),

            content=ft.Column(
                controls=[
                    ft.Icon(
                        ft.Icons.PHONE,
                        size=35,
                        color=ORANGE,
                    ),

                    ft.Text(
                        "شماره تماس",
                        color=GRAY,
                    ),

                    ft.Text(
                        phone,
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        color=DARK,
                    ),
                ]
            ),
        )

        # -----------------------------------------------
        # Main Dashboard
        # -----------------------------------------------

        dashboard_content = ft.Column(
            scroll=ft.ScrollMode.AUTO,

            controls=[

                ft.Text(
                    "داشبورد",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color=DARK,
                ),

                ft.Text(
                    f"خوش آمدید {first_name} 👋",
                    size=16,
                    color=GRAY,
                ),

                ft.Container(
                    height=15
                ),

                # Cards
                ft.Row(
                    spacing=15,

                    controls=[
                        card1,
                        card2,
                        card3,
                    ],
                ),

                ft.Container(
                    height=25
                ),

                # Information Box
                ft.Container(
                    padding=25,
                    bgcolor=WHITE,
                    border_radius=15,

                    shadow=ft.BoxShadow(
                        blur_radius=10,
                        color="#20000000",
                    ),

                    content=ft.Column(
                        controls=[

                            ft.Text(
                                "اطلاعات کاربر",
                                size=22,
                                weight=ft.FontWeight.BOLD,
                                color=DARK,
                            ),

                            ft.Container(
                                height=10
                            ),

                            user_table,
                        ]
                    ),
                ),
            ],
        )

        content_area.content = dashboard_content

        page.update()

    # =====================================================
    # Profile Page
    # =====================================================

    def show_profile(e=None):

        profile_content = ft.Column(
            scroll=ft.ScrollMode.AUTO,

            controls=[

                ft.Text(
                    "پروفایل کاربری",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color=DARK,
                ),

                ft.Text(
                    "اطلاعات حساب کاربری",
                    color=GRAY,
                ),

                ft.Container(
                    height=20
                ),

                ft.Container(
                    padding=30,
                    bgcolor=WHITE,
                    border_radius=15,

                    shadow=ft.BoxShadow(
                        blur_radius=10,
                        color="#20000000",
                    ),

                    content=ft.Column(
                        horizontal_alignment=
                        ft.CrossAxisAlignment.CENTER,

                        controls=[

                            ft.Icon(
                                ft.Icons.ACCOUNT_CIRCLE,
                                size=100,
                                color=PRIMARY,
                            ),

                            ft.Text(
                                f"{first_name} {last_name}",
                                size=25,
                                weight=ft.FontWeight.BOLD,
                                color=DARK,
                            ),

                            ft.Text(
                                f"@{username}",
                                color=GRAY,
                            ),

                            ft.Divider(
                                color=LIGHT_BORDER
                            ),

                            ft.Text(
                                f"ایمیل: {email}",
                                size=16,
                            ),

                            ft.Text(
                                f"شماره تماس: {phone}",
                                size=16,
                            ),

                            ft.Text(
                                f"سن: {age}",
                                size=16,
                            ),
                        ],
                    ),
                ),
            ],
        )

        content_area.content = profile_content

        page.update()

    # =====================================================
    # Reports Page
    # =====================================================

    def show_reports(e=None):

        reports_content = ft.Column(
            scroll=ft.ScrollMode.AUTO,

            controls=[

                ft.Text(
                    "گزارشات",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color=DARK,
                ),

                ft.Text(
                    "گزارش اطلاعات کاربر",
                    color=GRAY,
                ),

                ft.Container(
                    height=20
                ),

                ft.Container(
                    padding=30,
                    bgcolor=WHITE,
                    border_radius=15,

                    shadow=ft.BoxShadow(
                        blur_radius=10,
                        color="#20000000",
                    ),

                    content=ft.Column(
                        controls=[

                            ft.Row(
                                controls=[

                                    ft.Icon(
                                        ft.Icons.BAR_CHART,
                                        size=40,
                                        color=PRIMARY,
                                    ),

                                    ft.Text(
                                        "گزارش کاربر",
                                        size=22,
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                ]
                            ),

                            ft.Divider(),

                            ft.Text(
                                f"نام: {first_name}"
                            ),

                            ft.Text(
                                f"نام خانوادگی: {last_name}"
                            ),

                            ft.Text(
                                f"نام کاربری: {username}"
                            ),

                            ft.Text(
                                f"سن: {age}"
                            ),

                            ft.Text(
                                f"شماره تماس: {phone}"
                            ),
                        ],
                    ),
                ),
            ],
        )

        content_area.content = reports_content

        page.update()

    # =====================================================
    # Settings Page
    # =====================================================

    def show_settings(e=None):

        settings_content = ft.Column(
            scroll=ft.ScrollMode.AUTO,

            controls=[

                ft.Text(
                    "تنظیمات",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color=DARK,
                ),

                ft.Text(
                    "تنظیمات حساب کاربری",
                    color=GRAY,
                ),

                ft.Container(
                    height=20
                ),

                ft.Container(
                    padding=25,
                    bgcolor=WHITE,
                    border_radius=15,

                    shadow=ft.BoxShadow(
                        blur_radius=10,
                        color="#20000000",
                    ),

                    content=ft.Column(
                        controls=[

                            ft.Text(
                                "تنظیمات برنامه",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                            ),

                            ft.Switch(
                                label="اعلان‌ها",
                                value=True,
                            ),

                            ft.Switch(
                                label="حالت تاریک",
                                value=False,
                            ),
                        ],
                    ),
                ),
            ],
        )

        content_area.content = settings_content

        page.update()

    # =====================================================
    # Logout
    # =====================================================

    def logout(e):

        page.controls.clear()

        page.controls.append(
            ft.Container(
                expand=True,
                bgcolor=BACKGROUND,
                alignment=ft.Alignment.CENTER,

                content=ft.Column(
                    horizontal_alignment=
                    ft.CrossAxisAlignment.CENTER,

                    controls=[

                        ft.Icon(
                            ft.Icons.LOGOUT,
                            size=70,
                            color=RED,
                        ),

                        ft.Text(
                            "خروج از حساب",
                            size=25,
                            weight=ft.FontWeight.BOLD,
                        ),

                        ft.Text(
                            "از حساب کاربری خارج شدید.",
                            color=GRAY,
                        ),
                    ],
                ),
            )
        )

        page.update()

    # =====================================================
    # Sidebar Button
    # =====================================================

    def sidebar_button(
        icon,
        text,
        on_click,
    ):

        return ft.Container(

            padding=12,

            border_radius=10,

            ink=True,

            on_click=on_click,

            content=ft.Row(
                spacing=15,

                controls=[

                    ft.Icon(
                        icon,
                        size=22,
                        color=WHITE,
                    ),

                    ft.Text(
                        text,
                        size=15,
                        color=WHITE,
                    ),
                ],
            ),
        )

    # =====================================================
    # Sidebar
    # =====================================================

    sidebar = ft.Container(

        width=240,

        bgcolor=SIDEBAR,

        padding=15,

        content=ft.Column(

            spacing=8,

            controls=[

                # -----------------------------------------
                # Logo
                # -----------------------------------------

                ft.Container(
                    padding=15,

                    content=ft.Column(
                        horizontal_alignment=
                        ft.CrossAxisAlignment.CENTER,

                        controls=[

                            ft.Icon(
                                ft.Icons.DASHBOARD,
                                size=50,
                                color=WHITE,
                            ),

                            ft.Text(
                                "My Dashboard",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color=WHITE,
                            ),
                        ],
                    ),
                ),

                ft.Divider(
                    color="#374151"
                ),

                # -----------------------------------------
                # Menu
                # -----------------------------------------

                sidebar_button(
                    ft.Icons.HOME,
                    "داشبورد",
                    show_dashboard,
                ),

                sidebar_button(
                    ft.Icons.PERSON,
                    "پروفایل",
                    show_profile,
                ),

                sidebar_button(
                    ft.Icons.BAR_CHART,
                    "گزارشات",
                    show_reports,
                ),

                sidebar_button(
                    ft.Icons.SETTINGS,
                    "تنظیمات",
                    show_settings,
                ),

                # فاصله تا پایین
                ft.Container(
                    expand=True
                ),

                ft.Divider(
                    color="#374151"
                ),

                sidebar_button(
                    ft.Icons.LOGOUT,
                    "خروج",
                    logout,
                ),
            ],
        ),
    )

    # =====================================================
    # Header
    # =====================================================

    header = ft.Container(

        height=70,

        bgcolor=WHITE,

        padding=ft.Padding(
            left=25,
            right=25,
            top=0,
            bottom=0,
        ),

        shadow=ft.BoxShadow(
            blur_radius=8,
            color="#20000000",
        ),

        content=ft.Row(

            alignment=
            ft.MainAxisAlignment.SPACE_BETWEEN,

            controls=[

                # -----------------------------------------
                # Header Title
                # -----------------------------------------

                ft.Text(
                    "پنل مدیریت",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color=DARK,
                ),

                # -----------------------------------------
                # User
                # -----------------------------------------

                ft.Row(

                    spacing=10,

                    controls=[

                        ft.Column(

                            horizontal_alignment=
                            ft.CrossAxisAlignment.END,

                            spacing=0,

                            controls=[

                                ft.Text(
                                    f"{first_name} {last_name}",
                                    weight=ft.FontWeight.BOLD,
                                    color=DARK,
                                ),

                                ft.Text(
                                    f"@{username}",
                                    size=12,
                                    color=GRAY,
                                ),
                            ],
                        ),

                        ft.CircleAvatar(

                            radius=22,

                            bgcolor=PRIMARY,

                            content=ft.Text(
                                first_name[:1]
                                if first_name
                                else "U",

                                color=WHITE,

                                size=20,
                            ),
                        ),
                    ],
                ),
            ],
        ),
    )

    # =====================================================
    # Footer
    # =====================================================

    footer = ft.Container(

        height=50,

        bgcolor=WHITE,

        padding=ft.Padding(
            left=15,
            right=15,
            top=0,
            bottom=0,
        ),

        content=ft.Row(

            alignment=
            ft.MainAxisAlignment.CENTER,

            controls=[

                ft.Text(
                    "© 2026 My Dashboard",
                    size=13,
                    color=GRAY,
                ),

                ft.Text(
                    " | ",
                    color="#D1D5DB",
                ),

                ft.Text(
                    "ساخته شده با Python و Flet",
                    size=13,
                    color=GRAY,
                ),
            ],
        ),
    )

    # =====================================================
    # Main Area
    # =====================================================

    main_area = ft.Column(

        expand=True,

        spacing=0,

        controls=[

            # Header
            header,

            # Center
            content_area,

            # Footer
            footer,
        ],
    )

    # =====================================================
    # Complete Dashboard
    # =====================================================

    complete_dashboard = ft.Row(

        expand=True,

        spacing=0,

        controls=[

            # Sidebar
            sidebar,

            # Header + Center + Footer
            main_area,
        ],
    )

    # =====================================================
    # Show
    # =====================================================

    page.controls.clear()

    page.controls.append(
        complete_dashboard
    )

    page.update()

    # نمایش داشبورد
    show_dashboard()

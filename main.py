
import flet as ft


# =========================
# In-Memory Users
# =========================

users = {
    "admin": "1234"
}


def main(page: ft.Page):

    page.title = "Authentication App"

    page.window.width = 900
    page.window.height = 650
    page.window.resizable = False

    page.padding = 0

    # =========================
    # Helper
    # =========================

    def show_message(text, color=ft.Colors.RED):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(text),
            bgcolor=color
        )

        page.snack_bar.open = True
        page.update()

    # =========================
    # Dashboard Page
    # =========================

    def dashboard_page(username):

        page.clean()

        # =========================
        # Sidebar
        # =========================

        sidebar = ft.Container(
            width=220,
            bgcolor=ft.Colors.BLUE_GREY_900,
            padding=20,

            content=ft.Column(
                controls=[

                    ft.Text(
                        "My Dashboard",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE,
                    ),

                    ft.Divider(
                        color=ft.Colors.WHITE24
                    ),

                    ft.Container(
                        height=20
                    ),

                    ft.ListTile(
                        leading=ft.Icon(
                            ft.Icons.DASHBOARD,
                            color=ft.Colors.WHITE
                        ),

                        title=ft.Text(
                            "داشبورد",
                            color=ft.Colors.WHITE
                        ),
                    ),

                    ft.ListTile(
                        leading=ft.Icon(
                            ft.Icons.PERSON,
                            color=ft.Colors.WHITE
                        ),

                        title=ft.Text(
                            "پروفایل",
                            color=ft.Colors.WHITE
                        ),
                    ),

                    ft.ListTile(
                        leading=ft.Icon(
                            ft.Icons.SETTINGS,
                            color=ft.Colors.WHITE
                        ),

                        title=ft.Text(
                            "تنظیمات",
                            color=ft.Colors.WHITE
                        ),
                    ),

                    ft.Container(
                        expand=True
                    ),

                    ft.ListTile(
                        leading=ft.Icon(
                            ft.Icons.LOGOUT,
                            color=ft.Colors.WHITE
                        ),

                        title=ft.Text(
                            "خروج",
                            color=ft.Colors.WHITE
                        ),

                        on_click=lambda e: login_page(),
                    ),
                ]
            )
        )

        # =========================
        # Header
        # =========================

        header = ft.Container(
            height=80,

            padding=ft.Padding(
                left=30,
                right=30,
                top=0,
                bottom=0,
            ),

            content=ft.Row(
                controls=[

                    ft.Column(
                        controls=[

                            ft.Text(
                                "داشبورد",
                                size=28,
                                weight=ft.FontWeight.BOLD,
                            ),

                            ft.Text(
                                f"خوش آمدی {username} 👋",
                                size=14,
                                color=ft.Colors.GREY_600,
                            ),
                        ],

                        spacing=3,
                    ),

                    ft.Container(
                        expand=True
                    ),

                    ft.CircleAvatar(
                        content=ft.Icon(
                            ft.Icons.PERSON
                        ),
                        radius=23,
                    ),
                ]
            )
        )

        # =========================
        # Statistics Card 1
        # =========================

        card1 = ft.Container(
            expand=True,
            padding=20,
            bgcolor=ft.Colors.BLUE_50,
            border_radius=15,

            content=ft.Column(
                controls=[

                    ft.Icon(
                        ft.Icons.PEOPLE,
                        size=35,
                        color=ft.Colors.BLUE,
                    ),

                    ft.Text(
                        "کاربران",
                        size=15,
                    ),

                    ft.Text(
                        "120",
                        size=28,
                        weight=ft.FontWeight.BOLD,
                    ),
                ]
            )
        )

        # =========================
        # Statistics Card 2
        # =========================

        card2 = ft.Container(
            expand=True,
            padding=20,
            bgcolor=ft.Colors.GREEN_50,
            border_radius=15,

            content=ft.Column(
                controls=[

                    ft.Icon(
                        ft.Icons.TASK_ALT,
                        size=35,
                        color=ft.Colors.GREEN,
                    ),

                    ft.Text(
                        "وظایف انجام شده",
                        size=15,
                    ),

                    ft.Text(
                        "85",
                        size=28,
                        weight=ft.FontWeight.BOLD,
                    ),
                ]
            )
        )

        # =========================
        # Statistics Card 3
        # =========================

        card3 = ft.Container(
            expand=True,
            padding=20,
            bgcolor=ft.Colors.ORANGE_50,
            border_radius=15,

            content=ft.Column(
                controls=[

                    ft.Icon(
                        ft.Icons.NOTIFICATIONS,
                        size=35,
                        color=ft.Colors.ORANGE,
                    ),

                    ft.Text(
                        "اعلان‌ها",
                        size=15,
                    ),

                    ft.Text(
                        "12",
                        size=28,
                        weight=ft.FontWeight.BOLD,
                    ),
                ]
            )
        )

        # =========================
        # Statistics
        # =========================

        statistics = ft.Row(
            controls=[
                card1,
                card2,
                card3,
            ],

            spacing=20,
        )

        # =========================
        # Recent Activity
        # =========================

        recent_activity = ft.Container(
            margin=ft.Margin(
                left=0,
                right=0,
                top=25,
                bottom=0,
            ),

            padding=20,

            bgcolor=ft.Colors.WHITE,

            border_radius=15,

            content=ft.Column(
                controls=[

                    ft.Text(
                        "فعالیت‌های اخیر",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                    ),

                    ft.Divider(),

                    ft.ListTile(
                        leading=ft.Icon(
                            ft.Icons.LOGIN,
                            color=ft.Colors.GREEN,
                        ),

                        title=ft.Text(
                            "ورود موفق به حساب کاربری"
                        ),

                        subtitle=ft.Text(
                            "همین الان"
                        ),
                    ),

                    ft.ListTile(
                        leading=ft.Icon(
                            ft.Icons.PERSON_ADD,
                            color=ft.Colors.BLUE,
                        ),

                        title=ft.Text(
                            "ایجاد حساب کاربری"
                        ),

                        subtitle=ft.Text(
                            "امروز"
                        ),
                    ),

                    ft.ListTile(
                        leading=ft.Icon(
                            ft.Icons.SETTINGS,
                            color=ft.Colors.ORANGE,
                        ),

                        title=ft.Text(
                            "به‌روزرسانی تنظیمات"
                        ),

                        subtitle=ft.Text(
                            "دیروز"
                        ),
                    ),
                ]
            )
        )

        # =========================
        # Main Content
        # =========================

        main_content = ft.Container(
            expand=True,

            bgcolor=ft.Colors.GREY_100,

            content=ft.Column(
                controls=[

                    header,

                    ft.Container(

                        padding=ft.Padding(
                            left=30,
                            right=30,
                            top=0,
                            bottom=0,
                        ),

                        content=ft.Column(
                            controls=[
                                statistics,
                                recent_activity,
                            ]
                        )
                    ),
                ],

                spacing=0,
            )
        )

        # =========================
        # Final Dashboard Layout
        # =========================

        page.add(
            ft.Row(
                controls=[
                    sidebar,
                    main_content,
                ],

                spacing=0,
                expand=True,
            )
        )

        page.update()

    # =========================
    # Login Page
    # =========================

    def login_page():

        page.clean()

        username = ft.TextField(
            label="نام کاربری",
            hint_text="نام کاربری خود را وارد کنید",
            width=300,
        )

        password = ft.TextField(
            label="رمز عبور",
            hint_text="رمز عبور خود را وارد کنید",

            password=True,
            can_reveal_password=True,

            width=300,
        )

        # =========================
        # Login Function
        # =========================

        def login(e):

            user = username.value.strip()

            passw = password.value

            if not user or not passw:

                show_message(
                    "لطفاً همه فیلدها را پر کنید."
                )

                return

            if user in users and users[user] == passw:

                dashboard_page(user)

            else:

                show_message(
                    "نام کاربری یا رمز عبور اشتباه است."
                )

        # =========================
        # Login UI
        # =========================

        page.add(
            ft.Column(
                controls=[

                    ft.Container(
                        height=50
                    ),

                    ft.Text(
                        "ورود",
                        size=32,
                        weight=ft.FontWeight.BOLD,
                    ),

                    ft.Text(
                        "به حساب کاربری خود وارد شوید",
                        size=16,
                    ),

                    ft.Container(
                        height=30
                    ),

                    username,

                    password,

                    ft.Container(
                        height=10
                    ),

                    ft.ElevatedButton(
                        "ورود",

                        width=300,
                        height=50,

                        on_click=login,
                    ),

                    ft.TextButton(
                        "حساب کاربری ندارید؟ ثبت نام کنید",

                        on_click=lambda e: register_page(),
                    ),
                ],

                horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                spacing=15,
            )
        )

        page.update()

    # =========================
    # Register Page
    # =========================

    def register_page():

        page.clean()

        username = ft.TextField(
            label="نام کاربری",
            hint_text="یک نام کاربری انتخاب کنید",

            width=300,
        )

        password = ft.TextField(
            label="رمز عبور",
            hint_text="رمز عبور خود را وارد کنید",

            password=True,
            can_reveal_password=True,

            width=300,
        )

        confirm_password = ft.TextField(
            label="تکرار رمز عبور",
            hint_text="رمز عبور را دوباره وارد کنید",

            password=True,
            can_reveal_password=True,

            width=300,
        )

        # =========================
        # Register Function
        # =========================

        def register(e):

            user = username.value.strip()

            passw = password.value

            confirm = confirm_password.value

            if not user or not passw or not confirm:

                show_message(
                    "لطفاً همه فیلدها را پر کنید."
                )

                return

            if user in users:

                show_message(
                    "این نام کاربری قبلاً ثبت شده است."
                )

                return

            if passw != confirm:

                show_message(
                    "رمزهای عبور یکسان نیستند."
                )

                return

            users[user] = passw

            dashboard_page(user)

        # =========================
        # Register UI
        # =========================

        page.add(
            ft.Column(
                controls=[

                    ft.Container(
                        height=30
                    ),

                    ft.Text(
                        "ثبت نام",
                        size=32,
                        weight=ft.FontWeight.BOLD,
                    ),

                    ft.Text(
                        "ساخت حساب کاربری جدید",
                        size=16,
                    ),

                    ft.Container(
                        height=25
                    ),

                    username,

                    password,

                    confirm_password,

                    ft.Container(
                        height=10
                    ),

                    ft.ElevatedButton(
                        "ثبت نام",

                        width=300,
                        height=50,

                        on_click=register,
                    ),

                    ft.TextButton(
                        "قبلاً حساب دارید؟ ورود",

                        on_click=lambda e: login_page(),
                    ),
                ],

                horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                spacing=15,
            )
        )

        page.update()

    # =========================
    # Start Application
    # =========================

    login_page()


# =========================
# Run App
# =========================

ft.app(target=main)


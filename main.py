
import flet as ft


# =========================================================
# Users
# =========================================================

users = {
    "admin": {
        "password": "1234",
        "first_name": "Admin",
        "last_name": "User",
        "age": "25",
        "phone": "09000000000",
    }
}


# =========================================================
# Participants
# =========================================================

participants = [
    {
        "first_name": "حمید",
        "last_name": "مغانلو",
        "age": "32",
        "phone": "09120003456",
    },

    {
        "first_name": "امیر محمد",
        "last_name": "دهقانی",
        "age": "21",
        "phone": "09190987654",
    },

    {
        "first_name": "علی",
        "last_name": "فرزین",
        "age": "14",
        "phone": "09013457654",
    },

    {
        "first_name": "یسنا",
        "last_name": "احمدی",
        "age": "20",
        "phone": "09982344567",
    },

    {
        "first_name": "لیلا",
        "last_name": "نورایی",
        "age": "18",
        "phone": "09183452345",
    },
]


# =========================================================
# Main
# =========================================================

def main(page: ft.Page):

    page.title = "Authentication App"

    page.window.width = 1000
    page.window.height = 700
    page.window.resizable = False

    page.padding = 0

    # =====================================================
    # Helper
    # =====================================================

    def show_message(text, color=ft.Colors.RED):

        page.snack_bar = ft.SnackBar(
            content=ft.Text(text),
            bgcolor=color,
        )

        page.snack_bar.open = True

        page.update()

    # =====================================================
    # Home Page
    # =====================================================

    def home_page():

        page.clean()

        # ---------------------------------------------
        # Title
        # ---------------------------------------------

        title = ft.Text(
            "مشخصات شرکت‌کنندگان",
            size=32,
            weight=ft.FontWeight.BOLD,
        )

        subtitle = ft.Text(
            "لیست شرکت‌کنندگان ثبت‌نام شده",
            size=16,
            color=ft.Colors.GREY_600,
        )

        # ---------------------------------------------
        # Table
        # ---------------------------------------------

        rows = []

        for person in participants:

            rows.append(
                ft.DataRow(
                    cells=[

                        ft.DataCell(
                            ft.Text(
                                person["first_name"]
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                person["last_name"]
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                person["age"]
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                person["phone"]
                            )
                        ),
                    ]
                )
            )

        table = ft.DataTable(

            columns=[

                ft.DataColumn(
                    ft.Text(
                        "نام",
                        weight=ft.FontWeight.BOLD,
                    )
                ),

                ft.DataColumn(
                    ft.Text(
                        "نام خانوادگی",
                        weight=ft.FontWeight.BOLD,
                    )
                ),

                ft.DataColumn(
                    ft.Text(
                        "سن",
                        weight=ft.FontWeight.BOLD,
                    )
                ),

                ft.DataColumn(
                    ft.Text(
                        "شماره",
                        weight=ft.FontWeight.BOLD,
                    )
                ),
            ],

            rows=rows,

           border=ft.Border.all(
    1,
    ft.Colors.GREY_300,
),

            border_radius=10,

            heading_row_color=ft.Colors.BLUE_GREY_100,

            column_spacing=60,
        )

        # ---------------------------------------------
        # Main Content
        # ---------------------------------------------

        content = ft.Column(

            controls=[

                ft.Container(
                    height=40
                ),

                title,

                subtitle,

                ft.Container(
                    height=25
                ),

                ft.Container(
                    padding=20,

                    bgcolor=ft.Colors.WHITE,

                    border_radius=15,

                    content=ft.Column(
                        controls=[
                            table
                        ]
                    ),
                ),
            ],

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

            scroll=ft.ScrollMode.AUTO,
        )

        # ---------------------------------------------
        # Page
        # ---------------------------------------------

        page.add(

            ft.Container(

                expand=True,

                bgcolor=ft.Colors.GREY_100,

                padding=30,

                content=content,
            )
        )

        page.update()

    # =====================================================
    # Dashboard
    # =====================================================

    def dashboard_page(username):

        page.clean()

        # ---------------------------------------------
        # Sidebar
        # ---------------------------------------------

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

                    # Home Button
                    ft.ListTile(

                        leading=ft.Icon(
                            ft.Icons.HOME,
                            color=ft.Colors.WHITE,
                        ),

                        title=ft.Text(
                            "صفحه اصلی",
                            color=ft.Colors.WHITE,
                        ),

                        on_click=lambda e: home_page(),
                    ),

                    # Dashboard Button
                    ft.ListTile(

                        leading=ft.Icon(
                            ft.Icons.DASHBOARD,
                            color=ft.Colors.WHITE,
                        ),

                        title=ft.Text(
                            "داشبورد",
                            color=ft.Colors.WHITE,
                        ),

                        on_click=lambda e: dashboard_page(
                            username
                        ),
                    ),

                    # Profile
                    ft.ListTile(

                        leading=ft.Icon(
                            ft.Icons.PERSON,
                            color=ft.Colors.WHITE,
                        ),

                        title=ft.Text(
                            "پروفایل",
                            color=ft.Colors.WHITE,
                        ),
                    ),

                    # Settings
                    ft.ListTile(

                        leading=ft.Icon(
                            ft.Icons.SETTINGS,
                            color=ft.Colors.WHITE,
                        ),

                        title=ft.Text(
                            "تنظیمات",
                            color=ft.Colors.WHITE,
                        ),
                    ),

                    ft.Container(
                        expand=True
                    ),

                    # Logout
                    ft.ListTile(

                        leading=ft.Icon(
                            ft.Icons.LOGOUT,
                            color=ft.Colors.WHITE,
                        ),

                        title=ft.Text(
                            "خروج",
                            color=ft.Colors.WHITE,
                        ),

                        on_click=lambda e: login_page(),
                    ),
                ]
            )
        )

        # ---------------------------------------------
        # Header
        # ---------------------------------------------

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

        # ---------------------------------------------
        # Card 1
        # ---------------------------------------------

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
                        "شرکت‌کنندگان",
                        size=15,
                    ),

                    ft.Text(
                        str(len(participants)),
                        size=28,
                        weight=ft.FontWeight.BOLD,
                    ),
                ]
            )
        )

        # ---------------------------------------------
        # Card 2
        # ---------------------------------------------

        card2 = ft.Container(

            expand=True,

            padding=20,

            bgcolor=ft.Colors.GREEN_50,

            border_radius=15,

            content=ft.Column(

                controls=[

                    ft.Icon(
                        ft.Icons.PERSON_ADD,
                        size=35,
                        color=ft.Colors.GREEN,
                    ),

                    ft.Text(
                        "کاربران ثبت‌نام شده",
                        size=15,
                    ),

                    ft.Text(
                        str(len(users)),
                        size=28,
                        weight=ft.FontWeight.BOLD,
                    ),
                ]
            )
        )

        # ---------------------------------------------
        # Card 3
        # ---------------------------------------------

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

        # ---------------------------------------------
        # Statistics
        # ---------------------------------------------

        statistics = ft.Row(

            controls=[
                card1,
                card2,
                card3,
            ],

            spacing=20,
        )

        # ---------------------------------------------
        # Recent Activity
        # ---------------------------------------------

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
                            "مدیریت شرکت‌کنندگان"
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

        # ---------------------------------------------
        # Main Content
        # ---------------------------------------------

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

        # ---------------------------------------------
        # Dashboard Layout
        # ---------------------------------------------

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

    # =====================================================
    # Login Page
    # =====================================================

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

        # ---------------------------------------------
        # Login Function
        # ---------------------------------------------

        def login(e):

            user = username.value.strip()

            passw = password.value

            if not user or not passw:

                show_message(
                    "لطفاً همه فیلدها را پر کنید."
                )

                return

            if user in users:

                if users[user]["password"] == passw:

                    dashboard_page(user)

                    return

            show_message(
                "نام کاربری یا رمز عبور اشتباه است."
            )

        # ---------------------------------------------
        # Login UI
        # ---------------------------------------------

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

    # =====================================================
    # Register Page
    # =====================================================

    def register_page():

        page.clean()

        # ---------------------------------------------
        # Fields
        # ---------------------------------------------

        first_name = ft.TextField(
            label="نام",
            hint_text="نام خود را وارد کنید",
            width=300,
        )

        last_name = ft.TextField(
            label="نام خانوادگی",
            hint_text="نام خانوادگی خود را وارد کنید",
            width=300,
        )

        age = ft.TextField(
            label="سن",
            hint_text="سن خود را وارد کنید",
            width=300,
            keyboard_type=ft.KeyboardType.NUMBER,
        )

        phone = ft.TextField(
            label="شماره تلفن",
            hint_text="مثلاً 09123456789",
            width=300,
        )

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

        # ---------------------------------------------
        # Register Function
        # ---------------------------------------------

        def register(e):

            fname = first_name.value.strip()

            lname = last_name.value.strip()

            user_age = age.value.strip()

            user_phone = phone.value.strip()

            user = username.value.strip()

            passw = password.value

            confirm = confirm_password.value

            # -----------------------------------------
            # Empty Fields
            # -----------------------------------------

            if (
                not fname
                or not lname
                or not user_age
                or not user_phone
                or not user
                or not passw
                or not confirm
            ):

                show_message(
                    "لطفاً همه فیلدها را پر کنید."
                )

                return

            # -----------------------------------------
            # Username Duplicate
            # -----------------------------------------

            if user in users:

                show_message(
                    "این نام کاربری قبلاً ثبت شده است."
                )

                return

            # -----------------------------------------
            # Password
            # -----------------------------------------

            if passw != confirm:

                show_message(
                    "رمزهای عبور یکسان نیستند."
                )

                return

            # -----------------------------------------
            # Add User
            # -----------------------------------------

            users[user] = {

                "password": passw,

                "first_name": fname,

                "last_name": lname,

                "age": user_age,

                "phone": user_phone,
            }

            # -----------------------------------------
            # Add Participant
            # -----------------------------------------

            participants.append({

                "first_name": fname,

                "last_name": lname,

                "age": user_age,

                "phone": user_phone,
            })

            # -----------------------------------------
            # Go To Dashboard
            # -----------------------------------------

            dashboard_page(user)

        # ---------------------------------------------
        # Register UI
        # ---------------------------------------------

        page.add(

            ft.Column(

                controls=[

                    ft.Container(
                        height=20
                    ),

                    ft.Text(
                        "ثبت نام",
                        size=32,
                        weight=ft.FontWeight.BOLD,
                    ),

                    ft.Text(
                        "مشخصات خود را وارد کنید",
                        size=16,
                    ),

                    ft.Container(
                        height=15
                    ),

                    first_name,

                    last_name,

                    age,

                    phone,

                    username,

                    password,

                    confirm_password,

                    ft.Container(
                        height=5
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

                spacing=10,

                scroll=ft.ScrollMode.AUTO,
            )
        )

        page.update()

    # =====================================================
    # Start
    # =====================================================

    login_page()


# =========================================================
# Run
# =========================================================

ft.app(target=main)

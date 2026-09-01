import flet as ft


# =========================
# اطلاعات کاربران - In Memory
# =========================

users = []

# کاربری که در حال حاضر وارد شده
current_user = None


# =========================
# برنامه اصلی
# =========================

def main(page: ft.Page):

    global current_user

    page.title = "User Management"
    page.window_width = 1000
    page.window_height = 700

    # برای راست چین شدن محیط
    page.rtl = True

    # --------------------------------
    # تابع رفتن به صفحه
    # --------------------------------

    def go(route):
        page.go(route)

    # =================================
    # LOGIN
    # =================================

    def login_page():

        username = ft.TextField(
            label="نام کاربری",
            width=350
        )

        password = ft.TextField(
            label="رمز عبور",
            password=True,
            can_reveal_password=True,
            width=350
        )

        message = ft.Text(
            color=ft.Colors.RED
        )

        def login_click(e):

            global current_user

            found_user = None

            for user in users:
                if (
                    user["username"] == username.value
                    and user["password"] == password.value
                ):
                    found_user = user
                    break

            if found_user:

                current_user = found_user

                # ورود موفق
                page.go("/welcome")

            else:
                message.value = "نام کاربری یا رمز عبور اشتباه است"
                page.update()

        def register_click(e):
            page.go("/register")

        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "ورود به حساب کاربری",
                        size=32,
                        weight=ft.FontWeight.BOLD
                    ),

                    ft.Text(
                        "اگر حساب کاربری دارید وارد شوید"
                    ),

                    ft.Divider(),

                    username,
                    password,

                    ft.ElevatedButton(
                        "ورود",
                        width=350,
                        height=45,
                        on_click=login_click
                    ),

                    message,

                    ft.Text("حساب کاربری ندارید؟"),

                    ft.TextButton(
                        "ثبت نام",
                        on_click=register_click
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=15
            ),
            alignment=ft.alignment.center,
            expand=True
        )

    # =================================
    # REGISTER
    # =================================

    def register_page():

        first_name = ft.TextField(
            label="نام",
            width=350
        )

        last_name = ft.TextField(
            label="نام خانوادگی",
            width=350
        )

        username = ft.TextField(
            label="نام کاربری",
            width=350
        )

        password = ft.TextField(
            label="رمز عبور",
            password=True,
            can_reveal_password=True,
            width=350
        )

        age = ft.TextField(
            label="سن",
            width=350,
            keyboard_type=ft.KeyboardType.NUMBER
        )

        phone = ft.TextField(
            label="شماره همراه",
            width=350
        )

        message = ft.Text(
            color=ft.Colors.RED
        )

        def register_click(e):

            # بررسی خالی نبودن اطلاعات
            if (
                not first_name.value
                or not last_name.value
                or not username.value
                or not password.value
                or not age.value
                or not phone.value
            ):
                message.value = "لطفاً تمام اطلاعات را وارد کنید"
                page.update()
                return

            # بررسی تکراری نبودن username
            for user in users:

                if user["username"] == username.value:

                    message.value = "این نام کاربری قبلاً ثبت شده است"
                    page.update()
                    return

            # ساخت کاربر جدید
            new_user = {

                "first_name": first_name.value,

                "last_name": last_name.value,

                "username": username.value,

                "password": password.value,

                "age": age.value,

                "phone": phone.value
            }

            # اضافه کردن به حافظه
            users.append(new_user)

            # کاربر فعلی
            global current_user
            current_user = new_user

            # رفتن به خوش آمدگویی
            page.go("/welcome")

        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "ثبت نام",
                        size=32,
                        weight=ft.FontWeight.BOLD
                    ),

                    first_name,
                    last_name,
                    username,
                    password,
                    age,
                    phone,

                    ft.ElevatedButton(
                        "ثبت نام",
                        width=350,
                        height=45,
                        on_click=register_click
                    ),

                    message,

                    ft.TextButton(
                        "قبلاً حساب دارم - ورود",
                        on_click=lambda e: page.go("/")
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                scroll=ft.ScrollMode.AUTO
            ),
            alignment=ft.alignment.center,
            expand=True
        )

    # =================================
    # WELCOME
    # =================================

    def welcome_page():

        if current_user is None:
            page.go("/")
            return ft.Container()

        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "خوش آمدید 🌷",
                        size=40,
                        weight=ft.FontWeight.BOLD
                    ),

                    ft.Text(
                        f"{current_user['first_name']} عزیز، خوش آمدی",
                        size=24
                    ),

                    ft.Text(
                        "ثبت نام شما با موفقیت انجام شد.",
                        size=18
                    ),

                    ft.ElevatedButton(
                        "مشاهده پروفایل",
                        width=250,
                        height=50,
                        on_click=lambda e: page.go("/profile")
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20
            ),
            alignment=ft.alignment.center,
            expand=True
        )

    # =================================
    # PROFILE
    # =================================

    def profile_page():

        if current_user is None:
            page.go("/")
            return ft.Container()

        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "پروفایل کاربری",
                        size=35,
                        weight=ft.FontWeight.BOLD
                    ),

                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(
                                    f"نام: {current_user['first_name']}",
                                    size=20
                                ),

                                ft.Text(
                                    f"نام کاربری: {current_user['username']}",
                                    size=20
                                ),

                                ft.Text(
                                    f"شماره همراه: {current_user['phone']}",
                                    size=20
                                )
                            ],
                            spacing=15
                        ),
                        padding=30,
                        border=ft.border.all(1),
                        border_radius=15,
                        width=450
                    ),

                    ft.ElevatedButton(
                        "داشبورد",
                        width=250,
                        height=50,
                        on_click=lambda e: page.go("/dashboard")
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=25
            ),
            alignment=ft.alignment.center,
            expand=True
        )

    # =================================
    # DASHBOARD
    # =================================

    def dashboard_page():

        if current_user is None:
            page.go("/")
            return ft.Container()

        # ساخت جدول کاربران
        rows = []

        for user in users:

            rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Text(user["first_name"])
                        ),

                        ft.DataCell(
                            ft.Text(user["last_name"])
                        ),

                        ft.DataCell(
                            ft.Text(user["username"])
                        ),

                        ft.DataCell(
                            ft.Text(user["password"])
                        ),

                        ft.DataCell(
                            ft.Text(user["age"])
                        ),

                        ft.DataCell(
                            ft.Text(user["phone"])
                        )
                    ]
                )
            )

        table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("نام")),
                ft.DataColumn(ft.Text("نام خانوادگی")),
                ft.DataColumn(ft.Text("نام کاربری")),
                ft.DataColumn(ft.Text("رمز عبور")),
                ft.DataColumn(ft.Text("سن")),
                ft.DataColumn(ft.Text("شماره همراه"))
            ],

            rows=rows
        )

        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "داشبورد",
                        size=35,
                        weight=ft.FontWeight.BOLD
                    ),

                    ft.Text(
                        "اطلاعات کاربران ثبت نام شده",
                        size=20
                    ),

                    ft.Container(
                        content=ft.Row(
                            [table],
                            scroll=ft.ScrollMode.AUTO
                        ),
                        padding=20,
                        border=ft.border.all(1),
                        border_radius=15
                    ),

                    ft.ElevatedButton(
                        "بازگشت به پروفایل",
                        on_click=lambda e: page.go("/profile")
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.AUTO
            ),
            padding=30,
            expand=True
        )

    # =================================
    # ROUTING
    # =================================

    def route_change(e):

        page.controls.clear()

        if page.route == "/":
            page.add(login_page())

        elif page.route == "/register":
            page.add(register_page())

        elif page.route == "/welcome":
            page.add(welcome_page())

        elif page.route == "/profile":
            page.add(profile_page())

        elif page.route == "/dashboard":
            page.add(dashboard_page())

        else:
            page.go("/")

        page.update()

    # اتصال Routing
    page.on_route_change = route_change

    # شروع برنامه
    page.go("/")


# اجرای برنامه
ft.run(main)
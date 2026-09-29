import flet as ft


# -------------------------
# In-Memory Users
# -------------------------
# =========================
# اطلاعات کاربران - In Memory
# =========================

users = []

users = {
    "zahra": "1234"
}
# کاربری که در حال حاضر وارد شده
current_user = None


# =========================
# برنامه اصلی
# =========================

def main(page: ft.Page):

    page.title = "Login App"
    global current_user

    page.title = "User Management"
    page.window_width = 1000
    page.window_height = 700

    # برای راست چین شدن محیط
    page.rtl = True

    # --------------------------------
    # تابع رفتن به صفحه
    # --------------------------------

    # -------------------------
    # Login Page
    # -------------------------
    def go(route):
        page.go(route)

    def login_view():
    # =================================
    # LOGIN
    # =================================

    def login_page():

        username = ft.TextField(
            label="Username",
            width=300
            label="نام کاربری",
            width=350
        )

        password = ft.TextField(
            label="Password",
            label="رمز عبور",
            password=True,
            width=300
            can_reveal_password=True,
            width=350
        )

        message = ft.Text(
            color=ft.Colors.RED
        )

        def login(e):
        def login_click(e):

            global current_user

            user = username.value
            passwd = password.value
            found_user = None

            if user in users and users[user] == passwd:
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
                page.navigate("/welcome")

            elif user not in users:

                message.value = "Account not found"
                page.update()
                page.go("/welcome")

            else:

                message.value = "Wrong password"
                message.value = "نام کاربری یا رمز عبور اشتباه است"
                page.update()

        return ft.View(
            route="/",
            controls=[
                ft.Column(
                    controls=[
                        ft.Text(
                            "Login",
                            size=30,
                            weight=ft.FontWeight.BOLD
                        ),
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

                        username,
                        password,
                    ft.Text(
                        "اگر حساب کاربری دارید وارد شوید"
                    ),

                    ft.Divider(),

                    username,
                    password,

                        message,
                    ft.ElevatedButton(
                        "ورود",
                        width=350,
                        height=45,
                        on_click=login_click
                    ),

                    message,

                        ft.Button(
                            "Login",
                            on_click=login
                        ),
                    ft.Text("حساب کاربری ندارید؟"),

                        ft.TextButton(
                            "Create account",
                            on_click=lambda e: page.navigate("/register")
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
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

    # -------------------------
    # Register Page
    # -------------------------
        first_name = ft.TextField(
            label="نام",
            width=350
        )

    def register_view():
        last_name = ft.TextField(
            label="نام خانوادگی",
            width=350
        )

        username = ft.TextField(
            label="Username",
            width=300
            label="نام کاربری",
            width=350
        )

        password = ft.TextField(
            label="Password",
            label="رمز عبور",
            password=True,
            width=300
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

        def register(e):

            user = username.value
            passwd = password.value
        def register_click(e):

            if not user or not passwd:

                message.value = "Fill all fields"
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

            if user in users:
            # بررسی تکراری نبودن username
            for user in users:

                message.value = "Username already exists"
                page.update()
                return
                if user["username"] == username.value:

                    message.value = "این نام کاربری قبلاً ثبت شده است"
                    page.update()
                    return

            # ذخیره در حافظه
            users[user] = passwd
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

            # رفتن به Welcome
            page.navigate("/welcome")
            # کاربر فعلی
            global current_user
            current_user = new_user

        return ft.View(
            route="/register",
            controls=[
                ft.Column(
                    controls=[
                        ft.Text(
                            "Register",
                            size=30,
                            weight=ft.FontWeight.BOLD
                        ),
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

                        username,
                        password,
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
                    message,

                        ft.Button(
                            "Register",
                            on_click=register
                        ),

                        ft.TextButton(
                            "Back to Login",
                            on_click=lambda e: page.navigate("/")
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
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

    # -------------------------
    # Welcome Page
    # -------------------------
    def welcome_page():

    def welcome_view():
        if current_user is None:
            page.go("/")
            return ft.Container()

        return ft.View(
            route="/welcome",
            controls=[
                ft.Column(
                    controls=[
                        ft.Text(
                            "Welcome!",
                            size=35,
                            weight=ft.FontWeight.BOLD
                        ),
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

                        ft.Text(
                            "خوش آمدید 🌹",
                            size=20
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

                        ft.Button(
                            "Logout",
                            on_click=lambda e: page.navigate("/")
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
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
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


    # -------------------------
    # Routing
    # -------------------------
    # =================================
    # ROUTING
    # =================================

    def route_change(e):

        page.views.clear()
        page.controls.clear()

        if page.route == "/":
            page.views.append(login_view())
            page.add(login_page())

        elif page.route == "/register":
            page.views.append(register_view())
            page.add(register_page())

        elif page.route == "/welcome":
            page.views.append(welcome_view())
            page.add(welcome_page())

        elif page.route == "/profile":
            page.add(profile_page())

        elif page.route == "/dashboard":
            page.add(dashboard_page())

        else:
            page.views.append(login_view())
            page.go("/")

        page.update()


    # فعال کردن Routing
    # اتصال Routing
    page.on_route_change = route_change

    # اجرای صفحه اول
    route_change(None)
    # شروع برنامه
    page.go("/")


# اجرای برنامه
ft.run(main)

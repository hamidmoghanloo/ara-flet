import flet as ft


# -------------------------
# In-Memory Users
# -------------------------

users = {
    "zahra": "1234"
}


def main(page: ft.Page):

    page.title = "Login App"

    # -------------------------
    # Login Page
    # -------------------------

    def login_view():

        username = ft.TextField(
            label="Username",
            width=300
        )

        password = ft.TextField(
            label="Password",
            password=True,
            width=300
        )

        message = ft.Text(
            color=ft.Colors.RED
        )

        def login(e):

            user = username.value
            passwd = password.value

            if user in users and users[user] == passwd:

                # ورود موفق
                page.navigate("/welcome")

            elif user not in users:

                message.value = "Account not found"
                page.update()

            else:

                message.value = "Wrong password"
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

                        username,
                        password,

                        message,

                        ft.Button(
                            "Login",
                            on_click=login
                        ),

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
        )


    # -------------------------
    # Register Page
    # -------------------------

    def register_view():

        username = ft.TextField(
            label="Username",
            width=300
        )

        password = ft.TextField(
            label="Password",
            password=True,
            width=300
        )

        message = ft.Text(
            color=ft.Colors.RED
        )

        def register(e):

            user = username.value
            passwd = password.value

            if not user or not passwd:

                message.value = "Fill all fields"
                page.update()
                return

            if user in users:

                message.value = "Username already exists"
                page.update()
                return

            # ذخیره در حافظه
            users[user] = passwd

            # رفتن به Welcome
            page.navigate("/welcome")

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

                        username,
                        password,

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
        )


    # -------------------------
    # Welcome Page
    # -------------------------

    def welcome_view():

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

                        ft.Text(
                            "خوش آمدید 🌹",
                            size=20
                        ),

                        ft.Button(
                            "Logout",
                            on_click=lambda e: page.navigate("/")
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )


    # -------------------------
    # Routing
    # -------------------------

    def route_change(e):

        page.views.clear()

        if page.route == "/":
            page.views.append(login_view())

        elif page.route == "/register":
            page.views.append(register_view())

        elif page.route == "/welcome":
            page.views.append(welcome_view())

        else:
            page.views.append(login_view())

        page.update()


    # فعال کردن Routing
    page.on_route_change = route_change

    # اجرای صفحه اول
    route_change(None)


# اجرای برنامه
ft.run(main)
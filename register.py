import flet as ft


# =========================================================
# In-Memory Users
# =========================================================

users = {}


# =========================================================
# Main
# =========================================================

def main(page: ft.Page):

    # -----------------------------------------------------
    # Page Settings
    # -----------------------------------------------------

    page.title = "Login App"
    page.bgcolor = "#F5F7FB"
    page.padding = 0


    # =====================================================
    # Show Message
    # =====================================================

    def show_message(message, color="#EF4444"):

        page.show_dialog(
            ft.SnackBar(
                content=ft.Text(
                    message,
                    color="white",
                ),
                bgcolor=color,
            )
        )


    # =====================================================
    # Create Input
    # =====================================================

    def create_input(
        label,
        hint="",
        password=False,
        keyboard_type=None,
    ):

        return ft.TextField(
            label=label,
            hint_text=hint,
            password=password,
            can_reveal_password=password,
            keyboard_type=keyboard_type,
            text_align=ft.TextAlign.RIGHT,
            border_radius=10,
            border_color="#D1D5DB",
            focused_border_color="#4F46E5",
            bgcolor="white",
        )


    # =====================================================
    # Page Container
    # =====================================================

    def page_container(content):

        return ft.Container(
            expand=True,
            alignment=ft.Alignment.CENTER,
            padding=20,

            content=ft.Container(
                width=420,
                padding=35,
                border_radius=20,
                bgcolor="white",

                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=20,
                    color="#22000000",
                ),

                content=content,
            ),
        )


    # =====================================================
    # LOGIN PAGE
    # =====================================================

    def login_page():

        email = create_input(
            "ایمیل",
            "example@gmail.com",
            keyboard_type=ft.KeyboardType.EMAIL,
        )

        password = create_input(
            "رمز عبور",
            "رمز عبور خود را وارد کنید",
            password=True,
        )


        # -------------------------------------------------
        # Login
        # -------------------------------------------------

        def login(e):

            email_value = email.value.strip().lower()
            password_value = password.value


            # Empty fields
            if not email_value or not password_value:

                show_message(
                    "لطفاً ایمیل و رمز عبور را وارد کنید."
                )

                return


            # User doesn't exist
            if email_value not in users:

                show_message(
                    "این حساب وجود ندارد. ابتدا ثبت نام کنید."
                )

                register_page()

                return


            # Wrong password
            if users[email_value]["password"] != password_value:

                show_message(
                    "رمز عبور اشتباه است."
                )

                return


            # Login successful
            welcome_page(
                users[email_value]
            )


        # -------------------------------------------------
        # Go Register
        # -------------------------------------------------

        def go_register(e):

            register_page()


        # -------------------------------------------------
        # Login UI
        # ---------------------------------

        content = ft.Column(

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

            spacing=15,

            controls=[

                ft.Icon(
                    ft.Icons.LOCK_PERSON,
                    size=65,
                    color="#4F46E5",
                ),

                ft.Text(
                    "ورود",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color="#111827",
                ),

                ft.Text(
                    "وارد حساب کاربری خود شوید",
                    size=14,
                    color="#6B7280",
                    text_align=ft.TextAlign.CENTER,
                ),

                ft.Container(
                    height=10
                ),

                email,

                password,

                ft.Container(
                    height=5
                ),

                ft.ElevatedButton(
                    "ورود",
                    width=300,
                    height=50,
                    bgcolor="#4F46E5",
                    color="white",
                    on_click=login,
                ),

                ft.Row(

                    alignment=ft.MainAxisAlignment.CENTER,

                    controls=[

                        ft.Text(
                            "حساب کاربری ندارید؟",
                            color="#6B7280",
                        ),

                        ft.TextButton(
                            "ثبت نام",
                            on_click=go_register,
                        ),

                    ],
                ),
            ],
        )


        page.controls.clear()

        page.controls.append(
            page_container(content)
        )

        page.update()


    # =====================================================
    # REGISTER PAGE
    # =====================================================

    def register_page():

        name = create_input(
            "نام",
            "نام خود را وارد کنید",
        )

        email = create_input(
            "ایمیل",
            "example@gmail.com",
            keyboard_type=ft.KeyboardType.EMAIL,
        )

        password = create_input(
            "رمز عبور",
            "حداقل 4 کاراکتر",
            password=True,
        )

        confirm_password = create_input(
            "تکرار رمز عبور",
            "رمز عبور را دوباره وارد کنید",
            password=True,
        )


        # -------------------------------------------------
        # Register
        # -------------------------------------------------

        def register(e):

            name_value = name.value.strip()
            email_value = email.value.strip().lower()
            password_value = password.value
            confirm_value = confirm_password.value


            # Name
            if not name_value:

                show_message(
                    "لطفاً نام خود را وارد کنید."
                )

                return


            # Email
            if not email_value:

                show_message(
                    "لطفاً ایمیل خود را وارد کنید."
                )

                return


            # Email validation
            if "@" not in email_value:

                show_message(
                    "ایمیل وارد شده معتبر نیست."
                )

                return


            # Password
            if len(password_value) < 4:

                show_message(
                    "رمز عبور باید حداقل 4 کاراکتر باشد."
                )

                return


            # Confirm password
            if password_value != confirm_value:

                show_message(
                    "رمز عبور و تکرار آن یکسان نیستند."
                )

                return


            # Existing user
            if email_value in users:

                show_message(
                    "این ایمیل قبلاً ثبت نام کرده است."
                )

                return


            # -------------------------------------------------
            # Save User In Memory
            # -------------------------------------------------

            users[email_value] = {

                "name": name_value,

                "password": password_value,
            }


            # -------------------------------------------------
            # Go Welcome
            # -------------------------------------------------

            welcome_page(
                users[email_value]
            )


        # -------------------------------------------------
        # Back To Login
        # -------------------------------------------------

        def go_login(e):

            login_page()


        # -------------------------------------------------
        # Register UI
        # -------------------------------------------------

        content = ft.Column(

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

            spacing=14,

            controls=[

                ft.Icon(
                    ft.Icons.PERSON_ADD,
                    size=65,
                    color="#4F46E5",
                ),

                ft.Text(
                    "ثبت نام",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color="#111827",
                ),

                ft.Text(
                    "یک حساب کاربری جدید بسازید",
                    size=14,
                    color="#6B7280",
                    text_align=ft.TextAlign.CENTER,
                ),

                ft.Container(
                    height=5
                ),

                name,

                email,

                password,

                confirm_password,

                ft.Container(
                    height=5
                ),

                ft.ElevatedButton(
                    "ثبت نام",
                    width=300,
                    height=50,
                    bgcolor="#4F46E5",
                    color="white",
                    on_click=register,
                ),

                ft.Row(

                    alignment=ft.MainAxisAlignment.CENTER,

                    controls=[

                        ft.Text(
                            "قبلاً حساب دارید؟",
                            color="#6B7280",
                        ),

                        ft.TextButton(
                            "ورود",
                            on_click=go_login,
                        ),
                    ],
                ),
            ],
        )


        page.controls.clear()

        page.controls.append(
            page_container(content)
        )

        page.update()


    # =====================================================
    # WELCOME PAGE
    # =====================================================

    def welcome_page(user):

        name = user["name"]


        # -------------------------------------------------
        # Logout
        # -------------------------------------------------

        def logout(e):

            login_page()


        # -------------------------------------------------
        # Welcome UI
        # -------------------------------------------------

        content = ft.Column(

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

            spacing=20,

            controls=[

                ft.Container(

                    width=100,
                    height=100,

                    border_radius=50,

                    bgcolor="#DCFCE7",

                    alignment=ft.Alignment.CENTER,

                    content=ft.Icon(
                        ft.Icons.CHECK_CIRCLE,
                        size=60,
                        color="#16A34A",
                    ),
                ),

                ft.Text(
                    "خوش آمدید 🎉",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color="#111827",
                ),

                ft.Text(
                    f"سلام {name} 👋",
                    size=22,
                    weight=ft.FontWeight.W_500,
                    color="#374151",),

                ft.Text(
                    "ورود شما با موفقیت انجام شد.",
                    size=15,
                    color="#6B7280",
                    text_align=ft.TextAlign.CENTER,
                ),

                ft.Container(
                    height=10
                ),

                ft.ElevatedButton(
                    "خروج از حساب",
                    width=300,
                    height=50,
                    bgcolor="#EF4444",
                    color="white",
                    on_click=logout,
                ),
            ],
        )


        page.controls.clear()

        page.controls.append(
            page_container(content)
        )

        page.update()


    # =====================================================
    # START
    # =====================================================

    login_page()


# =========================================================
# Run Application
# =========================================================

if __name__ == "__main__":
    ft.run(main)
import re
import flet as ft

# اطلاعات کاربران فقط در حافظه است و با بستن برنامه پاک می‌شود.
USERS = {}


def main(page: ft.Page):
    page.title = "سامانه ورود"
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT

    current_user = {"username": ""}

    root = ft.Container(expand=True)
    page.add(root)

    def primary_button(text, on_click):
        return ft.Row(
            controls=[
                ft.FilledButton(
                    content=text,
                    on_click=on_click,
                    expand=True,
                    height=52,
                    style=ft.ButtonStyle(
                        bgcolor="#4F46E5",
                        color="#FFFFFF",
                        shape=ft.RoundedRectangleBorder(radius=14),
                    ),
                )
            ]
        )

    def input_field(label, icon, password=False, on_change=None, autofocus=False):
        return ft.TextField(
            label=label,
            prefix_icon=icon,
            password=password,
            can_reveal_password=password,
            on_change=on_change,
            autofocus=autofocus,
            rtl=True,
            text_align=ft.TextAlign.RIGHT,
            height=58,
            bgcolor="#F8FAFC",
            filled=True,
            border=ft.InputBorder.OUTLINE,
            border_radius=14,
            border_color="#E2E8F0",
            focused_border_color="#4F46E5",
            cursor_color="#4F46E5",
            color="#0F172A",
        )

    def logo(icon):
        return ft.Container(
            width=70,
            height=70,
            border_radius=35,
            bgcolor="#EEF2FF",
            alignment=ft.Alignment.CENTER,
            content=ft.Icon(icon, size=34, color="#4F46E5"),
        )

    def create_screen(content):
        return ft.Container(
            expand=True,
            gradient=ft.LinearGradient(
                begin=ft.Alignment.TOP_LEFT,
                end=ft.Alignment.BOTTOM_RIGHT,
                colors=["#EEF2FF", "#F5F3FF", "#E0F2FE"],
            ),
            content=ft.SafeArea(
                expand=True,
                content=ft.Column(
                    expand=True,
                    scroll=ft.ScrollMode.AUTO,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            width=430,
                            margin=20,
                            padding=32,
                            bgcolor="#FFFFFF",
                            border_radius=26,
                            shadow=ft.BoxShadow(
                                blur_radius=25,
                                spread_radius=1,
                                color="#220F172A",
                                offset=ft.Offset(0, 10),
                            ),
                            content=content,
                        )
                    ],
                ),
            ),
        )

    def show_screen(content):
        root.content = create_screen(content)
        page.update()

    def password_score(password):
        if not password:
            return 0

        score = 0
        score += len(password) >= 6
        score += len(password) >= 8
        score += bool(re.search(r"[a-z]", password))
        score += bool(re.search(r"[A-Z]", password))
        score += bool(re.search(r"\d", password))
        score += bool(re.search(r"[^A-Za-z0-9]", password))

        return score

    def show_login():
        username = input_field(
            "نام کاربری",
            ft.Icons.PERSON,
            autofocus=True,
        )

        password = input_field(
            "رمز عبور",
            ft.Icons.LOCK,
            password=True,
        )

        error_text = ft.Text("", size=13, color="#DC2626")

        def login(_):
            name = username.value.strip()
            pwd = password.value

            if not name or not pwd:
                error_text.value = "نام کاربری و رمز عبور را وارد کنید."
                page.update()
                return

            if USERS.get(name) != pwd:
                error_text.value = "حسابی با این اطلاعات پیدا نشد."
                page.update()
                return

            current_user["username"] = name
            show_welcome()

        password.on_submit = login

        show_screen(
            ft.Column(
                tight=True,
                rtl=True,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15,
                controls=[
                    logo(ft.Icons.LOCK),
                    ft.Text(
                        "خوش آمدید",
                        size=28,
                        weight=ft.FontWeight.BOLD,
                        color="#0F172A",
                    ),
                    ft.Text(
                        "برای ورود، اطلاعات حساب خود را وارد کنید.",
                        size=14,
                        color="#64748B",
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Container(height=8),
                    username,
                    password,
                    error_text,
                    primary_button("ورود به حساب", login),
                    ft.Divider(color="#E2E8F0"),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text("حساب کاربری ندارید؟", color="#64748B"),
                            ft.TextButton(
                                content="ثبت نام",
                                on_click=lambda _: show_register(),
                                style=ft.ButtonStyle(color="#4F46E5"),
                            ),
                        ],
                    ),
                ],
            )
        )

    def show_register():
        username = input_field(
            "نام کاربری",
            ft.Icons.PERSON,
            autofocus=True,
        )

        password = input_field(
            "رمز عبور",
            ft.Icons.LOCK,
            password=True,
        )

        confirm_password = input_field(
            "تکرار رمز عبور",
            ft.Icons.LOCK,
            password=True,
        )

        strength_text = ft.Text(
            "قدرت رمز: هنوز رمزی وارد نشده",
            size=13,
            color="#64748B",
        )

        dots = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8,
            controls=[
                ft.Container(
                    width=14,
                    height=14,
                    border_radius=14,
                    bgcolor="#E2E8F0",
                )
                for _ in range(6)
            ],
        )

        error_text = ft.Text("", size=13, color="#DC2626")

        levels = [
            "",
            "خیلی ضعیف",
            "ضعیف",
            "متوسط",
            "خوب",
            "قوی",
            "خیلی قوی",
        ]

        def update_strength(_):
            score = password_score(password.value)

            if score == 0:
                strength_text.value = "قدرت رمز: هنوز رمزی وارد نشده"
            else:
                strength_text.value = f"قدرت رمز: {levels[score]} ({score} از 6)"

            for index, dot in enumerate(dots.controls):
                dot.bgcolor = "#22C55E" if index < score else "#E2E8F0"

            page.update()

        password.on_change = update_strength

        def register(_):
            name = username.value.strip()
            pwd = password.value
            confirm = confirm_password.value

            if len(name) < 3:
                error_text.value = "نام کاربری باید حداقل ۳ کاراکتر باشد."
                page.update()
                return

            if name in USERS:
                error_text.value = "این نام کاربری قبلاً ثبت شده است."
                page.update()
                return

            if len(pwd) < 6:
                error_text.value = "رمز عبور باید حداقل ۶ کاراکتر باشد."
                page.update()
                return

            if pwd != confirm:
                error_text.value = "تکرار رمز عبور درست نیست."
                page.update()
                return

            USERS[name] = pwd
            current_user["username"] = name
            show_welcome()

        confirm_password.on_submit = register

        show_screen(
            ft.Column(
                tight=True,
                rtl=True,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=14,
                controls=[
                    logo(ft.Icons.PERSON_ADD),
                    ft.Text(
                        "ساخت حساب کاربری",
                        size=27,
                        weight=ft.FontWeight.BOLD,
                        color="#0F172A",
                    ),
                    ft.Text(
                        "اطلاعات زیر را وارد کنید تا حساب شما ساخته شود.",
                        size=14,
                        color="#64748B",
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Container(height=6),
                    username,
                    password,
                    ft.Column(
                        tight=True,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=8,
                        controls=[dots, strength_text],
                    ),
                    confirm_password,
                    error_text,
                    primary_button("ثبت نام و ادامه", register),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text("قبلاً ثبت نام کرده‌اید؟", color="#64748B"),
                            ft.TextButton(
                                content="ورود",
                                on_click=lambda _: show_login(),
                                style=ft.ButtonStyle(color="#4F46E5"),
                            ),
                        ],
                    ),
                ],
            )
        )

    def show_welcome():
        def logout(_):
            current_user["username"] = ""
            show_login()

        show_screen(
            ft.Column(
                tight=True,
                rtl=True,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=18,
                controls=[
                    ft.Container(
                        width=82,
                        height=82,
                        border_radius=41,
                        bgcolor="#DCFCE7",
                        alignment=ft.Alignment.CENTER,
                        content=ft.Icon(
                            ft.Icons.CHECK_CIRCLE,
                            size=46,
                            color="#16A34A",
                        ),
                    ),
                    ft.Text(
                        f"سلام {current_user['username']} 👋",
                        size=29,
                        weight=ft.FontWeight.BOLD,
                        color="#0F172A",
                    ),
                    ft.Text(
                        "حساب کاربری شما با موفقیت ساخته شد.",
                        size=15,
                        color="#64748B",
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Container(
                        padding=22,
                        border_radius=18,
                        bgcolor="#F8FAFC",
                        content=ft.Column(
                            tight=True,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=8,
                            controls=[
                                ft.Icon(
                                    ft.Icons.VERIFIED_USER,
                                    size=28,
                                    color="#4F46E5",
                                ),
                                ft.Text(
                                    "ورود شما با موفقیت انجام شد",
                                    weight=ft.FontWeight.BOLD,
                                    color="#334155",
                                ),
                                ft.Text(
                                    "اطلاعات تا زمان باز بودن برنامه در حافظه نگه‌داری می‌شوند.",
                                    size=12,
                                    color="#64748B",
                                    text_align=ft.TextAlign.CENTER,
                                ),
                            ],
                        ),
                    ),
                    primary_button("خروج از حساب", logout),
                ],
            )
        )

    show_login()


if __name__ == "__main__":
    ft.run(main)
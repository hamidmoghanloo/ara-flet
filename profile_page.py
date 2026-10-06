import flet as ft

from user_data import get_profile, set_profile


def show_profile(page, username, on_saved, on_back):
    """
    صفحه اطلاعات کاربر
    """

    profile = get_profile(username)

    name_field = ft.TextField(
        label="نام و نام خانوادگی",
        hint_text="مثلاً: علی احمدی",
        prefix_icon=ft.Icons.PERSON,
        value=profile.get("name", ""),
        rtl=True,
        text_align=ft.TextAlign.RIGHT,
        height=58,
        bgcolor="#F8FAFC",
        filled=True,
        border=ft.InputBorder.OUTLINE,
        border_radius=14,
        border_color="#E2E8F0",
        focused_border_color="#4F46E5",
    )

    username_field = ft.TextField(
        label="نام کاربری",
        value=username,
        prefix_icon=ft.Icons.ACCOUNT_CIRCLE,
        read_only=True,
        rtl=True,
        text_align=ft.TextAlign.RIGHT,
        height=58,
        bgcolor="#F1F5F9",
        filled=True,
        border=ft.InputBorder.OUTLINE,
        border_radius=14,
        border_color="#E2E8F0",
    )

    phone_field = ft.TextField(
        label="شماره همراه",
        hint_text="مثلاً: 09123456789",
        prefix_icon=ft.Icons.PHONE,
        value=profile.get("phone", ""),
        keyboard_type=ft.KeyboardType.PHONE,
        rtl=True,
        text_align=ft.TextAlign.RIGHT,
        height=58,
        bgcolor="#F8FAFC",
        filled=True,
        border=ft.InputBorder.OUTLINE,
        border_radius=14,
        border_color="#E2E8F0",
        focused_border_color="#4F46E5",
    )

    error_text = ft.Text(
        "",
        size=13,
        color="#DC2626",
        text_align=ft.TextAlign.RIGHT,
    )

    success_text = ft.Text(
        "",
        size=13,
        color="#16A34A",
        text_align=ft.TextAlign.RIGHT,
    )

    def save_profile(_):
        name = name_field.value.strip()
        phone = phone_field.value.strip()

        if not name:
            error_text.value = "لطفاً نام و نام خانوادگی را وارد کنید."
            success_text.value = ""
            page.update()
            return

        if not phone:
            error_text.value = "لطفاً شماره همراه را وارد کنید."
            success_text.value = ""
            page.update()
            return

        if not phone.isdigit():
            error_text.value = "شماره همراه باید فقط شامل اعداد باشد."
            success_text.value = ""
            page.update()
            return

        if len(phone) != 11 or not phone.startswith("09"):
            error_text.value = "شماره همراه معتبر نیست."
            success_text.value = ""
            page.update()
            return

        set_profile(
            username=username,
            name=name,
            phone=phone,
        )

        error_text.value = ""
        success_text.value = "اطلاعات با موفقیت ذخیره شد."

        page.update()

        # رفتن به داشبورد
        on_saved()

    def back(_):
        on_back()

    content = ft.Column(
        tight=True,
        rtl=True,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15,
        controls=[
            ft.Container(
                width=75,
                height=75,
                border_radius=38,
                bgcolor="#EEF2FF",
                alignment=ft.Alignment.CENTER,
                content=ft.Icon(
                    ft.Icons.PERSON,
                    size=38,
                    color="#4F46E5",
                ),
            ),

            ft.Text(
                "اطلاعات کاربر",
                size=28,
                weight=ft.FontWeight.BOLD,
                color="#0F172A",
            ),

            ft.Text(
                "اطلاعات پروفایل خود را وارد کنید.",
                size=14,
                color="#64748B",
                text_align=ft.TextAlign.CENTER,
            ),

            ft.Container(height=8),

            name_field,

            username_field,

            phone_field,

            error_text,

            success_text,

            ft.FilledButton(
                content="ذخیره اطلاعات و ورود به داشبورد",
                icon=ft.Icons.SAVE,
                on_click=save_profile,
                height=52,
                width=390,
                style=ft.ButtonStyle(
                    bgcolor="#4F46E5",
                    color="#FFFFFF",
                    shape=ft.RoundedRectangleBorder(radius=14),
                ),
            ),

            ft.TextButton(
                content="بازگشت",
                icon=ft.Icons.ARROW_BACK,
                on_click=back,
                style=ft.ButtonStyle(
                    color="#64748B",
                ),
            ),
        ],
    )

    page.controls.clear()

    page.add(
        ft.Container(
            expand=True,
            gradient=ft.LinearGradient(
                begin=ft.Alignment.TOP_LEFT,
                end=ft.Alignment.BOTTOM_RIGHT,
                colors=[
                    "#EEF2FF",
                    "#F5F3FF",
                    "#E0F2FE",
                ],
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
                            width=450,
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
    )

    page.update()
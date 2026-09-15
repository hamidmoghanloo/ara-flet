import flet as ft
from dashboard import dashboard_page


# =========================================================
# Profile Page
# =========================================================

def profile_page(
    page,
    user,
    email,
    show_message,
):

    # -----------------------------------------------------
    # Inputs
    # -----------------------------------------------------

    first_name = ft.TextField(
        label="نام",
        hint_text="مثلاً علی",
        value=user.get("first_name", ""),
        text_align=ft.TextAlign.RIGHT,
        border_radius=10,
        bgcolor="white",
    )

    last_name = ft.TextField(
        label="نام خانوادگی",
        hint_text="مثلاً احمدی",
        value=user.get("last_name", ""),
        text_align=ft.TextAlign.RIGHT,
        border_radius=10,
        bgcolor="white",
    )

    username = ft.TextField(
        label="نام کاربری",
        hint_text="مثلاً ali123",
        value=user.get("username", ""),
        text_align=ft.TextAlign.RIGHT,
        border_radius=10,
        bgcolor="white",
    )

    phone = ft.TextField(
        label="شماره همراه",
        hint_text="مثلاً 09123456789",
        value=user.get("phone", ""),
        keyboard_type=ft.KeyboardType.PHONE,
        text_align=ft.TextAlign.RIGHT,
        border_radius=10,
        bgcolor="white",
    )

    age = ft.TextField(
        label="سن",
        hint_text="مثلاً 20",
        value=user.get("age", ""),
        keyboard_type=ft.KeyboardType.NUMBER,
        text_align=ft.TextAlign.RIGHT,
        border_radius=10,
        bgcolor="white",
    )


    # =====================================================
    # Save Profile
    # =====================================================

    def save_profile(e):

        first_name_value = first_name.value.strip()
        last_name_value = last_name.value.strip()
        username_value = username.value.strip()
        phone_value = phone.value.strip()
        age_value = age.value.strip()


        # -------------------------------------------------
        # Validation
        # -------------------------------------------------

        if not first_name_value:

            show_message(
                "لطفاً نام خود را وارد کنید."
            )

            return


        if not last_name_value:

            show_message(
                "لطفاً نام خانوادگی خود را وارد کنید."
            )

            return


        if not username_value:

            show_message(
                "لطفاً نام کاربری را وارد کنید."
            )

            return


        if not phone_value:

            show_message(
                "لطفاً شماره همراه را وارد کنید."
            )

            return


        if not age_value:

            show_message(
                "لطفاً سن خود را وارد کنید."
            )

            return


        # -------------------------------------------------
        # Save
        # -------------------------------------------------

        user["first_name"] = first_name_value
        user["last_name"] = last_name_value
        user["username"] = username_value
        user["phone"] = phone_value
        user["age"] = age_value


        show_message(
            "اطلاعات پروفایل با موفقیت ذخیره شد.",
            "#16A34A",
        )


        # -------------------------------------------------
        # Go Dashboard
        # -------------------------------------------------

        dashboard_page(
            page,
            user,
            email,
            show_message,
        )


    # =====================================================
    # Profile UI
    # =====================================================

    content = ft.Column(

        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

        spacing=14,

        controls=[

            ft.Icon(
                ft.Icons.ACCOUNT_CIRCLE,
                size=75,
                color="#4F46E5",
            ),

            ft.Text(
                "پروفایل کاربری",
                size=30,
                weight=ft.FontWeight.BOLD,
                color="#111827",
            ),

            ft.Text(
                "اطلاعات خود را وارد کنید",
                size=14,
                color="#6B7280",
            ),

            ft.Container(height=5),

            first_name,

            last_name,

            username,

            phone,

            age,

            ft.Container(height=5),

            ft.ElevatedButton(
                "ذخیره و ورود به داشبورد",
                width=300,
                height=50,
                bgcolor="#4F46E5",
                color="white",
                on_click=save_profile,
            ),
        ],
    )


    # =====================================================
    # Page
    # =====================================================

    page.controls.clear()

    page.controls.append(

        ft.Container(
            expand=True,
            alignment=ft.Alignment.CENTER,
            padding=20,

            content=ft.Container(
                width=450,
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
    )

    page.update()

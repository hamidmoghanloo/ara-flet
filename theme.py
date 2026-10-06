# import flet as ft


# # =========================
# # رنگ‌های اصلی Fin3an
# # =========================

# NAVY = "#101C36"
# NAVY_LIGHT = "#172746"
# NAVY_DARK = "#0A1224"

# WHITE = "#FFFFFF"
# BLACK = "#0B0F19"

# GRAY = "#6B7280"
# LIGHT_GRAY = "#F4F6FA"

# BORDER = "#E5E7EB"


# # =========================
# # استایل صفحه
# # =========================

# def setup_page(page: ft.Page):

#     page.title = "Fin3an"

#     page.bgcolor = LIGHT_GRAY

#     page.padding = 0

#     page.rtl = True

#     page.window.width = 1200
#     page.window.height = 750


# # =========================
# # دکمه اصلی
# # =========================

# def primary_button(text, on_click):

#     return ft.ElevatedButton(
#         text=text,
#         width=350,
#         height=50,
#         on_click=on_click,
#         style=ft.ButtonStyle(
#             bgcolor=NAVY,
#             color=WHITE,
#         ),
#     )


# # =========================
# # TextField
# # =========================

# def input_field(
#     label,
#     password=False,
# ):

#     return ft.TextField(
#         label=label,
#         width=350,
#         password=password,
#         can_reveal_password=password,
#         border_color=BORDER,
#         focused_border_color=NAVY,
#         cursor_color=NAVY,
#     )


# # =========================
# # کارت سفید
# # =========================

# def white_card(content, width=450):

#     return ft.Container(
#         width=width,
#         padding=40,
#         bgcolor=WHITE,
#         border_radius=20,
#         content=content,
#     )

import flet as ft

NAVY = "#101C36"
NAVY_LIGHT = "#172746"
NAVY_DARK = "#0A1224"

WHITE = "#FFFFFF"
BLACK = "#0B0F19"

GRAY = "#6B7280"
LIGHT_GRAY = "#F4F6FA"
BORDER = "#E5E7EB"

GREEN = "#16A34A"
ORANGE = "#F59E0B"
RED = "#DC2626"


def setup_page(page: ft.Page):
    page.title = "Fin3an"
    page.bgcolor = LIGHT_GRAY
    page.padding = 0
    page.rtl = True

    page.window.width = 1200
    page.window.height = 750


def card(content, padding=20):
    return ft.Container(
        bgcolor=WHITE,
        border_radius=16,
        padding=padding,
        content=content,
    )


def menu_button(text, icon, on_click):
    return ft.TextButton(
        text=text,
        icon=icon,
        on_click=on_click,
        style=ft.ButtonStyle(
            color=WHITE,
        ),
    )
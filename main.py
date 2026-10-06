# import flet as ft


# def main(page: ft.Page):
#     page.title = "Fin3an Dashboard"
#     page.window.width = 1200
#     page.window.height = 750
#     page.padding = 0
#     page.bgcolor = "#F5F6FA"
#     page.rtl = True

#     # -----------------------------
#     # اطلاعات کاربر
#     # -----------------------------
#     user_name = "پریسان"
#     username = "Fin3an"

#     # -----------------------------
#     # محتوای اصلی
#     # -----------------------------
#     content = ft.Container(
#         expand=True,
#         padding=30,
#     )

#     # -----------------------------
#     # عنوان صفحه
#     # -----------------------------
#     header_title = ft.Text(
#         "داشبورد",
#         size=28,
#         weight=ft.FontWeight.BOLD,
#     )

#     # -----------------------------
#     # هدر
#     # -----------------------------
#     header = ft.Container(
#         content=ft.Row(
#             [
#                 ft.Row(
#                     [
#                         ft.CircleAvatar(
#                             content=ft.Text(
#                                 "پ",
#                                 size=20,
#                                 weight=ft.FontWeight.BOLD,
#                             ),
#                         ),
#                         ft.Column(
#                             [
#                                 ft.Text(
#                                     user_name,
#                                     size=16,
#                                     weight=ft.FontWeight.BOLD,
#                                 ),
#                                 ft.Text(
#                                     f"@{username}",
#                                     size=12,
#                                     color=ft.Colors.GREY_600,
#                                 ),
#                             ],
#                             spacing=0,
#                         ),
#                     ],
#                     spacing=10,
#                 ),
#                 header_title,
#             ],
#             alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
#         ),
#         padding=30,
#         bgcolor=ft.Colors.WHITE,
#     )

#     # -----------------------------
#     # کارت آماری
#     # -----------------------------
#     def stat_card(title, value, icon):
#         return ft.Container(
#             content=ft.Row(
#                 [
#                     ft.Container(
#                         content=ft.Icon(
#                             icon,
#                             size=30,
#                         ),
#                         width=55,
#                         height=55,
#                         alignment=ft.Alignment(0, 0),
#                         border_radius=12,
#                     ),
#                     ft.Column(
#                         [
#                             ft.Text(
#                                 title,
#                                 size=13,
#                                 color=ft.Colors.GREY_600,
#                             ),
#                             ft.Text(
#                                 value,
#                                 size=24,
#                                 weight=ft.FontWeight.BOLD,
#                             ),
#                         ],
#                         spacing=3,
#                     ),
#                 ],
#                 spacing=15,
#             ),
#             padding=20,
#             expand=True,
#             bgcolor=ft.Colors.WHITE,
#             border_radius=15,
#         )

#     # -----------------------------
#     # صفحه داشبورد
#     # -----------------------------
#     def dashboard_page(e=None):
#         header_title.value = "داشبورد"

#         content.content = ft.Column(
#             [
#                 ft.Text(
#                     f"سلام {user_name} 👋",
#                     size=26,
#                     weight=ft.FontWeight.BOLD,
#                 ),
#                 ft.Text(
#                     "به داشبورد شخصی خودت خوش اومدی.",
#                     size=15,
#                     color=ft.Colors.GREY_600,
#                 ),

#                 ft.Container(height=15),

#                 ft.Row(
#                     [
#                         stat_card(
#                             "پروژه‌ها",
#                             "12",
#                             ft.Icons.FOLDER,
#                         ),
#                         stat_card(
#                             "گزارش‌ها",
#                             "24",
#                             ft.Icons.INSERT_CHART,
#                         ),
#                         stat_card(
#                             "فعالیت‌ها",
#                             "38",
#                             ft.Icons.TRENDING_UP,
#                         ),
#                     ],
#                     spacing=15,
#                 ),

#                 ft.Container(height=20),

#                 ft.Container(
#                     content=ft.Column(
#                         [
#                             ft.Text(
#                                 "فعالیت‌های اخیر",
#                                 size=20,
#                                 weight=ft.FontWeight.BOLD,
#                             ),

#                             ft.Divider(),

#                             ft.ListTile(
#                                 leading=ft.Icon(
#                                     ft.Icons.CHECK_CIRCLE,
#                                 ),
#                                 title=ft.Text(
#                                     "پروژه جدید ایجاد شد",
#                                 ),
#                                 subtitle=ft.Text(
#                                     "امروز",
#                                 ),
#                             ),

#                             ft.ListTile(
#                                 leading=ft.Icon(
#                                     ft.Icons.EDIT,
#                                 ),
#                                 title=ft.Text(
#                                     "اطلاعات پروفایل ویرایش شد",
#                                 ),
#                                 subtitle=ft.Text(
#                                     "دیروز",
#                                 ),
#                             ),

#                             ft.ListTile(
#                                 leading=ft.Icon(
#                                     ft.Icons.INSERT_CHART,
#                                 ),
#                                 title=ft.Text(
#                                     "گزارش جدید ثبت شد",
#                                 ),
#                                 subtitle=ft.Text(
#                                     "۲ روز پیش",
#                                 ),
#                             ),
#                         ],
#                         spacing=5,
#                     ),
#                     padding=20,
#                     bgcolor=ft.Colors.WHITE,
#                     border_radius=15,
#                 ),
#             ],
#             spacing=5,
#             scroll=ft.ScrollMode.AUTO,
#         )

#         page.update()

#     # -----------------------------
#     # صفحه پروفایل
#     # -----------------------------
#     def profile_page(e=None):
#         header_title.value = "پروفایل"

#         content.content = ft.Column(
#             [
#                 ft.Text(
#                     "پروفایل من",
#                     size=26,
#                     weight=ft.FontWeight.BOLD,
#                 ),

#                 ft.Container(height=15),

#                 ft.Container(
#                     content=ft.Column(
#                         [
#                             ft.CircleAvatar(
#                                 content=ft.Text(
#                                     "پ",
#                                     size=35,
#                                     weight=ft.FontWeight.BOLD,
#                                 ),
#                                 radius=45,
#                             ),

#                             ft.Text(
#                                 user_name,
#                                 size=24,
#                                 weight=ft.FontWeight.BOLD,
#                             ),

#                             ft.Text(
#                                 f"@{username}",
#                                 size=15,
#                                 color=ft.Colors.GREY_600,
#                             ),

#                             ft.Divider(),

#                             ft.ListTile(
#                                 leading=ft.Icon(
#                                     ft.Icons.PERSON,
#                                 ),
#                                 title=ft.Text(
#                                     "نام",
#                                 ),
#                                 subtitle=ft.Text(
#                                     user_name,
#                                 ),
#                             ),

#                             ft.ListTile(
#                                 leading=ft.Icon(
#                                     ft.Icons.ALTERNATE_EMAIL,
#                                 ),
#                                 title=ft.Text(
#                                     "Username",
#                                 ),
#                                 subtitle=ft.Text(
#                                     username,
#                                 ),
#                             ),
#                         ],
#                         horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#                         spacing=12,
#                     ),
#                     padding=30,
#                     bgcolor=ft.Colors.WHITE,
#                     border_radius=15,
#                     width=600,
#                 ),
#             ],
#             horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#         )

#         page.update()

#     # -----------------------------
#     # صفحه گزارش‌ها
#     # -----------------------------
#     def reports_page(e=None):
#         header_title.value = "گزارش‌ها"

#         content.content = ft.Column(
#             [
#                 ft.Text(
#                     "گزارش‌ها",
#                     size=26,
#                     weight=ft.FontWeight.BOLD,
#                 ),

#                 ft.Container(height=10),

#                 ft.Container(
#                     content=ft.Column(
#                         [
#                             ft.ListTile(
#                                 leading=ft.Icon(
#                                     ft.Icons.INSERT_CHART,
#                                 ),
#                                 title=ft.Text(
#                                     "گزارش فعالیت",
#                                 ),
#                                 subtitle=ft.Text(
#                                     "آخرین بروزرسانی: امروز",
#                                 ),
#                                 trailing=ft.Icon(
#                                     ft.Icons.ARROW_FORWARD_IOS,
#                                 ),
#                             ),

#                             ft.Divider(),

#                             ft.ListTile(
#                                 leading=ft.Icon(
#                                     ft.Icons.ANALYTICS,
#                                 ),
#                                 title=ft.Text(
#                                     "گزارش پروژه‌ها",
#                                 ),
#                                 subtitle=ft.Text(
#                                     "۱۲ پروژه ثبت شده",
#                                 ),
#                                 trailing=ft.Icon(
#                                     ft.Icons.ARROW_FORWARD_IOS,
#                                 ),
#                             ),

#                             ft.Divider(),

#                             ft.ListTile(
#                                 leading=ft.Icon(
#                                     ft.Icons.BAR_CHART,
#                                 ),
#                                 title=ft.Text(
#                                     "گزارش عملکرد",
#                                 ),
#                                 subtitle=ft.Text(
#                                     "وضعیت کلی فعالیت‌ها",
#                                 ),
#                                 trailing=ft.Icon(
#                                     ft.Icons.ARROW_FORWARD_IOS,
#                                 ),
#                             ),
#                         ],
#                     ),
#                     bgcolor=ft.Colors.WHITE,
#                     border_radius=15,
#                     padding=10,
#                 ),
#             ],
#         )

#         page.update()

#     # -----------------------------
#     # صفحه تنظیمات
#     # -----------------------------
#     def settings_page(e=None):
#         header_title.value = "تنظیمات"

#         content.content = ft.Column(
#             [
#                 ft.Text(
#                     "تنظیمات",
#                     size=26,
#                     weight=ft.FontWeight.BOLD,
#                 ),

#                 ft.Container(height=10),

#                 ft.Container(
#                     content=ft.Column(
#                         [
#                             ft.Switch(
#                                 label="اعلان‌ها",
#                                 value=True,
#                             ),

#                             ft.Divider(),

#                             ft.Switch(
#                                 label="حالت تاریک",
#                                 value=False,
#                             ),

#                             ft.Divider(),

#                             ft.ListTile(
#                                 leading=ft.Icon(
#                                     ft.Icons.LANGUAGE,
#                                 ),
#                                 title=ft.Text(
#                                     "زبان",
#                                 ),
#                                 subtitle=ft.Text(
#                                     "فارسی",
#                                 ),
#                             ),
#                         ],
#                     ),
#                     padding=20,
#                     bgcolor=ft.Colors.WHITE,
#                     border_radius=15,
#                 ),
#             ],
#         )

#         page.update()

#     # -----------------------------
#     # دکمه‌های منوی کناری
#     # -----------------------------
#     def menu_button(text, icon, function):
#         return ft.Container(
#             content=ft.TextButton(
#                 content=ft.Row(
#                     [
#                         ft.Icon(icon),
#                         ft.Text(
#                             text,
#                             size=15,
#                         ),
#                     ],
#                     spacing=12,
#                 ),
#                 on_click=function,
#             ),
#             width=220,
#         )

#     # -----------------------------
#     # منوی کناری
#     # -----------------------------
#     sidebar = ft.Container(
#         content=ft.Column(
#             [
#                 ft.Container(
#                     content=ft.Text(
#                         "Fin3an",
#                         size=26,
#                         weight=ft.FontWeight.BOLD,
#                     ),
#                     padding=20,
#                 ),

#                 ft.Divider(),

#                 menu_button(
#                     "داشبورد",
#                     ft.Icons.DASHBOARD,
#                     dashboard_page,
#                 ),

#                 menu_button(
#                     "پروفایل",
#                     ft.Icons.PERSON,
#                     profile_page,
#                 ),

#                 menu_button(
#                     "گزارش‌ها",
#                     ft.Icons.INSERT_CHART,
#                     reports_page,
#                 ),

#                 menu_button(
#                     "تنظیمات",
#                     ft.Icons.SETTINGS,
#                     settings_page,
#                 ),

#                 ft.Container(
#                     expand=True,
#                 ),

#                 menu_button(
#                     "خروج",
#                     ft.Icons.LOGOUT,
#                     lambda e: page.window.close(),
#                 ),
#             ],
#             spacing=5,
#         ),
#         width=240,
#         bgcolor=ft.Colors.WHITE,
#         padding=10,
#     )

#     # -----------------------------
#     # ساخت صفحه اصلی
#     # -----------------------------
#     page.add(
#         ft.Row(
#             [
#                 sidebar,

#                 ft.Column(
#                     [
#                         header,
#                         content,
#                     ],
#                     expand=True,
#                     spacing=0,
#                 ),
#             ],
#             expand=True,
#             spacing=0,
#         )
#     )
    

import flet as ft

from theme import setup_page
from login import login_page


def main(page: ft.Page):
    setup_page(page)
    login_page(page)


ft.run(main)
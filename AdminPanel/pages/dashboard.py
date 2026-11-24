import flet as ft
from sqlalchemy import select
from database.db import SessionLocal
from database.models import User


def dashboard_page(page: ft.Page, user):

    page.title = "Admin Panel | User Dashboard"
    page.bgcolor = "#080F20"
    page.padding = 0
    page.theme_mode = ft.ThemeMode.DARK

    user_name = user.full_name

    # Main content area
    content_area = ft.Column(
        expand=True,
        spacing=20,
        scroll=ft.ScrollMode.AUTO,
    )

    # Dashboard content
    def show_dashboard(e=None):

        content_area.controls.clear()

        welcome_section = ft.Container(
            padding=25,
            border_radius=16,
            bgcolor="#14294A",
            content=ft.Column(
                controls=[
                    ft.Text(
                        f"Welcome back, {user_name}!",
                        size=28,
                        weight=ft.FontWeight.BOLD,
                        color="white",
                    ),
                    ft.Text(
                        "Welcome to your personal dashboard.",
                        size=14,
                        color="#91A3BD",
                    ),
                ],
                spacing=10,
            ),
        )

        user_card = ft.Container(
            padding=25,
            border_radius=16,
            bgcolor="#101B30",
            border=ft.Border.all(1, "#263B5B"),
            content=ft.Column(
                controls=[
                    ft.Icon(
                        ft.Icons.PERSON,
                        size=45,
                        color="#65A8FF",
                    ),
                    ft.Text(
                        "My Account",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color="white",
                    ),
                    ft.Text(
                        f"Name: {user.full_name}",
                        color="#91A3BD",
                    ),
                    ft.Text(
                        f"Email: {user.email}",
                        color="#91A3BD",
                    ),
                    ft.Text(
                        f"Age: {user.age}",
                        color="#91A3BD",
                    ),
                ],
                spacing=12,
            ),
        )

        content_area.controls.extend([
            ft.Text(
                "Dashboard",
                size=26,
                weight=ft.FontWeight.BOLD,
                color="white",
            ),
            welcome_section,
            user_card,
        ])

        page.update()

    # Profile content
    def show_profile(e=None):

        content_area.controls.clear()

        created_at = user.created_at

        if created_at:
            membership_date = created_at.strftime("%Y-%m-%d %H:%M")
        else:
            membership_date = "Not available"

        profile_card = ft.Container(
            padding=30,
            border_radius=16,
            bgcolor="#101B30",
            border=ft.Border.all(1, "#263B5B"),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=18,
                controls=[
                    ft.Container(
                        width=90,
                        height=90,
                        border_radius=45,
                        bgcolor="#193B70",
                        alignment=ft.Alignment.CENTER,
                        content=ft.Icon(
                            ft.Icons.PERSON,
                            size=55,
                            color="#65A8FF",
                        ),
                    ),

                    ft.Text(
                        user.full_name,
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color="white",
                    ),

                    ft.Text(
                        "Personal Profile",
                        size=14,
                        color="#91A3BD",
                    ),

                    ft.Divider(color="#263B5B"),

                    ft.Row(
                        controls=[
                            ft.Icon(
                                ft.Icons.BADGE_OUTLINED,
                                color="#65A8FF",
                            ),
                            ft.Column(
                                controls=[
                                    ft.Text(
                                        "Full Name",
                                        size=12,
                                        color="#7186A6",
                                    ),
                                    ft.Text(
                                        user.full_name,
                                        color="white",
                                    ),
                                ],
                                spacing=4,
                                expand=True,
                            ),
                        ],
                    ),

                    ft.Row(
                        controls=[
                            ft.Icon(
                                ft.Icons.EMAIL_OUTLINED,
                                color="#65A8FF",
                            ),
                            ft.Column(
                                controls=[
                                    ft.Text(
                                        "Email Address",
                                        size=12,
                                        color="#7186A6",
                                    ),
                                    ft.Text(
                                        user.email,
                                        color="white",
                                    ),
                                ],
                                spacing=4,
                                expand=True,
                            ),
                        ],
                    ),

                    ft.Row(
                        controls=[
                            ft.Icon(
                                ft.Icons.CALENDAR_TODAY,
                                color="#65A8FF",
                            ),
                            ft.Column(
                                controls=[
                                    ft.Text(
                                        "Age",
                                        size=12,
                                        color="#7186A6",
                                    ),
                                    ft.Text(
                                        str(user.age),
                                        color="white",
                                    ),
                                ],
                                spacing=4,
                                expand=True,
                            ),
                        ],
                    ),

                    ft.Row(
                        controls=[
                            ft.Icon(
                                ft.Icons.ACCESS_TIME,
                                color="#65A8FF",
                            ),
                            ft.Column(
                                controls=[
                                    ft.Text(
                                        "Membership Date",
                                        size=12,
                                        color="#7186A6",
                                    ),
                                    ft.Text(
                                        membership_date,
                                        color="white",
                                    ),
                                ],
                                spacing=4,
                                expand=True,
                            ),
                        ],
                    ),
                ],
            ),
        )

        content_area.controls.extend([
            ft.Text(
                "My Profile",
                size=26,
                weight=ft.FontWeight.BOLD,
                color="white",
            ),
            profile_card,
        ])

        page.update()
       # Show all registered users
    def show_users(e=None):

        content_area.controls.clear()

        users_list = ft.Column(
            spacing=12,
            scroll=ft.ScrollMode.AUTO,
        )

        db = SessionLocal()

        try:
            users = db.scalars(
                select(User).order_by(User.id)
            ).all()

            if not users:
                users_list.controls.append(
                    ft.Text(
                        "No users registered yet.",
                        color="#91A3BD",
                    )
                )

            for registered_user in users:

                user_card = ft.Container(
                    padding=20,
                    border_radius=14,
                    bgcolor="#101B30",
                    border=ft.Border.all(1, "#263B5B"),

                    content=ft.Column(
                        spacing=8,
                        controls=[
                            ft.Text(
                                registered_user.full_name,
                                size=19,
                                weight=ft.FontWeight.BOLD,
                                color="white",
                            ),

                            ft.Text(
                                f"Email: {registered_user.email}",
                                color="#91A3BD",
                            ),

                            ft.Text(
                                f"Age: {registered_user.age}",
                                color="#91A3BD",
                            ),

                            ft.Text(
                                "Membership Date: "
                                + registered_user.created_at.strftime(
                                    "%Y-%m-%d %H:%M"
                                ),
                                color="#91A3BD",
                            ),
                        ],
                    ),
                )

                users_list.controls.append(user_card)

        except Exception as error:
            print("Users Loading Error:", error)

            users_list.controls.append(
                ft.Text(
                    "Could not load users.",
                    color="#FF6B6B",
                )
            )

        finally:
            db.close()

        content_area.controls.extend([
            ft.Text(
                "All Users",
                size=26,
                weight=ft.FontWeight.BOLD,
                color="white",
            ),
            users_list,
        ])

        page.update()
    # Logout
    def logout(e=None):

        page.clean()

        from pages.login import login_page

        login_page(page)

    # Sidebar
    sidebar = ft.Container(
        width=240,
        bgcolor="#101B30",
        padding=20,
        content=ft.Column(
            controls=[
                ft.Text(
                    "ADMIN PANEL",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="#65A8FF",
                ),

                ft.Divider(color="#263B5B"),

                ft.Text(
                    "MAIN MENU",
                    size=11,
                    color="#7186A6",
                ),

                ft.ListTile(
                    leading=ft.Icon(
                        ft.Icons.DASHBOARD_OUTLINED,
                        color="#65A8FF",
                    ),
                    title=ft.Text("Dashboard"),
                    selected=True,
                    selected_tile_color="#193B70",
                    on_click=show_dashboard,
                ),

                ft.ListTile(
                    leading=ft.Icon(
                        ft.Icons.PERSON_OUTLINE,
                        color="#91A3BD",
                    ),
                    title=ft.Text("My Profile"),
                    on_click=show_profile,
                ),

               ft.ListTile(
                    leading=ft.Icon(
                       ft.Icons.GROUP_OUTLINED,
                       color="#91A3BD",
                    ),
                    title=ft.Text("All Users"),
                    on_click=show_users,
                ),

                ft.Container(expand=True),

                ft.Divider(color="#263B5B"),

                ft.ListTile(
                    leading=ft.Icon(
                        ft.Icons.LOGOUT,
                        color="#FF6B6B",
                    ),
                    title=ft.Text(
                        "Logout",
                        color="#FF6B6B",
                    ),
                    on_click=logout,
                ),
            ],
            expand=True,
            spacing=8,
        ),
    )

    # Main Content
    main_content = ft.Container(
        expand=True,
        padding=30,
        content=content_area,
    )

    # Show Dashboard by default
    show_dashboard()

    # Main Layout
    page.add(
        ft.Row(
            controls=[
                sidebar,
                main_content,
            ],
            expand=True,
            spacing=0,
        )
    )
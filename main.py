import flet as ft


def main(page: ft.Page):
    page.title = "ماشین حساب"
    page.bgcolor = "#000000"
    page.padding = 20

    result = ft.Text(
        "0",
        color="white",
        size=45,
        text_align=ft.TextAlign.RIGHT,
    )

    expression = ""

    def update():
        result.value = expression if expression else "0"
        page.update()

    def click(e):
        nonlocal expression
        expression += e.control.data
        update()

    def clear(e):
        nonlocal expression
        expression = ""
        update()

    def calculate(e):
        nonlocal expression
        try:
            expression = str(
                eval(
                    expression
                    .replace("×", "*")
                    .replace("÷", "/")
                )
            )
        except:
            expression = "Error"

        update()

    def make_button(text, color="#333333", func=click):
        return ft.ElevatedButton(
            text,
            data=text,
            width=70,
            height=70,
            style=ft.ButtonStyle(
                bgcolor=color,
                color="white",
                shape=ft.CircleBorder(),
            ),
            on_click=func,
        )

    page.add(
        ft.Container(
            result,
            width=320,
            height=100,
        ),

        ft.Row(
            [
                make_button("AC", "#999999", clear),
                make_button("%", "#999999"),
                make_button("÷", "#ff9500"),
                make_button("×", "#ff9500"),
            ]
        ),

        ft.Row(
            [
                make_button("7"),
                make_button("8"),
                make_button("9"),
                make_button("-", "#ff9500"),
            ]
        ),

        ft.Row(
            [
                make_button("4"),
                make_button("5"),
                make_button("6"),
                make_button("+", "#ff9500"),
            ]
        ),

        ft.Row(
            [
                make_button("1"),
                make_button("2"),
                make_button("3"),
                make_button("=", "#ff9500", calculate),
            ]
        ),

        ft.Row(
            [
                make_button("0"),
                make_button("."),
            ]
        ),
    )


ft.run(main)
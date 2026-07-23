import flet as ft

def main(page: ft.Page):
    page.title = "iPhone Calculator"
    page.bgcolor = "#000000"
    page.window_width = 350
    page.window_height = 600

    result = ft.Text(
        "0",
        color="white",
        size=45,
        text_align="right",
    )

    expression = ""

    def click(e):
        nonlocal expression

        value = e.control.text

        if value == "AC":
            expression = ""
            result.value = "0"

        elif value == "=":
            try:
                expression = str(eval(expression))
                result.value = expression
            except:
                expression = ""
                result.value = "Error"

        elif value == "±":
            if expression.startswith("-"):
                expression = expression[1:]
            else:
                expression = "-" + expression
            result.value = expression

        elif value == "%":
            try:
                expression = str(float(expression) / 100)
                result.value = expression
            except:
                pass

        else:
            expression += value
            result.value = expression

        page.update()


    def button(text, color="#333333"):
        return ft.ElevatedButton(
            text,
            width=70,
            height=70,
            style=ft.ButtonStyle(
                bgcolor=color,
                shape=ft.CircleBorder(),
                color="white",
            ),
            on_click=click
        )


    display = ft.Container(
        result,
        alignment=ft.alignment.center_right,
        padding=20,
        height=130
    )


    keys = [
        ("AC","#A5A5A5"),("±","#A5A5A5"),("%","#A5A5A5"),("÷","#FF9500"),
        ("7","#333333"),("8","#333333"),("9","#333333"),("×","#FF9500"),
        ("4","#333333"),("5","#333333"),("6","#333333"),("-","#FF9500"),
        ("1","#333333"),("2","#333333"),("3","#333333"),("+","#FF9500"),
        ("0","#333333"),(".","#333333"),("=","#FF9500")
    ]


    rows=[]
    row=[]

    for text,color in keys:
        row.append(button(text,color))

        if len(row)==4:
            rows.append(ft.Row(row,alignment="center"))
            row=[]

    rows.append(
        ft.Row(
            [button("0"),button("."),button("=","#FF9500")],
            alignment="center"
        )
    )


    page.add(
        ft.Column(
            [display]+rows,
            alignment="center"
        )
    )


ft.app(target=main)
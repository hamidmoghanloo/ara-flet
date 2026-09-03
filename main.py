import tkinter as tk
from dataclasses import dataclass
from decimal import Decimal, DivisionByZero, InvalidOperation, getcontext

getcontext().prec = 18


@dataclass(frozen=True)
class Button:
    label: str
    kind: str
    column: int
    row: int
    span: int = 1


class IPhoneCalculator(tk.Tk):
    BLACK = "#000000"
    NUMBER = "#333333"
    NUMBER_PRESSED = "#737373"
    UTILITY = "#A5A5A5"
    UTILITY_PRESSED = "#D4D4D2"
    ORANGE = "#FF9F0A"
    ORANGE_PRESSED = "#FFD08A"
    WHITE = "#FFFFFF"

    BUTTONS = (
        Button("AC", "utility", 0, 0),
        Button("±", "utility", 1, 0),
        Button("%", "utility", 2, 0),
        Button("÷", "operator", 3, 0),
        Button("7", "number", 0, 1),
        Button("8", "number", 1, 1),
        Button("9", "number", 2, 1),
        Button("×", "operator", 3, 1),
        Button("4", "number", 0, 2),
        Button("5", "number", 1, 2),
        Button("6", "number", 2, 2),
        Button("−", "operator", 3, 2),
        Button("1", "number", 0, 3),
        Button("2", "number", 1, 3),
        Button("3", "number", 2, 3),
        Button("+", "operator", 3, 3),
        Button("0", "number", 0, 4, 2),
        Button(".", "number", 2, 4),
        Button("=", "operator", 3, 4),
    )

    def __init__(self):
        super().__init__()
        self.title("ماشین حساب")
        self.geometry("390x700")
        self.minsize(320, 520)
        self.configure(bg=self.BLACK)

        self.value = "0"
        self.pending_value = None
        self.pending_operator = None
        self.last_operator = None
        self.last_value = None
        self.waiting_for_number = False
        self.has_error = False
        self.pressed_label = None
        self.hit_areas = []

        self.canvas = tk.Canvas(self, bg=self.BLACK, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.canvas.bind("<Configure>", lambda event: self.draw())
        self.canvas.bind("<ButtonPress-1>", self.mouse_down)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_up)

        self.bind("<Key>", self.keyboard)
        self.bind("<BackSpace>", self.backspace)
        self.bind("<Escape>", lambda event: self.press("AC"))

        self.draw()

    def draw(self):
        width = max(self.canvas.winfo_width(), 320)
        height = max(self.canvas.winfo_height(), 520)

        self.canvas.delete("all")
        self.hit_areas.clear()

        margin = max(12, width * 0.042)
        gap = max(8, width * 0.031)
        display_height = height * 0.345
        cell_width = (width - 2 * margin - 3 * gap) / 4
        row_height = (height - display_height - margin - 4 * gap) / 5
        size = min(cell_width, row_height - gap)

        font_size = max(22, int(width * 0.17) - max(0, len(self.value) - 8) * 4)

        self.canvas.create_text(
            width - margin,
            display_height - margin * 0.55,
            text=self.value,
            fill=self.WHITE,
            anchor="se",
            font=("Arial", font_size),
        )

        for button in self.BUTTONS:
            x1 = margin + button.column * (cell_width + gap)
            y1 = display_height + button.row * (row_height + gap)
            y1 += (row_height - size) / 2
            x2 = x1 + cell_width * button.span + gap * (button.span - 1)
            y2 = y1 + size

            color, text_color = self.button_colors(button)

            if button.span == 2:
                self.draw_pill(x1, y1, x2, y2, color)
                text_x = x1 + size / 2
            else:
                self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)
                text_x = (x1 + x2) / 2

            self.canvas.create_text(
                text_x,
                (y1 + y2) / 2,
                text=button.label,
                fill=text_color,
                font=("Arial", max(18, int(size * 0.36))),
            )

            self.hit_areas.append(((x1, y1, x2, y2), button.label))

    def draw_pill(self, x1, y1, x2, y2, color):
        radius = (y2 - y1) / 2
        self.canvas.create_rectangle(
            x1 + radius, y1, x2 - radius, y2, fill=color, outline=color
        )
        self.canvas.create_oval(x1, y1, x1 + 2 * radius, y2, fill=color, outline=color)
        self.canvas.create_oval(
            x2 - 2 * radius, y1, x2, y2, fill=color, outline=color
        )

    def button_colors(self, button):
        if button.label == self.pending_operator and self.waiting_for_number:
            return self.WHITE, self.ORANGE

        pressed = button.label == self.pressed_label

        if button.kind == "utility":
            return (
                self.UTILITY_PRESSED if pressed else self.UTILITY,
                self.BLACK,
            )

        if button.kind == "operator":
            return (
                self.ORANGE_PRESSED if pressed else self.ORANGE,
                self.WHITE,
            )

        return (
            self.NUMBER_PRESSED if pressed else self.NUMBER,
            self.WHITE,
        )

    def mouse_down(self, event):
        self.pressed_label = self.button_at(event.x, event.y)
        self.draw()

    def mouse_up(self, event):
        clicked = self.button_at(event.x, event.y)
        was_pressed = self.pressed_label
        self.pressed_label = None

        if clicked and clicked == was_pressed:
            self.press(clicked)
        else:
            self.draw()

    def button_at(self, x, y):
        for (x1, y1, x2, y2), label in self.hit_areas:
            if x1 <= x <= x2 and y1 <= y <= y2:
                return label
        return None

    def keyboard(self, event):
        mapping = {
            "Return": "=",
            "KP_Enter": "=",
            "plus": "+",
            "minus": "−",
            "slash": "÷",
            "asterisk": "×",
            "percent": "%",
        }

        key = mapping.get(event.keysym, event.char)

        if key and key in "0123456789.+-*/%=":
            self.press({"-": "−", "*": "×", "/": "÷"}.get(key, key))
            return "break"

    def press(self, key):
        if key.isdigit() or key == ".":
            self.input_digit(key)
        elif key in {"+", "−", "×", "÷"}:
            self.input_operator(key)
        elif key == "=":
            self.equals()
        elif key == "AC":
            self.clear()
        elif key == "±":
            self.change_sign()
        elif key == "%":
            self.percent()

        self.draw()

    def input_digit(self, digit):
        if self.has_error or self.waiting_for_number:
            self.value = "0"
            self.has_error = False
            self.waiting_for_number = False

        if digit == ".":
            if "." not in self.value:
                self.value += "."
            return

        if len(self.value.replace("-", "").replace(".", "")) >= 12:
            return

        if self.value == "0":
            self.value = digit
        elif self.value == "-0":
            self.value = "-" + digit
        else:
            self.value += digit

    def input_operator(self, operator):
        if self.has_error:
            return

        current = self.current_number()

        if self.pending_operator and not self.waiting_for_number:
            result = self.calculate(self.pending_value, current, self.pending_operator)
            if result is None:
                return
            self.pending_value = result
            self.value = self.format_number(result)
        else:
            self.pending_value = current

        self.pending_operator = operator
        self.waiting_for_number = True

    def equals(self):
        if self.has_error:
            return

        if self.pending_operator:
            right = self.pending_value if self.waiting_for_number else self.current_number()
            result = self.calculate(self.pending_value, right, self.pending_operator)

            if result is None:
                return

            self.last_operator = self.pending_operator
            self.last_value = right
            self.value = self.format_number(result)
            self.pending_value = None
            self.pending_operator = None
            self.waiting_for_number = True

        elif self.last_operator and self.last_value is not None:
            result = self.calculate(
                self.current_number(),
                self.last_value,
                self.last_operator,
            )

            if result is not None:
                self.value = self.format_number(result)
                self.waiting_for_number = True

    def calculate(self, left, right, operator):
        if left is None or right is None:
            return None

        try:
            if operator == "+":
                result = left + right
            elif operator == "−":
                result = left - right
            elif operator == "×":
                result = left * right
            else:
                result = left / right

            if not result.is_finite() or abs(result) > Decimal("999999999999"):
                raise InvalidOperation

            return result

        except (DivisionByZero, InvalidOperation, ZeroDivisionError):
            self.value = "Error"
            self.has_error = True
            self.pending_operator = None
            self.pending_value = None
            return None

    def clear(self):
        self.value = "0"
        self.pending_value = None
        self.pending_operator = None
        self.last_operator = None
        self.last_value = None
        self.waiting_for_number = False
        self.has_error = False

    def change_sign(self):
        if self.has_error or self.value in {"0", "0."}:
            return

        self.value = (
            self.value[1:]
            if self.value.startswith("-")
            else "-" + self.value
        )

    def percent(self):
        if self.has_error:
            return

        number = self.current_number()

        if self.pending_value is not None and self.pending_operator in {"+", "−"}:
            number = self.pending_value * number / Decimal("100")
        else:
            number /= Decimal("100")

        self.value = self.format_number(number)

    def backspace(self, event=None):
        if not self.has_error and not self.waiting_for_number:
            self.value = self.value[:-1]

            if self.value in {"", "-"}:
                self.value = "0"

            self.draw()

        return "break"

    def current_number(self):
        try:
            return Decimal(self.value)
        except InvalidOperation:
            return Decimal(0)

    @staticmethod
    def format_number(number):
        if number == number.to_integral():
            return format(number, ".0f")

        text = format(number, ".12f").rstrip("0").rstrip(".")
        return text if len(text.replace("-", "")) <= 12 else format(number, ".8g")


if __name__ == "__main__":
    IPhoneCalculator().mainloop()
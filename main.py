"""
ماشین‌حساب شبیه به آیفون (iOS Calculator Clone)
با استفاده از tkinter - کاملاً کاربردی و بدون نیاز به نصب کتابخانه اضافه

طرز اجرا:
    python3 iphone_calculator.py
"""

import tkinter as tk

# ---------- رنگ‌بندی شبیه به آیفون ----------
BG_COLOR = "#000000"           # پس‌زمینه اصلی
DISPLAY_COLOR = "#000000"      # پس‌زمینه صفحه نمایش
TEXT_COLOR = "#FFFFFF"         # رنگ متن صفحه نمایش

NUM_BTN_COLOR = "#333333"      # رنگ دکمه‌های عدد
NUM_BTN_ACTIVE = "#5a5a5a"

FUNC_BTN_COLOR = "#a5a5a5"     # رنگ دکمه‌های تابع (AC, +/-, %)
FUNC_BTN_ACTIVE = "#d9d9d9"
FUNC_TEXT_COLOR = "#000000"

OP_BTN_COLOR = "#ff9f0a"       # رنگ دکمه‌های عملگر (نارنجی)
OP_BTN_ACTIVE = "#ffc069"
OP_TEXT_COLOR = "#FFFFFF"

FONT_DISPLAY = ("Helvetica", 60)
FONT_BTN = ("Helvetica", 24)


class iPhoneCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("320x568")
        self.root.resizable(False, False)
        self.root.configure(bg=BG_COLOR)

        # متغیرهای منطق ماشین‌حساب
        self.current_value = "0"
        self.stored_value = None
        self.pending_operator = None
        self.should_reset_display = False

        self._build_display()
        self._build_buttons()

    # ---------------- صفحه نمایش ----------------
    def _build_display(self):
        self.display_var = tk.StringVar(value="0")
        display_frame = tk.Frame(self.root, bg=DISPLAY_COLOR)
        display_frame.pack(fill="both", expand=False)

        self.display_label = tk.Label(
            display_frame,
            textvariable=self.display_var,
            anchor="e",
            bg=DISPLAY_COLOR,
            fg=TEXT_COLOR,
            font=FONT_DISPLAY,
            padx=20,
            pady=30,
        )
        self.display_label.pack(fill="both", expand=True)

    # ---------------- دکمه‌ها ----------------
    def _build_buttons(self):
        btn_frame = tk.Frame(self.root, bg=BG_COLOR)
        btn_frame.pack(fill="both", expand=True)

        # چیدمان دکمه‌ها دقیقا مثل آیفون
        # هر آیتم: (متن, نوع)  نوع یکی از: num, func, op, zero
        layout = [
            [("AC", "func"), ("+/-", "func"), ("%", "func"), ("÷", "op")],
            [("7", "num"), ("8", "num"), ("9", "num"), ("×", "op")],
            [("4", "num"), ("5", "num"), ("6", "num"), ("-", "op")],
            [("1", "num"), ("2", "num"), ("3", "num"), ("+", "op")],
            [("0", "zero"), (".", "num"), ("=", "op")],
        ]

        for row_index, row in enumerate(layout):
            btn_frame.rowconfigure(row_index, weight=1)
            col_index = 0
            for (text, kind) in row:
                if kind == "zero":
                    btn = self._create_button(btn_frame, text, kind)
                    btn.grid(
                        row=row_index, column=col_index, columnspan=2,
                        sticky="nsew", padx=4, pady=4
                    )
                    col_index += 2
                else:
                    btn = self._create_button(btn_frame, text, kind)
                    btn.grid(
                        row=row_index, column=col_index,
                        sticky="nsew", padx=4, pady=4
                    )
                    col_index += 1

        for c in range(4):
            btn_frame.columnconfigure(c, weight=1)

    def _create_button(self, parent, text, kind):
        if kind == "num" or kind == "zero":
            bg, active_bg, fg = NUM_BTN_COLOR, NUM_BTN_ACTIVE, TEXT_COLOR
        elif kind == "func":
            bg, active_bg, fg = FUNC_BTN_COLOR, FUNC_BTN_ACTIVE, FUNC_TEXT_COLOR
        else:  # op
            bg, active_bg, fg = OP_BTN_COLOR, OP_BTN_ACTIVE, OP_TEXT_COLOR

        btn = tk.Button(
            parent,
            text=text,
            font=FONT_BTN,
            bg=bg,
            fg=fg,
            activebackground=active_bg,
            activeforeground=fg,
            bd=0,
            relief="flat",
            command=lambda t=text: self.on_button_press(t),
        )
        return btn

    # ---------------- منطق ماشین‌حساب ----------------
    def on_button_press(self, text):
        if text.isdigit():
            self._input_digit(text)
        elif text == ".":
            self._input_dot()
        elif text == "AC":
            self._clear()
        elif text == "+/-":
            self._toggle_sign()
        elif text == "%":
            self._percent()
        elif text in ("÷", "×", "-", "+"):
            self._set_operator(text)
        elif text == "=":
            self._calculate()

        self._update_display()

    def _input_digit(self, digit):
        if self.should_reset_display or self.current_value == "0":
            self.current_value = digit
            self.should_reset_display = False
        else:
            # جلوگیری از طولانی شدن بیش از حد عدد
            if len(self.current_value.replace("-", "").replace(".", "")) < 9:
                self.current_value += digit

    def _input_dot(self):
        if self.should_reset_display:
            self.current_value = "0."
            self.should_reset_display = False
            return
        if "." not in self.current_value:
            self.current_value += "."

    def _clear(self):
        self.current_value = "0"
        self.stored_value = None
        self.pending_operator = None
        self.should_reset_display = False

    def _toggle_sign(self):
        if self.current_value.startswith("-"):
            self.current_value = self.current_value[1:]
        elif self.current_value != "0":
            self.current_value = "-" + self.current_value

    def _percent(self):
        value = float(self.current_value) / 100
        self.current_value = self._format_number(value)

    def _set_operator(self, op):
        if self.pending_operator and not self.should_reset_display:
            self._calculate()
        self.stored_value = float(self.current_value)
        self.pending_operator = op
        self.should_reset_display = True

    def _calculate(self):
        if self.pending_operator is None or self.stored_value is None:
            return
        current = float(self.current_value)
        result = None

        try:
            if self.pending_operator == "+":
                result = self.stored_value + current
            elif self.pending_operator == "-":
                result = self.stored_value - current
            elif self.pending_operator == "×":
                result = self.stored_value * current
            elif self.pending_operator == "÷":
                result = self.stored_value / current
        except ZeroDivisionError:
            self.current_value = "Error"
            self.pending_operator = None
            self.stored_value = None
            self.should_reset_display = True
            return

        self.current_value = self._format_number(result)
        self.pending_operator = None
        self.stored_value = None
        self.should_reset_display = True

    @staticmethod
    def _format_number(value):
        # حذف اعشار غیرضروری (مثل 4.0 -> "4")
        if value == int(value) and abs(value) < 1e15:
            return str(int(value))
        formatted = f"{value:.8f}".rstrip("0").rstrip(".")
        return formatted

    def _update_display(self):
        text = self.current_value
        # اگر عدد خیلی بزرگ باشد فونت را کوچک‌تر می‌کنیم تا جا شود
        if len(text) > 9:
            self.display_label.config(font=("Helvetica", 40))
        else:
            self.display_label.config(font=FONT_DISPLAY)
        self.display_var.set(text)


def main():
    root = tk.Tk()
    app = iPhoneCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
    
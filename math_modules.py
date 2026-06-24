import customtkinter as ctk
import math
from colors import *


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


# ==================================================
# STANDARD CALCULATOR
# ==================================================

def show_standard_calculator(parent):

    clear_frame(parent)

    title = ctk.CTkLabel(
        parent,
        text="Standard Calculator",
        font=("Segoe UI", 24, "bold"),
        text_color=TEXT_WHITE
    )
    title.pack(pady=20)

    display_var = ctk.StringVar()

    display = ctk.CTkEntry(
        parent,
        width=400,
        height=70,
        font=("Consolas", 24, "bold"),
        fg_color="#4CAF50",
        text_color="black",
        textvariable=display_var,
        justify="right"
    )
    display.pack(pady=15)

    def button_click(value):
        display_var.set(display_var.get() + str(value))

    def clear_display():
        display_var.set("")

    def delete_last():
        display_var.set(display_var.get()[:-1])

    def calculate():
        try:
            result = eval(display_var.get())
            display_var.set(str(result))
        except:
            display_var.set("Error")

    def plus_minus():
        value = display_var.get()

        if value:
            if value.startswith("-"):
                display_var.set(value[1:])
            else:
                display_var.set("-" + value)

    buttons_frame = ctk.CTkFrame(
        parent,
        fg_color=BG_COLOR
    )
    buttons_frame.pack(pady=10)

    buttons = [
        ["C", "DEL", "%", "/"],
        ["7", "8", "9", "*"],
        ["4", "5", "6", "-"],
        ["1", "2", "3", "+"],
        ["+/-", "0", ".", "="]
    ]

    for r, row in enumerate(buttons):
        for c, text in enumerate(row):

            if text in ["C", "DEL"]:
                fg = CLEAR_BTN
                hover = CLEAR_HOVER

            elif text in ["+", "-", "*", "/", "="]:
                fg = OPERATOR_BTN
                hover = OPERATOR_HOVER

            else:
                fg = NUMBER_BTN
                hover = NUMBER_HOVER

            if text == "C":
                cmd = clear_display

            elif text == "DEL":
                cmd = delete_last

            elif text == "=":
                cmd = calculate

            elif text == "+/-":
                cmd = plus_minus

            else:
                cmd = lambda t=text: button_click(t)

            btn = ctk.CTkButton(
                buttons_frame,
                text=text,
                width=90,
                height=65,
                corner_radius=12,
                fg_color=fg,
                hover_color=hover,
                text_color="black",
                font=("Segoe UI", 18, "bold"),
                command=cmd
            )

            btn.grid(
                row=r,
                column=c,
                padx=6,
                pady=6
            )


# ==================================================
# SCIENTIFIC CALCULATOR
# ==================================================

def show_scientific_calculator(parent):

    clear_frame(parent)

    title = ctk.CTkLabel(
        parent,
        text="Scientific Calculator",
        font=("Segoe UI", 24, "bold"),
        text_color=TEXT_WHITE
    )
    title.pack(pady=20)

    display_var = ctk.StringVar()

    display = ctk.CTkEntry(
        parent,
        width=500,
        height=70,
        font=("Consolas", 24, "bold"),
        fg_color="#4CAF50",
        text_color="black",
        textvariable=display_var,
        justify="right"
    )
    display.pack(pady=15)

    def button_click(value):
        display_var.set(display_var.get() + str(value))

    def clear_display():
        display_var.set("")

    def calculate():
        try:
            result = eval(display_var.get())
            display_var.set(str(result))
        except:
            display_var.set("Error")

    def scientific_function(value):

        try:
            current = float(display_var.get())

            if value == "x²":
                display_var.set(str(current ** 2))

            elif value == "x³":
                display_var.set(str(current ** 3))

            elif value == "√":
                display_var.set(str(math.sqrt(current)))

            elif value == "1/x":
                display_var.set(str(1 / current))

            elif value == "log":
                display_var.set(str(math.log10(current)))

            elif value == "ln":
                display_var.set(str(math.log(current)))

            elif value == "10ˣ":
                display_var.set(str(10 ** current))

            elif value == "eˣ":
                display_var.set(str(math.exp(current)))

            elif value == "π":
                display_var.set(str(math.pi))

            elif value == "e":
                display_var.set(str(math.e))

            elif value == "n!":
                display_var.set(
                    str(math.factorial(int(current)))
                )

        except:
            display_var.set("Error")

    buttons_frame = ctk.CTkFrame(
        parent,
        fg_color=BG_COLOR
    )
    buttons_frame.pack(pady=10)

    buttons = [
        ["x²", "x³", "√", "1/x"],
        ["log", "ln", "10ˣ", "eˣ"],
        ["π", "e", "(", ")"],
        ["n!", "C", "/", "ANS"]
    ]

    for r, row in enumerate(buttons):
        for c, text in enumerate(row):

            if text == "ANS":
                fg = "#4CAF50"
                hover = "#45A049"

            elif text == "C":
                fg = CLEAR_BTN
                hover = CLEAR_HOVER

            else:
                fg = "#2E86DE"
                hover = "#3498DB"

            if text == "ANS":
                cmd = calculate

            elif text == "C":
                cmd = clear_display

            elif text in [
                "x²",
                "x³",
                "√",
                "1/x",
                "log",
                "ln",
                "10ˣ",
                "eˣ",
                "π",
                "e",
                "n!"
            ]:
                cmd = lambda t=text: scientific_function(t)

            else:
                cmd = lambda t=text: button_click(t)

            btn = ctk.CTkButton(
                buttons_frame,
                text=text,
                width=110,
                height=75,
                corner_radius=12,
                fg_color=fg,
                hover_color=hover,
                font=("Segoe UI", 18, "bold"),
                command=cmd
            )

            btn.grid(
                row=r,
                column=c,
                padx=8,
                pady=8
            )

def show_trigonometry_calculator(parent):

    clear_frame(parent)

    title = ctk.CTkLabel(
        parent,
        text="Trigonometry Calculator",
        font=("Segoe UI", 22, "bold"),
        text_color=TEXT_WHITE
    )
    title.pack(pady=(10, 5))

    # ==========================
    # MAIN LAYOUT
    # ==========================

    main_frame = ctk.CTkFrame(
        parent,
        fg_color="transparent"
    )
    main_frame.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=10
    )

    left_frame = ctk.CTkFrame(
        main_frame,
        fg_color="transparent"
    )

    right_frame = ctk.CTkFrame(
        main_frame,
        width=280
    )

    left_frame.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(0, 15)
    )

    right_frame.pack(
        side="right",
        fill="y"
    )

    angle_var = ctk.StringVar()
    mode_var = ctk.StringVar(value="DEG")

    # ==========================
    # INPUT
    # ==========================

    display = ctk.CTkEntry(
        left_frame,
        width=420,
        height=55,
        textvariable=angle_var,
        justify="right",
        font=("Consolas", 18, "bold"),
        fg_color="#7CB342",
        text_color="black",
        border_width=0
    )
    display.pack(pady=10)

    result_var = ctk.StringVar(value="Ready")

    result_box = ctk.CTkLabel(
        left_frame,
        textvariable=result_var,
        width=420,
        height=55,
        fg_color="#1E293B",
        corner_radius=10,
        text_color="white",
        font=("Consolas", 15, "bold")
    )
    result_box.pack(pady=(0, 10))

    def copy_result():

        parent.clipboard_clear()

        parent.clipboard_append(
            result_var.get()
        )

        result_var.set(
            "Result Copied ✓"
        )

    copy_btn = ctk.CTkButton(
        left_frame,
        text="📋 Copy Result",
        width=180,
        fg_color="#3949AB",
        hover_color="#5C6BC0",
        command=copy_result
    )
    copy_btn.pack(pady=(0, 15))

    # ==========================
    # HISTORY PANEL
    # ==========================

    history_title = ctk.CTkLabel(
        right_frame,
        text="History",
        font=("Segoe UI", 18, "bold")
    )
    history_title.pack(pady=(10, 10))

    history_box = ctk.CTkTextbox(
        right_frame,
        width=260,
        height=420,
        font=("Consolas", 13)
    )
    history_box.pack(
        padx=10,
        pady=5
    )

    history_box.insert(
        "end",
        "=== Calculation History ===\n\n"
    )

    clear_history_btn = ctk.CTkButton(
        right_frame,
        text="Clear History",
        fg_color="#8E24AA",
        hover_color="#AB47BC",
        command=lambda: history_box.delete(
            "1.0",
            "end"
        )
    )
    clear_history_btn.pack(pady=10)

    # ==========================
    # FUNCTIONS
    # ==========================

    def calculate(operation):

        try:

            expression = angle_var.get().replace(
                "^",
                "**"
            )

            angle = eval(
                expression,
                {"__builtins__": None},
                {
                    "pi": math.pi,
                    "e": math.e
                }
            )

            if mode_var.get() == "DEG":
                value = math.radians(angle)
            else:
                value = angle

            if operation == "sin":
                result = math.sin(value)

            elif operation == "cos":
                result = math.cos(value)

            elif operation == "tan":
                result = math.tan(value)

            elif operation == "cot":
                result = 1 / math.tan(value)

            elif operation == "sec":
                result = 1 / math.cos(value)

            elif operation == "cosec":
                result = 1 / math.sin(value)

            elif operation == "sin⁻¹":

                if angle < -1 or angle > 1:
                    result_var.set("Domain Error")
                    return

                result = math.degrees(
                    math.asin(angle)
                )

            elif operation == "cos⁻¹":

                if angle < -1 or angle > 1:
                    result_var.set("Domain Error")
                    return

                result = math.degrees(
                    math.acos(angle)
                )

            elif operation == "tan⁻¹":
                result = math.degrees(
                    math.atan(angle)
                )

            formatted_result = (
                f"{operation}({expression}) = "
                f"{round(result, 8)}"
            )

            result_var.set(
                formatted_result
            )

            history_box.insert(
                "end",
                formatted_result + "\n"
            )

            history_box.see("end")

        except:
            result_var.set("Error")

    def set_deg():

        mode_var.set("DEG")

        deg_btn.configure(
            fg_color="#4CAF50"
        )

        rad_btn.configure(
            fg_color="#1976D2"
        )

        result_var.set(
            "Degree Mode"
        )

    def set_rad():

        mode_var.set("RAD")

        rad_btn.configure(
            fg_color="#4CAF50"
        )

        deg_btn.configure(
            fg_color="#1976D2"
        )

        result_var.set(
            "Radian Mode"
        )

    def clear_all():

        angle_var.set("")

        result_var.set("Ready")

        display.focus()

    def enter_pressed(event):

        calculate("sin")

    display.bind(
        "<Return>",
        enter_pressed
    )

    # ==========================
    # BUTTONS
    # ==========================

    buttons_frame = ctk.CTkFrame(
        left_frame,
        fg_color="transparent"
    )
    buttons_frame.pack(pady=10)

    buttons = [
        ["sin", "cos", "tan"],
        ["cosec", "sec", "cot"],
        ["sin⁻¹", "cos⁻¹", "tan⁻¹"]
    ]

    for r, row in enumerate(buttons):
        for c, text in enumerate(row):

            btn = ctk.CTkButton(
                buttons_frame,
                text=text,
                width=130,
                height=60,
                corner_radius=10,
                fg_color="#2F7E8A",
                hover_color="#3F95A3",
                font=("Segoe UI", 15, "bold"),
                command=lambda t=text: calculate(t)
            )

            btn.grid(
                row=r,
                column=c,
                padx=8,
                pady=8
            )

    mode_frame = ctk.CTkFrame(
        left_frame,
        fg_color="transparent"
    )
    mode_frame.pack(pady=15)

    deg_btn = ctk.CTkButton(
        mode_frame,
        text="DEG",
        width=110,
        fg_color="#4CAF50",
        command=set_deg
    )
    deg_btn.grid(
        row=0,
        column=0,
        padx=10
    )

    rad_btn = ctk.CTkButton(
        mode_frame,
        text="RAD",
        width=110,
        fg_color="#1976D2",
        command=set_rad
    )
    rad_btn.grid(
        row=0,
        column=1,
        padx=10
    )

    clr_btn = ctk.CTkButton(
        mode_frame,
        text="CLR",
        width=110,
        fg_color="#E53935",
        hover_color="#EF5350",
        command=clear_all
    )
    clr_btn.grid(
        row=0,
        column=2,
        padx=10
    )

import customtkinter as ctk
from datetime import datetime

from colors import *
from fonts import *


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def show_programmer_calculator(parent):

    clear_frame(parent)

    # ==================================
    # TITLE
    # ==================================

    title = ctk.CTkLabel(
        parent,
        text="💻 Programmer Calculator",
        font=TITLE_FONT
    )
    title.pack(pady=10)

    # ==================================
    # MAIN FRAME
    # ==================================

    main_frame = ctk.CTkFrame(
        parent,
        fg_color="transparent"
    )

    main_frame.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    # ==================================
    # LEFT PANEL
    # ==================================

    left_panel = ctk.CTkFrame(
        main_frame,
        fg_color="transparent"
    )

    left_panel.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(0, 10)
    )

    # ==================================
    # RIGHT HISTORY PANEL
    # ==================================

    right_panel = ctk.CTkFrame(
        main_frame,
        width=260,
        fg_color=CARD_COLOR
    )

    right_panel.pack(
        side="right",
        fill="y"
    )

    right_panel.pack_propagate(False)

    # ==================================
    # TOP SECTION
    # ==================================

    top_section = ctk.CTkFrame(
        left_panel,
        fg_color="transparent"
    )

    top_section.pack(
        fill="both",
        expand=True
    )

    # ==================================
    # CONVERTER FRAME
    # ==================================

    converter_frame = ctk.CTkFrame(
        top_section,
        fg_color=CARD_COLOR
    )

    converter_frame.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(0, 5)
    )

    # ==================================
    # BITWISE FRAME
    # ==================================

    bitwise_frame = ctk.CTkFrame(
        top_section,
        fg_color=CARD_COLOR
    )

    bitwise_frame.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(5, 0)
    )

    # ==================================
    # NUMBER INPUT
    # ==================================

    ctk.CTkLabel(
        converter_frame,
        text="Enter Number",
        font=SUBTITLE_FONT
    ).pack(pady=(15, 5))

    number_entry = ctk.CTkEntry(
        converter_frame,
        height=40,
        font=ENTRY_FONT
    )

    number_entry.pack(
        fill="x",
        padx=20
    )

    # ==================================
    # CONVERT FROM
    # ==================================

    from_var = ctk.StringVar(value="Decimal")

    ctk.CTkLabel(
        converter_frame,
        text="Convert From",
        font=SUBTITLE_FONT
    ).pack(pady=(15, 5))

    for item in [
        "Decimal",
        "Binary",
        "Octal",
        "Hexadecimal"
    ]:

        ctk.CTkRadioButton(
            converter_frame,
            text=item,
            variable=from_var,
            value=item
        ).pack(
            anchor="w",
            padx=30,
            pady=2
        )

    # ==================================
    # CONVERT TO
    # ==================================

    to_var = ctk.StringVar(value="Binary")

    ctk.CTkLabel(
        converter_frame,
        text="Convert To",
        font=SUBTITLE_FONT
    ).pack(pady=(15, 5))

    for item in [
        "Decimal",
        "Binary",
        "Octal",
        "Hexadecimal"
    ]:

        ctk.CTkRadioButton(
            converter_frame,
            text=item,
            variable=to_var,
            value=item
        ).pack(
            anchor="w",
            padx=30,
            pady=2
        )

    # ==================================
    # SECOND NUMBER
    # ==================================

    ctk.CTkLabel(
        bitwise_frame,
        text="Second Number",
        font=SUBTITLE_FONT
    ).pack(pady=(15, 5))

    number2_entry = ctk.CTkEntry(
        bitwise_frame,
        height=40,
        font=ENTRY_FONT
    )

    number2_entry.pack(
        fill="x",
        padx=20
    )

    # ==================================
    # RESULT CARD
    # ==================================

    result_var = ctk.StringVar(
        value="Result Will Appear Here"
    )

    result_label = ctk.CTkLabel(
        bitwise_frame,
        textvariable=result_var,
        font=DISPLAY_FONT,
        fg_color=DISPLAY_COLOR,
        text_color="black",
        corner_radius=10,
        height=60
    )

    result_label.pack(
        fill="x",
        padx=20,
        pady=20
    )

    # ==================================
    # FUNCTIONS
    # ==================================

    def convert_number():

        try:

            value = number_entry.get().strip()

            if not value:
                return

            from_type = from_var.get()
            to_type = to_var.get()

            if from_type == "Decimal":
                decimal_value = int(value)

            elif from_type == "Binary":
                decimal_value = int(value, 2)

            elif from_type == "Octal":
                decimal_value = int(value, 8)

            else:
                decimal_value = int(value, 16)

            if to_type == "Decimal":
                result = str(decimal_value)

            elif to_type == "Binary":
                result = bin(decimal_value)[2:]

            elif to_type == "Octal":
                result = oct(decimal_value)[2:]

            else:
                result = hex(decimal_value)[2:].upper()

            result_var.set(result)

            current_time = datetime.now().strftime("%H:%M")

            history_box.insert(
                "end",
                f"[{current_time}] {value} ({from_type}) → {result} ({to_type})\n"
            )

        except:
            result_var.set("Invalid Input")

    def bitwise_operation(operation):

        try:

            if operation == "NOT":

                num1 = int(number_entry.get())
                result = ~num1

            else:

                num1 = int(number_entry.get())
                num2 = int(number2_entry.get())

                if operation == "AND":
                    result = num1 & num2

                elif operation == "OR":
                    result = num1 | num2

                elif operation == "XOR":
                    result = num1 ^ num2

                elif operation == "LEFT":
                    result = num1 << num2

                elif operation == "RIGHT":
                    result = num1 >> num2

            result_var.set(str(result))

            current_time = datetime.now().strftime("%H:%M")

            if operation == "NOT":

                history_box.insert(
                    "end",
                    f"[{current_time}] NOT {num1} = {result}\n"
                )

            else:

                history_box.insert(
                    "end",
                    f"[{current_time}] {num1} {operation} {num2} = {result}\n"
                )

        except:

            result_var.set("Invalid Input")
    def copy_result():

        parent.clipboard_clear()
        parent.clipboard_append(result_var.get())


    def clear_all():

        number_entry.delete(0, "end")
        number2_entry.delete(0, "end")

        result_var.set(
                "Result Will Appear Here"
        )


    def clear_history():

        history_box.delete(
            "1.0",
            "end"
        )

    # ==================================
    # BUTTON SECTION
    # ==================================

    button_frame = ctk.CTkFrame(
        bitwise_frame,
        fg_color="transparent"
    )

    button_frame.pack(
        pady=10
    )

    # ROW 1

    ctk.CTkButton(
        button_frame,
        text="Convert",
        command=convert_number,
        fg_color=BUTTON_GREEN,
        hover_color="#4CAF50",
        font=BUTTON_FONT,
        width=120
    ).grid(
        row=0,
        column=0,
        padx=5,
        pady=5
    )

    ctk.CTkButton(
        button_frame,
        text="Copy",
        command=copy_result,
        fg_color=BUTTON_BLUE,
        hover_color="#2196F3",
        font=BUTTON_FONT,
        width=120
    ).grid(
        row=0,
        column=1,
        padx=5,
        pady=5
    )

    # ROW 2

    ctk.CTkButton(
        button_frame,
        text="Clear",
        command=clear_all,
        fg_color=CLEAR_BTN,
        hover_color=CLEAR_HOVER,
        text_color="black",
        font=BUTTON_FONT,
        width=120
    ).grid(
        row=1,
        column=0,
        padx=5,
        pady=5
    )

    ctk.CTkButton(
        button_frame,
        text="AND",
        command=lambda: bitwise_operation("AND"),
        fg_color=BUTTON_PURPLE,
        hover_color="#8E24AA",
        font=BUTTON_FONT,
        width=120
    ).grid(
        row=1,
        column=1,
        padx=5,
        pady=5
    )

    # ROW 3

    ctk.CTkButton(
        button_frame,
        text="OR",
        command=lambda: bitwise_operation("OR"),
        fg_color=BUTTON_PURPLE,
        hover_color="#8E24AA",
        font=BUTTON_FONT,
        width=120
    ).grid(
        row=2,
        column=0,
        padx=5,
        pady=5
    )

    ctk.CTkButton(
        button_frame,
        text="XOR",
        command=lambda: bitwise_operation("XOR"),
        fg_color=BUTTON_PURPLE,
        hover_color="#8E24AA",
        font=BUTTON_FONT,
        width=120
    ).grid(
        row=2,
        column=1,
        padx=5,
        pady=5
    )

    # ROW 4

    ctk.CTkButton(
        button_frame,
        text="<<",
        command=lambda: bitwise_operation("LEFT"),
        fg_color=BUTTON_PURPLE,
        hover_color="#8E24AA",
        font=BUTTON_FONT,
        width=120
    ).grid(
        row=3,
        column=0,
        padx=5,
        pady=5
    )

    ctk.CTkButton(
        button_frame,
        text=">>",
        command=lambda: bitwise_operation("RIGHT"),
        fg_color=BUTTON_PURPLE,
        hover_color="#8E24AA",
        font=BUTTON_FONT,
        width=120
    ).grid(
        row=3,
        column=1,
        padx=5,
        pady=5
    )

    ctk.CTkButton(
        button_frame,
        text="NOT",
        command=lambda: bitwise_operation("NOT"),
        fg_color=BUTTON_PURPLE,
        hover_color="#8E24AA",
        font=BUTTON_FONT,
        width=120
    ).grid(
        row=4,
        column=0,
        columnspan=2,
        padx=5,
        pady=5,
        sticky="ew"
    )

    # ==================================
    # HISTORY PANEL
    # ==================================

    history_title = ctk.CTkLabel(
        right_panel,
        text="📜 History",
        font=SUBTITLE_FONT
    )

    history_title.pack(
        pady=10
    )

    history_box = ctk.CTkTextbox(
        right_panel,
        font=TEXT_FONT
    )

    history_box.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    ctk.CTkButton(
        right_panel,
        text="Clear History",
        command=clear_history,
        fg_color=CLEAR_BTN,
        hover_color=CLEAR_HOVER,
        text_color="black",
        font=BUTTON_FONT
    ).pack(
        padx=10,
        pady=10,
        fill="x"
    )        
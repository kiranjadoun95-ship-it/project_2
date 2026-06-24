import customtkinter as ctk

from colors import *
from fonts import *


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def show_unit_converter(parent):

    clear_frame(parent)

    title = ctk.CTkLabel(
        parent,
        text="📏 Unit Converter",
        font=TITLE_FONT
    )
    title.pack(pady=10)

    main_frame = ctk.CTkFrame(parent)
    main_frame.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    left_frame = ctk.CTkFrame(main_frame)
    left_frame.pack(
        side="left",
        fill="both",
        expand=True,
        padx=5
    )

    right_frame = ctk.CTkFrame(
        main_frame,
        width=250
    )
    right_frame.pack(
        side="right",
        fill="y",
        padx=5
    )

    # =========================
    # CONVERSION TYPE
    # =========================

    conversion_type = ctk.StringVar(
        value="Length"
    )

    ctk.CTkLabel(
        left_frame,
        text="Conversion Type"
    ).pack(
        pady=(15, 5)
    )

    type_menu = ctk.CTkOptionMenu(
        left_frame,
        values=[
            "Length",
            "Weight",
            "Temperature",
            "Area",
            "Volume"
        ],
        variable=conversion_type
    )
    type_menu.pack(
        fill="x",
        padx=20
    )

    # =========================
    # FROM UNIT
    # =========================

    ctk.CTkLabel(
        left_frame,
        text="From Unit"
    ).pack(
        pady=(15, 5)
    )

    from_unit = ctk.StringVar(
        value="Meter"
    )

    from_menu = ctk.CTkOptionMenu(
        left_frame,
        values=[
            "Millimeter",
            "Centimeter",
            "Meter",
            "Kilometer"
        ],
        variable=from_unit
    )
    from_menu.pack(
        fill="x",
        padx=20
    )

    # =========================
    # TO UNIT
    # =========================

    ctk.CTkLabel(
        left_frame,
        text="To Unit"
    ).pack(
        pady=(15, 5)
    )

    to_unit = ctk.StringVar(
        value="Kilometer"
    )

    to_menu = ctk.CTkOptionMenu(
        left_frame,
        values=[
            "Millimeter",
            "Centimeter",
            "Meter",
            "Kilometer"
        ],
        variable=to_unit
    )
    to_menu.pack(
        fill="x",
        padx=20
    )

    # =========================
    # VALUE ENTRY
    # =========================

    ctk.CTkLabel(
        left_frame,
        text="Enter Value"
    ).pack(
        pady=(15, 5)
    )

    value_entry = ctk.CTkEntry(
        left_frame,
        placeholder_text="Enter Value"
    )
    value_entry.pack(
        fill="x",
        padx=20
    )

    # =========================
    # RESULT
    # =========================

    result_var = ctk.StringVar(
        value="Result will appear here"
    )

    result_label = ctk.CTkLabel(
        left_frame,
        textvariable=result_var,
        font=("Arial", 18, "bold")
    )
    result_label.pack(
        pady=15
    )

    # =========================
    # FUNCTIONS
    # =========================

    def convert_unit():

        try:

            value = float(value_entry.get())

            if conversion_type.get() == "Length":

                length_units = {
                    "Millimeter": 0.001,
                    "Centimeter": 0.01,
                    "Meter": 1,
                    "Kilometer": 1000
                }

                meter_value = (
                    value *
                    length_units[from_unit.get()]
                )

                result = (
                    meter_value /
                    length_units[to_unit.get()]
                )

                result_var.set(
                    f"{result:.6f}"
                )

            elif conversion_type.get() == "Weight":

                weight_units = {
                    "Milligram": 0.001,
                    "Gram": 1,
                    "Kilogram": 1000
                }

                gram_value = (
                    value *
                    weight_units[from_unit.get()]
                )

                result = (
                    gram_value /
                    weight_units[to_unit.get()]
                )

                result_var.set(
                    f"{result:.6f}"
                )

            elif conversion_type.get() == "Temperature":

                if from_unit.get() == to_unit.get():

                    result = value

                elif (
                    from_unit.get() == "Celsius"
                    and
                    to_unit.get() == "Fahrenheit"
                ):

                    result = (value * 9 / 5) + 32

                elif (
                    from_unit.get() == "Fahrenheit"
                    and
                    to_unit.get() == "Celsius"
                ):

                    result = (value - 32) * 5 / 9

                elif (
                    from_unit.get() == "Celsius"
                    and
                    to_unit.get() == "Kelvin"
                ):

                    result = value + 273.15

                elif (
                    from_unit.get() == "Kelvin"
                    and
                    to_unit.get() == "Celsius"
                ):

                    result = value - 273.15

                elif (
                    from_unit.get() == "Fahrenheit"
                    and
                    to_unit.get() == "Kelvin"
                ):

                    result = ((value - 32) * 5 / 9) + 273.15

                elif (
                    from_unit.get() == "Kelvin"
                    and
                    to_unit.get() == "Fahrenheit"
                ):

                    result = ((value - 273.15) * 9 / 5) + 32

                result_var.set(
                    f"{result:.2f}"
                )

            elif conversion_type.get() == "Area":

                area_units = {
                    "Square Meter": 1,
                    "Square Kilometer": 1000000,
                    "Square Foot": 0.092903,
                    "Square Inch": 0.00064516
                }

                base_value = (
                    value *
                    area_units[from_unit.get()]
                )

                result = (
                    base_value /
                    area_units[to_unit.get()]
                )

                result_var.set(
                    f"{result:.6f}"
                )

                details_box.delete(
                    "1.0",
                    "end"
                )

                details_box.insert(
                    "end",
                    f"Conversion Type : Area\n\n"
                    f"Input Value : {value}\n"
                    f"From Unit : {from_unit.get()}\n"
                    f"To Unit : {to_unit.get()}\n\n"
                    f"Result : {result:.6f}"
                )

                history_box.insert(
                    "end",
                    f"{value} {from_unit.get()} → {result:.6f} {to_unit.get()}\n"
                )

                history_box.see("end")


            elif conversion_type.get() == "Volume":

                volume_units = {
                    "Milliliter": 0.001,
                    "Liter": 1,
                    "Cubic Meter": 1000
                }

                base_value = (
                    value *
                    volume_units[from_unit.get()]
                )

                result = (
                    base_value /
                    volume_units[to_unit.get()]
                )

                result_var.set(
                    f"{result:.6f}"
                )

                details_box.delete(
                    "1.0",
                    "end"
                )

                details_box.insert(
                    "end",
                    f"Conversion Type : Volume\n\n"
                    f"Input Value : {value}\n"
                    f"From Unit : {from_unit.get()}\n"
                    f"To Unit : {to_unit.get()}\n\n"
                    f"Result : {result:.6f}"
                )

                history_box.insert(
                    "end",
                    f"{value} {from_unit.get()} → {result:.6f} {to_unit.get()}\n"
                )

                history_box.see("end")    

            else:

                result_var.set(
                    "Coming Soon..."
                )

                return

            details_box.delete(
                "1.0",
                "end"
            )

            details_box.insert(
                "end",
                f"Conversion Type : {conversion_type.get()}\n\n"
                f"Input Value : {value}\n"
                f"From Unit : {from_unit.get()}\n"
                f"To Unit : {to_unit.get()}\n\n"
                f"Result : {result}"
            )

            history_box.insert(
                "end",
                f"{value} {from_unit.get()} → {result} {to_unit.get()}\n"
            )

            history_box.see("end")

        except:

            result_var.set(
                "Invalid Input"
            )

    def update_units(choice):

        if conversion_type.get() == "Length":

            units = [
                "Millimeter",
                "Centimeter",
                "Meter",
                "Kilometer"
            ]

        elif conversion_type.get() == "Weight":

            units = [
                "Milligram",
                "Gram",
                "Kilogram"
            ]

        elif conversion_type.get() == "Temperature":

            units = [
                "Celsius",
                "Fahrenheit",
                "Kelvin"
            ]

        elif conversion_type.get() == "Area":

            units = [
                "Square Meter",
                "Square Kilometer",
                "Square Foot",
                "Square Inch"
            ]

        elif conversion_type.get() == "Volume":

            units = [
                 "Milliliter",
                 "Liter",
                 "Cubic Meter"
            ]    

        else:

            units = ["Coming Soon"]

        from_menu.configure(
            values=units
        )

        to_menu.configure(
            values=units
        )

        from_unit.set(
            units[0]
        )

        to_unit.set(
            units[-1]
        )

    def copy_result():

        parent.clipboard_clear()

        parent.clipboard_append(
            result_var.get()
        )

    def clear_all():

        value_entry.delete(
            0,
            "end"
        )

        result_var.set(
            "Result will appear here"
        )

        details_box.delete(
            "1.0",
            "end"
        )

    def clear_history():

        history_box.delete(
            "1.0",
            "end"
        )
# =========================
    # BUTTONS
    # =========================

    button_frame = ctk.CTkFrame(
        left_frame,
        fg_color="transparent"
    )
    button_frame.pack(
        pady=10
    )

    ctk.CTkButton(
        button_frame,
        text="Convert",
        width=130,
        command=convert_unit
    ).grid(
        row=0,
        column=0,
        padx=5
    )

    ctk.CTkButton(
        button_frame,
        text="Copy Result",
        width=130,
        command=copy_result
    ).grid(
        row=0,
        column=1,
        padx=5
    )

    ctk.CTkButton(
        button_frame,
        text="Clear",
        width=130,
        command=clear_all
    ).grid(
        row=0,
        column=2,
        padx=5
    )

    # =========================
    # DETAILS BOX
    # =========================

    details_box = ctk.CTkTextbox(
        left_frame,
        height=120
    )

    details_box.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=10
    )

    # =========================
    # HISTORY
    # =========================

    history_title = ctk.CTkLabel(
        right_frame,
        text="History"
    )

    history_title.pack(
        pady=10
    )

    history_box = ctk.CTkTextbox(
        right_frame
    )

    history_box.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    # =========================
    # CLEAR HISTORY
    # =========================

    ctk.CTkButton(
        right_frame,
        text="Clear History",
        command=clear_history
    ).pack(
        pady=10
    )

    type_menu.configure(
        command=update_units
    )
    update_units(None)
import customtkinter as ctk

from colors import *
from fonts import *


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def show_health_bmi(parent):

    clear_frame(parent)

    title = ctk.CTkLabel(
        parent,
        text="❤️ Health & BMI",
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
    # HEIGHT
    # =========================

    ctk.CTkLabel(
        left_frame,
        text="Height (cm)"
    ).pack(
        pady=(15, 5)
    )

    height_entry = ctk.CTkEntry(
        left_frame,
        placeholder_text="Enter Height"
    )
    height_entry.pack(
        fill="x",
        padx=20
    )

    # =========================
    # WEIGHT
    # =========================

    ctk.CTkLabel(
        left_frame,
        text="Weight (kg)"
    ).pack(
        pady=(15, 5)
    )

    weight_entry = ctk.CTkEntry(
        left_frame,
        placeholder_text="Enter Weight"
    )
    weight_entry.pack(
        fill="x",
        padx=20
    )

# =========================
# AGE
# =========================

    ctk.CTkLabel(
        left_frame,
        text="Age"
    ).pack(
        pady=(15, 5)
    )

    age_entry = ctk.CTkEntry(
        left_frame,
        placeholder_text="Enter Age"
    )

    age_entry.pack(
        fill="x",
        padx=20
    )

    # =========================
    # RESULT
    # =========================

    result_var = ctk.StringVar(
        value="BMI Result Will Appear Here"
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
        text="BMI History"
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
# FUNCTIONS
# =========================

    def calculate_bmi():

        try:

            h = float(height_entry.get())
            w = float(weight_entry.get())
            age= int(age_entry.get())

            if h <= 0 or w <= 0:
                result_var.set(
                    "Enter Valid Values"
                )
                return

            bmi = round(
                w / ((h / 100) ** 2),
                2
            )

            if bmi < 18.5:
                status = "Underweight"

            elif bmi < 25:
                status = "Normal"

            elif bmi < 30:
                status = "Overweight"

            else:
                status = "Obese"

            result_var.set(
                f"BMI : {bmi} | {status}"
            )

            details_box.delete(
                "1.0",
                "end"
            )

            details_box.insert(
                "end",
                f"Height : {h} cm\n"
                f"Weight : {w} kg\n"
                f"Age : {age} years\n"
                f"BMI : {bmi}\n"
                f"Category : {status}\n\n"
            )
            water = round(w*0.033,2)

            if status == "Underweight":

                details_box.insert(
                    "end",
                    "Suggestion:\nIncrease healthy food intake and exercise."
                )

            elif status == "Normal":

                details_box.insert(
                    "end",
                    "Suggestion:\nExcellent! Maintain your lifestyle."
                )

            elif status == "Overweight":

                details_box.insert(
                    "end",
                    "Suggestion:\nRegular exercise and balanced diet recommended."
                )

            else:

                details_box.insert(
                    "end",
                    "Suggestion:\nConsult a healthcare professional."
                )
            
            details_box.insert(
                "end",
                f"\n\n💧 Recommended Water Intake : {water} Liters/Day"
            )
            history_box.insert(
                "end",
                f"BMI: {bmi} | {status}\n"
            )

        except:

            result_var.set(
                "Invalid Input"
            )


    def copy_result():

        parent.clipboard_clear()
        parent.clipboard_append(
            result_var.get()
        )


    def clear_all():

        height_entry.delete(
            0,
            "end"
        )

        weight_entry.delete(
            0,
            "end"
        )

        result_var.set(
            "BMI Result Will Appear Here"
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
        text="Calculate BMI",
        command=calculate_bmi
    ).grid(
        row=0,
        column=0,
        padx=5
    )

    ctk.CTkButton(
        button_frame,
        text="Copy Result",
        command=copy_result
    ).grid(
        row=0,
        column=1,
        padx=5
    )

    ctk.CTkButton(
        button_frame,
        text="Clear",
        command=clear_all
    ).grid(
        row=0,
        column=2,
        padx=5
    )

    # =========================
    # CLEAR HISTORY BUTTON
    # =========================

    ctk.CTkButton(
        right_frame,
        text="Clear History",
        command=clear_history
    ).pack(
        pady=10
    )    
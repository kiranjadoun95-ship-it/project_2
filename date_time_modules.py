import customtkinter as ctk
from datetime import datetime
from colors import *
from fonts import *

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def show_date_time_calculator(parent):

    clear_frame(parent)

    title = ctk.CTkLabel(
        parent,
        text="📅 Date & Time Calculator",
        font=TITLE_FONT
    )
    title.pack(pady=10)

    #===================
    # MAIN LAYOUT
    #===================

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
# DATE INPUTS
# =========================

    ctk.CTkLabel(
        left_frame,
        text="Date 1 (DD/MM/YYYY)"
    ).pack(
        pady=(15, 5)
    )

    date1_entry = ctk.CTkEntry(
        left_frame,
        placeholder_text="01/01/2026"
    )

    date1_entry.pack(
        fill="x",
        padx=20
    )

    ctk.CTkLabel(
        left_frame,
        text="Date 2 (DD/MM/YYYY)"
    ).pack(
        pady=(15, 5)
    )

    date2_entry = ctk.CTkEntry(
        left_frame,
        placeholder_text="31/12/2026"
    )

    date2_entry.pack(
        fill="x",
        padx=20
    )

# =========================
# RESULT LABEL
# =========================

    result_var = ctk.StringVar(
        value="Result Will Appear Here"
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
# HISTORY
# =========================

    history_title = ctk.CTkLabel(
        right_frame,
        text="Date History"
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

    def current_date():

        today = datetime.now().strftime(
            "%d/%m/%Y"
        )

        result_var.set(
            f"Today : {today}"
        )

        history_box.insert(
            "end",
            f"Current Date : {today}\n"
        )


    def current_time():

        now = datetime.now().strftime(
            "%H:%M:%S"
        )

        result_var.set(
            f"Current Time : {now}"
        )

        history_box.insert(
            "end",
            f"Current Time : {now}\n"
        )


    def find_difference():

        try:

            d1 = datetime.strptime(
                date1_entry.get(),
                "%d/%m/%Y"
            )

            d2 = datetime.strptime(
                date2_entry.get(),
                "%d/%m/%Y"
            )

            days = abs(
                (d2 - d1).days
            )

            result_var.set(
                f"{days} Days Difference"
            )

            history_box.insert(
                "end",
                f"Difference : {days} Days\n"
            )

        except:

            result_var.set(
                "Invalid Date Format"
            )


    def calculate_age():

        try:

            birth_date = datetime.strptime(
                date1_entry.get(),
                "%d/%m/%Y"
            )

            today = datetime.now()

            age = today.year - birth_date.year

            if (
                today.month,
                today.day
            ) < (
                birth_date.month,
                birth_date.day
            ):

                age -= 1

            result_var.set(
                f"Age : {age} Years"
            )

            history_box.insert(
                "end",
                f"Age : {age} Years\n"
            )

        except:

            result_var.set(
                "Invalid Birth Date"
            )
    def find_day():

        try:

            selected_date = datetime.strptime(
                date1_entry.get(),
                "%d/%m/%Y"
            )

            day_name = selected_date.strftime(
                "%A"
            )

            result_var.set(
                f"Day : {day_name}"
            )

            history_box.insert(
                "end",
                f"Day : {day_name}\n"
            )

        except:

            result_var.set(
                "Invalid Date"
            )
    def countdown():

        try:

            target_date = datetime.strptime(
                date1_entry.get(),
                "%d/%m/%Y"
            )

            today = datetime.now()

            remaining_days = (
                target_date - today
            ).days

            result_var.set(
                f"{remaining_days} Days Remaining"
            )

            history_box.insert(
                "end",
                f"Countdown : {remaining_days} Days\n"
            )

        except:

            result_var.set(
                "Invalid Date"
            )
    def check_leap_year():

        try:

            year = datetime.strptime(
                date1_entry.get(),
                "%d/%m/%Y"
            ).year

            if (
                year % 400 == 0
                or
                (year % 4 == 0 and year % 100 != 0)
            ):

                result_var.set(
                    f"{year} is a Leap Year"
                )

                history_box.insert(
                    "end",
                    f"Leap Year : {year}\n"
                )

            else:

                result_var.set(
                    f"{year} is Not a Leap Year"
                )

                history_box.insert(
                    "end",
                    f"Not Leap Year : {year}\n"
                )

        except:

            result_var.set(
                "Invalid Date"
            )                        
    

    def clear_all():

        date1_entry.delete(
            0,
            "end"
        )

        date2_entry.delete(
            0,
            "end"
        )

        result_var.set(
            "Result Will Appear Here"
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
            text="Current Date",
            command=current_date
        ).grid(
            row=0,
            column=0,
            padx=5
        )

    ctk.CTkButton(
            button_frame,
            text="Current Time",
            command=current_time
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

    ctk.CTkButton(
        button_frame,
        text="Find Difference",
        command=find_difference
    ).grid(
        row=1,
        column=0,
        padx=5,
        pady=5
    )

    ctk.CTkButton(
            button_frame,
            text="Calculate Age",
            command=calculate_age
        ).grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )
    
    ctk.CTkButton(
        button_frame,
        text="Find Day",
        command=find_day
    ).grid(
        row=1,
        column=2,
        padx=5,
        pady=5
    )

    ctk.CTkButton(
        button_frame,
        text="Countdown",
        command=countdown
    ).grid(
        row=2,
        column=0,
        padx=5,
        pady=5
    )

    ctk.CTkButton(
        button_frame,
        text="Leap Year",
        command=check_leap_year
    ).grid(
        row=2,
        column=1,
        padx=5,
        pady=5
    )
    
    
    ctk.CTkButton(
            right_frame,
            text="Clear History",
            command=clear_history
        ).pack(
            pady=10
        )
    
    


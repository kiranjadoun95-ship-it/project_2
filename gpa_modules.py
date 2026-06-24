import customtkinter as ctk
from datetime import datetime

from colors import *
from fonts import *


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def show_gpa_calculator(parent):

    clear_frame(parent)

    title = ctk.CTkLabel(
        parent,
        text="🎓 GPA Calculator",
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

    left_frame = ctk.CTkFrame(
    main_frame
)

    left_frame.pack(
        side="left",
        fill="both",
        expand=True,
        padx=5
    )

    

    right_frame = ctk.CTkFrame(
            main_frame,
            width=300
        )
    right_frame.pack(
            side="right",
            fill="both",
            padx=5,
            pady=5
        )

    

# =========================
# GPA DETAILS PANEL
# =========================

    details_title = ctk.CTkLabel(
        right_frame,
        text="📊 GPA Details",
        font=("Arial", 16, "bold")
    )

    details_title.pack(
        pady=(10, 5)
    )

    details_box = ctk.CTkTextbox(
        right_frame,
        height=140
    )

    details_box.pack(
        fill="x",
        padx=10,
        pady=(0, 10)
    )

    details_box.insert(
        "end",
        "GPA details will appear here..."
    )
    
# =========================
# SUBJECT INPUTS
# =========================

    ctk.CTkLabel(
        left_frame,
        text="Subject 1 Marks"
    ).pack(pady=(6, 2))

    sub1_entry = ctk.CTkEntry(
        left_frame,
        height=32
    )
    sub1_entry.pack(fill="x", padx=20)

    ctk.CTkLabel(
        left_frame,
        text="Subject 2 Marks"
    ).pack(pady=(6, 2))

    sub2_entry = ctk.CTkEntry(
        left_frame,
        height=32
    )
    sub2_entry.pack(fill="x", padx=20)

    ctk.CTkLabel(
        left_frame,
        text="Subject 3 Marks"
    ).pack(pady=(6, 2))

    sub3_entry = ctk.CTkEntry(
        left_frame,
        height=32
    )
    sub3_entry.pack(fill="x", padx=20)

    ctk.CTkLabel(
        left_frame,
        text="Subject 4 Marks"
    ).pack(pady=(6, 2))

    sub4_entry = ctk.CTkEntry(
        left_frame,
        height=32
    )
    sub4_entry.pack(fill="x", padx=20)

    ctk.CTkLabel(
        left_frame,
        text="Subject 5 Marks"
    ).pack(pady=(6, 2))

    sub5_entry = ctk.CTkEntry(
        left_frame,
        height=32
    )
    sub5_entry.pack(fill="x", padx=20)

# =========================
# DYNAMIC SUBJECTS
# =========================

    subject_entries = [
        sub1_entry,
        sub2_entry,
        sub3_entry,
        sub4_entry,
        sub5_entry
    ]

    subjects_frame = ctk.CTkFrame(
        left_frame,
        fg_color="transparent"
    )
    
    # =========================
# RESULT
# =========================

    result_var = ctk.StringVar(
        value="GPA Result Will Appear Here"
    )

    result_label = ctk.CTkLabel(
    left_frame,
    textvariable=result_var,
    font=("Arial", 18, "bold"),
    fg_color="#1E7D32",
    corner_radius=10,
    height=45
)

    result_label.pack(
        fill="x",
        padx=20,
        pady=15
    )
    
# =========================
# FUNCTIONS
# =========================

    def add_subject():

        subject_no = len(subject_entries) + 1

        ctk.CTkLabel(
            subjects_frame,
            text=f"Subject {subject_no} Marks"
        ).pack(pady=(10, 5))

        new_entry = ctk.CTkEntry(subjects_frame)

        new_entry.pack(
            fill="x",
            padx=20
        )

        subject_entries.append(new_entry)

    def calculate_gpa():

        try:

            marks_list = []

            for entry in subject_entries:

                value = entry.get().strip()

                if value != "":
                    marks_list.append(float(value))

            if len(marks_list) == 0:
                raise ValueError

            total = sum(marks_list)

            percentage = total / len(marks_list)

            if percentage >= 90:
                gpa = 10
                grade = "A+"

            elif percentage >= 80:
                gpa = 9
                grade = "A"

            elif percentage >= 70:
                gpa = 8
                grade = "B+"

            elif percentage >= 60:
                gpa = 7
                grade = "B"

            elif percentage >= 50:
                gpa = 6
                grade = "C"

            elif percentage >= 40:
                gpa = 5
                grade = "D"

            else:
                gpa = 0
                grade = "Fail"

            result_var.set(
                f"GPA : {gpa} | Grade : {grade}"
            )

            details_box.delete(
                "1.0",
                "end"
            )

            details_box.insert(
                "end",
                f"Total Marks : {total}/500\n"
                f"Percentage : {percentage:.2f}%\n"
                f"GPA : {gpa}\n"
                f"Grade : {grade}"
            )

            current_time = datetime.now().strftime("%H:%M")

            history_box.insert(
                "end",
                f"[{current_time}] GPA {gpa} | {grade}\n"
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

        for entry in subject_entries:
            entry.delete(0, "end")

        result_var.set(
            "GPA Result Will Appear Here"
        )

        details_box.delete("1.0", "end")

        details_box.insert(
            "end",
            "GPA details will appear here..."
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
        text="Calculate GPA",
        command=calculate_gpa
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

    ctk.CTkButton(
        button_frame,
        text="+ Add Subject",
        command=add_subject
    ).grid(
        row=1,
        column=0,
        columnspan=3,
        pady=(10,0)
    )

    subjects_frame.pack(
        fill="x",
        pady=10
    )



    
   


# =========================
# HISTORY
# =========================

    history_title = ctk.CTkLabel(
        right_frame,
        text="GPA History"
    )

    history_title.pack(
        pady=10
    )

    history_box = ctk.CTkTextbox(
        right_frame,
        height=220
    )

    history_box.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    ctk.CTkButton(
        right_frame,
        text="Clear History",
        command=clear_history
    ).pack(
        pady=10
    )    
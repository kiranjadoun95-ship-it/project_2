import customtkinter as ctk

from colors import *
from fonts import *


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def show_finance_tools(parent):

    clear_frame(parent)

    title = ctk.CTkLabel(
        parent,
        text="💰 Finance Tools",
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
    # INPUTS
    # =========================

    ctk.CTkLabel(
        left_frame,
        text="Principal Amount"
    ).pack(pady=(10, 5))

    principal_entry = ctk.CTkEntry(
        left_frame,
        placeholder_text="Enter Principal"
    )
    principal_entry.pack(fill="x", padx=20)

    ctk.CTkLabel(
        left_frame,
        text="Rate of Interest (%)"
    ).pack(pady=(10, 5))

    rate_entry = ctk.CTkEntry(
        left_frame,
        placeholder_text="Enter Rate"
    )
    rate_entry.pack(fill="x", padx=20)

    ctk.CTkLabel(
        left_frame,
        text="Time (Years)"
    ).pack(pady=(10, 5))

    time_entry = ctk.CTkEntry(
        left_frame,
        placeholder_text="Enter Time"
    )
    time_entry.pack(fill="x", padx=20)

    ctk.CTkLabel(
        left_frame,
        text="Loan Amount (For EMI)"
    ).pack(pady=(10, 5))

    loan_entry = ctk.CTkEntry(
        left_frame,
        placeholder_text="Enter Loan Amount"
    )
    loan_entry.pack(fill="x", padx=20)

    # =========================
    # FINANCE TYPE
    # =========================

    finance_type = ctk.StringVar(
        value="Simple Interest"
    )

    ctk.CTkLabel(
        left_frame,
        text="Calculation Type"
    ).pack(pady=(10, 5))

    finance_menu = ctk.CTkOptionMenu(
        left_frame,
        values=[
            "Simple Interest",
            "Compound Interest",
            "EMI Calculator"
        ],
        variable=finance_type
    )
    finance_menu.pack(fill="x", padx=20)

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
    result_label.pack(pady=10)

    # =========================
    # DETAILS BOX
    # =========================

    details_box = ctk.CTkTextbox(
        left_frame,
        height=120
    )
    
    # =========================
    # HISTORY
    # =========================

    ctk.CTkLabel(
        right_frame,
        text="History"
    ).pack(pady=10)

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

    def add_history(text):
        history_box.insert("end", text + "\n")
        history_box.see("end")

    def calculate_finance():

        try:

            rate = float(rate_entry.get())
            time = float(time_entry.get())

            details_box.delete("1.0", "end")

            if finance_type.get() == "Simple Interest":

                principal = float(
                    principal_entry.get()
                )

                interest = (
                    principal * rate * time
                ) / 100

                total = principal + interest

                result_var.set(
                    f"SI = ₹{interest:.2f}"
                )

                details_box.insert(
                    "end",
                    f"=== SIMPLE INTEREST ===\n\n"
                    f"Principal : ₹{principal:.2f}\n"
                    f"Rate : {rate}%\n"
                    f"Time : {time} Years\n\n"
                    f"Interest : ₹{interest:.2f}\n"
                    f"Total Amount : ₹{total:.2f}"
                )

                add_history(
                    f"SI → ₹{interest:.2f}"
                )

            elif finance_type.get() == "Compound Interest":

                principal = float(
                    principal_entry.get()
                )

                amount = principal * (
                    (1 + rate / 100) ** time
                )

                ci = amount - principal

                result_var.set(
                    f"CI = ₹{ci:.2f}"
                )

                details_box.insert(
                    "end",
                    f"=== COMPOUND INTEREST ===\n\n"
                    f"Principal : ₹{principal:.2f}\n"
                    f"Rate : {rate}%\n"
                    f"Time : {time} Years\n\n"
                    f"Compound Interest : ₹{ci:.2f}\n"
                    f"Final Amount : ₹{amount:.2f}"
                )

                add_history(
                    f"CI → ₹{ci:.2f}"
                )

            else:

                loan = float(
                    loan_entry.get()
                )

                monthly_rate = (
                    rate / 12 / 100
                )

                months = int(
                    time * 12
                )

                emi = (
                    loan
                    * monthly_rate
                    * (1 + monthly_rate) ** months
                ) / (
                    (1 + monthly_rate) ** months - 1
                )

                result_var.set(
                    f"EMI = ₹{emi:.2f}"
                )

                details_box.insert(
                    "end",
                    f"=== EMI CALCULATOR ===\n\n"
                    f"Loan Amount : ₹{loan:.2f}\n"
                    f"Rate : {rate}%\n"
                    f"Tenure : {months} Months\n\n"
                    f"Monthly EMI : ₹{emi:.2f}"
                )

                add_history(
                    f"EMI → ₹{emi:.2f}"
                )

        except:
            result_var.set(
                "Invalid Input"
            )

    def clear_all():

        principal_entry.delete(0, "end")
        rate_entry.delete(0, "end")
        time_entry.delete(0, "end")
        loan_entry.delete(0, "end")

        result_var.set(
            "Result will appear here"
        )

        details_box.delete(
            "1.0",
            "end"
        )

    def copy_result():

        parent.clipboard_clear()

        parent.clipboard_append(
            result_var.get()
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
        text="Calculate",
        command=calculate_finance,
        width=130
    ).grid(
        row=0,
        column=0,
        padx=5
    )

    ctk.CTkButton(
        button_frame,
        text="Copy Result",
        command=copy_result,
        width=130
    ).grid(
        row=0,
        column=1,
        padx=5
    )

    ctk.CTkButton(
        button_frame,
        text="Clear",
        command=clear_all,
        width=130
    ).grid(
        row=0,
        column=2,
        padx=5
    )

    ctk.CTkButton(
        right_frame,
        text="Clear History",
        command=clear_history
    ).pack(
        pady=10
    )
    details_box.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=10
    )

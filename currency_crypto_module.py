import customtkinter as ctk

from colors import *
from fonts import *


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def show_currency_crypto_converter(parent):

    clear_frame(parent)

    title = ctk.CTkLabel(
    parent,
    text="💱 Currency & Crypto Converter",
    font=TITLE_FONT
)
    title.pack(pady=10)

    main_frame = ctk.CTkFrame(parent)
    main_frame.pack(fill="both", expand=True, padx=10, pady=10)

    left_frame = ctk.CTkFrame(main_frame)
    left_frame.pack(side="left", fill="both", expand=True, padx=5)

    right_frame = ctk.CTkFrame(main_frame, width=250)
    right_frame.pack(side="right", fill="y", padx=5)

    ctk.CTkLabel(
        left_frame,
        text="Currency Type"
    ).pack(pady=(10, 5))

    type_menu = ctk.CTkOptionMenu(
    left_frame,
    values=["Currency", "Crypto"]
)
    type_menu.pack(pady=5)

    ctk.CTkLabel(
        left_frame,
        text="From"
    ).pack(pady=(10, 5))

    from_menu = ctk.CTkOptionMenu(
        left_frame,
        values=["INR", "USD", "EUR", "GBP"]
    )
    from_menu.pack(pady=5)

    currency_values = [
        "INR",
        "USD",
        "EUR",
        "GBP"
    ]

    crypto_values = [
        "BTC",
        "ETH",
        "USDT",
        "BNB",
        "DOGE"
    ]

    ctk.CTkLabel(
        left_frame,
        text="To"
    ).pack(pady=(10, 5))

    to_menu = ctk.CTkOptionMenu(
        left_frame,
        values=["USD", "INR", "EUR", "GBP"]
    )
    to_menu.pack(pady=5)

    def update_type(choice):

     if choice == "Currency":

        from_menu.configure(
            values=currency_values
        )

        to_menu.configure(
            values=currency_values
        )

        from_menu.set("INR")
        to_menu.set("USD")

     else:

        from_menu.configure(
            values=crypto_values
        )

        to_menu.configure(
            values=crypto_values
        )

        from_menu.set("BTC")
        to_menu.set("USDT")
    type_menu.configure(
        command=update_type
    )    

    amount_entry = ctk.CTkEntry(
        left_frame,
        placeholder_text="Enter Amount"
    )
    amount_entry.pack(fill="x", padx=20, pady=10)

    # =========================
    # RESULT VARIABLE
    # =========================

    result_var = ctk.StringVar(
        value="Result will appear here"
    )

    # =========================
    # DETAILS BOX
    # =========================

    details_box = ctk.CTkTextbox(
        left_frame,
        height=200
    )

    # =========================
    # FUNCTIONS
    # =========================

    def clear_all():

        amount_entry.delete(0, "end")

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

    def convert_currency():

        try:

            amount = float(
                amount_entry.get()
            )

            from_curr = from_menu.get()

            to_curr = to_menu.get()

            rates = {
                "INR": 1,
                "USD": 83.5,
                "EUR": 90,
                "GBP": 105,

                "BTC": 9000000,
                "ETH": 300000,
                "USDT": 83.5,
                "BNB": 50000,
                "DOGE": 15
}
            inr_amount = amount * rates[from_curr]

            result = inr_amount / rates[to_curr]

            result_text = (
                f"{result:.2f} {to_curr}"
            )

            result_var.set(
                result_text
            )

            details_box.delete(
                "1.0",
                "end"
            )

            details_box.insert(
                "end",
                f"From : {from_curr}\n"
                f"To : {to_curr}\n\n"
                f"Amount : {amount}\n\n"
                f"Rate Used :\n"
                f"1 {to_curr} = {rates[to_curr]:.2f} INR\n\n"
                f"Calculation :\n"
                f"{amount} × {rates[from_curr]} ÷ {rates[to_curr]}\n\n"
                f"Result :\n"
                f"{result_text}"
            )

            add_history(
                f"{amount} {from_curr} → {result_text}"
            )

        except:

            result_var.set(
                "Invalid Input"
            )
    def swap_currency():

        from_value = from_menu.get()
        to_value = to_menu.get()

        from_menu.set(to_value)
        to_menu.set(from_value)            

    # =========================
    # BUTTONS
    # =========================

    button_frame = ctk.CTkFrame(left_frame)
    button_frame.pack(pady=10)

    ctk.CTkButton(
        button_frame,
        text="Convert",
        width=140,
        command=convert_currency
    ).grid(row=0, column=0, padx=5, pady=5)

    ctk.CTkButton(
        button_frame,
        text="Swap",
        width=140,
        command=swap_currency
    ).grid(row=0, column=1, padx=5, pady=5)

    button_frame2 = ctk.CTkFrame(
        left_frame,
        fg_color="transparent"
    )
    button_frame2.pack(pady=(5, 10))

    copy_btn = ctk.CTkButton(
        button_frame2,
        text="Copy Result",
        width=120,
        command=copy_result
    )
    copy_btn.pack(side="left", padx=5)

    clear_btn = ctk.CTkButton(
        button_frame2,
        text="Clear",
        width=120,
        command=clear_all
    )
    clear_btn.pack(side="left", padx=5)

    # =========================
    # RESULT LABEL
    # =========================

    result_label = ctk.CTkLabel(
        left_frame,
        textvariable=result_var,
        height=40
    )
    result_label.pack(
        fill="x",
        padx=20,
        pady=10
    )

    # =========================
    # DETAILS BOX
    # =========================

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
    history_title.pack(pady=10)

    history_box = ctk.CTkTextbox(
        right_frame
    )
    history_box.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )
    def add_history(text):

        history_box.insert(
            "end",
            text + "\n"
        )

        history_box.see("end")


    def clear_history():

        history_box.delete(
            "1.0",
            "end"
        )
   
    ctk.CTkButton(
        right_frame,
        text="Clear History",
        command=clear_history
    ).pack(pady=10)    
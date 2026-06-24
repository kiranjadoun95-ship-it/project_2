import customtkinter as ctk
import tkinter as tk
from colors import *

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def show_statistics_calculator(parent):

    clear_frame(parent)

    title = ctk.CTkLabel(
        parent,
        text="📊 Statistics Calculator V1",
        font=("Segoe UI", 20, "bold")
    )
    title.pack(pady=10)

    # =========================
    # MAIN LAYOUT
    # =========================

    main_container = ctk.CTkFrame(parent)
    main_container.pack(fill="both", expand=True, padx=5, pady=5)

    left_frame = ctk.CTkFrame(main_container)
    left_frame.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(5, 2),
        pady=5
    )

    right_frame = ctk.CTkFrame(
        main_container,
        width=220
    )
    right_frame.pack(
        side="right",
        fill="y",
        padx=(2, 5),
        pady=5
    )

    right_frame.pack_propagate(False)

    # =========================
    # INPUT
    # =========================

    input_label = ctk.CTkLabel(
        left_frame,
        text="Enter Numbers (comma separated)",
        font=("Segoe UI", 14, "bold")
    )
    input_label.pack(pady=(10, 5))

    numbers_entry = ctk.CTkEntry(
        left_frame,
        width=380,
        height=35
    )
    numbers_entry.pack(pady=5)

    example_label = ctk.CTkLabel(
    left_frame,
    text="Example: 10,20,30,40,50",
    font=("Segoe UI", 11),
    text_color="lightgray"
)
    example_label.pack(pady=(0, 5))

    result_var = tk.StringVar()
    result_var.set("Result will appear here")

    result_label = ctk.CTkLabel(
    left_frame,
    textvariable=result_var,
    font=("Segoe UI", 18, "bold"),
    text_color="#00FFFF"
)
    result_label.pack(pady=10)

    # =========================
    # DETAILS BOX
    # =========================

    details_title = ctk.CTkLabel(
        left_frame,
        text="Statistics Details",
        font=("Segoe UI", 14, "bold")
    )
    details_title.pack()

    details_box = ctk.CTkTextbox(
        left_frame,
        width=500,
        height=140
    )
    details_box.pack(pady=5)

    # =========================
    # HISTORY
    # =========================

    history_title = ctk.CTkLabel(
        right_frame,
        text="📜 History",
        font=("Segoe UI", 16, "bold")
    )
    history_title.pack(pady=10)

    history_box = ctk.CTkTextbox(
        right_frame,
        width=210,
        height=380
    )
    history_box.pack(padx=5, pady=5)

    def add_history(text):
        history_box.insert("end", text + "\n")
        history_box.see("end")        
        
    def clear_history():

        history_box.delete("1.0", "end")    

# =========================
# BUTTON FRAME
# =========================

    button_frame= ctk.CTkFrame(left_frame)
    button_frame.pack(pady=10)

#===========================
# FUNCTIONS 
#===========================

    def calculate_mean():

        try:
            numbers = [
                float(x.strip())
                for x in numbers_entry.get().split(",")
            ]

            total = sum(numbers)
            count = len(numbers)

            mean = total / count

            result_var.set(f"Mean = {round(mean,4)}")

            details_box.delete("1.0", "end")

            details_box.insert(
                "end",
                f"Numbers:\n{numbers}\n\n"
                f"Count = {count}\n\n"
                f"Sum = {total}\n\n"
                f"Mean = Sum ÷ Count\n"
                f"Mean = {total} ÷ {count}\n\n"
                f"Mean = {round(mean,4)}"
            )

            add_history(f"Mean → {round(mean,4)}")

        except:
            result_var.set("Invalid Input")

    def calculate_median():

        try:

            numbers = sorted(
                [float(x.strip()) for x in numbers_entry.get().split(",")]
            )

            n = len(numbers)

            if n % 2 == 0:
                median = (
                    numbers[n//2 - 1] +
                    numbers[n//2]
                ) / 2
            else:
                median = numbers[n//2]

            result_var.set(f"Median = {round(median,4)}")

            details_box.delete("1.0", "end")

            details_box.insert(
                "end",
                f"Sorted Numbers:\n{numbers}\n\n"
                f"Count = {n}\n\n"
                f"Median = {round(median,4)}"
            )

            add_history(f"Median → {round(median,4)}")
        except:
         result_var.set("Invalid Input")

    def calculate_mode():

        try:

            numbers = [
                float(x.strip())
                for x in numbers_entry.get().split(",")
            ]

            frequency = {}

            for num in numbers:
                frequency[num] = frequency.get(num, 0) + 1

            max_count = max(frequency.values())

            modes = [
                num for num, count in frequency.items()
                if count == max_count
            ]

            if len(modes) == len(frequency):

                result_var.set("No Mode")

                details_box.delete("1.0", "end")

                details_box.insert(
                    "end",
                    f"Numbers:\n{numbers}\n\nNo Mode Found"
                )

                add_history("Mode → No Mode")

            else:

                mode_value = ", ".join(map(str, modes))

                result_var.set(f"Mode = {mode_value}")

                details_box.delete("1.0", "end")

                details_box.insert(
                    "end",
                    f"Numbers:\n{numbers}\n\n"
                    f"Frequency:\n{frequency}\n\n"
                    f"Mode = {mode_value}"
                )

                add_history(f"Mode → {mode_value}")

        except:
            result_var.set("Invalid Input")

    def calculate_range():

        try:

            numbers = [
              float(x.strip())
              for x in numbers_entry.get().split(",")
            ]

            highest = max(numbers)
            lowest = min(numbers)

            range_value = highest - lowest

            result_var.set(f"Range = {round(range_value, 4)}")

            details_box.delete("1.0", "end")

            details_box.insert(
                "end",
                 f"Numbers:\n{numbers}\n\n"
                 f"Maximum = {highest}\n"
                 f"Minimum = {lowest}\n\n"
                 f"Range = Maximum - Minimum\n"
                 f"Range = {highest} - {lowest}\n\n"
                 f"Range = {round(range_value, 4)}"
            )

            add_history(f"Range → {round(range_value, 4)}")
        except:
         result_var.set("Invalid Input")

    def calculate_variance():

        try:
            numbers = [
              float(x.strip())
              for x in numbers_entry.get().split(",")
        ]

            mean = sum(numbers) / len(numbers)

            variance = sum(
            (x - mean) ** 2 for x in numbers
        ) / len(numbers)

            result_var.set(
            f"Variance = {round(variance,4)}"
        )

            details_box.delete("1.0", "end")

            details_box.insert(
             "end",
             f"Numbers:\n{numbers}\n\n"
             f"Mean = {round(mean,4)}\n\n"
             f"Variance = {round(variance,4)}"
        )

            add_history(
             f"Variance → {round(variance,4)}"
        )
        except:
         result_var.set("Invalid Input")

    def calculate_std_dev():

        try:
            numbers = [
             float(x.strip())
             for x in numbers_entry.get().split(",")
        ]

            mean = sum(numbers) / len(numbers)

            variance = sum(
            (x - mean) ** 2 for x in numbers
        ) / len(numbers)

            std_dev = variance ** 0.5

            result_var.set(
             f"Std Dev = {round(std_dev,4)}"
        )

            details_box.delete("1.0", "end")

            details_box.insert(
             "end",
             f"Numbers:\n{numbers}\n\n"
             f"Mean = {round(mean,4)}\n\n"
             f"Variance = {round(variance,4)}\n\n"
             f"Standard Deviation = {round(std_dev,4)}"
        )

            add_history(
             f"Std Dev → {round(std_dev,4)}"
        )
        except:
         result_var.set("Invalid Input")

    def copy_result():

         parent.clipboard_clear()
         parent.clipboard_append(result_var.get())
         parent.update()              

    def clear_all():

        numbers_entry.delete(0, "end")

        result_var.set("Result will appear here")

        details_box.delete("1.0", "end")
    def clear_history():
        history_box.delete("1.0", "end")    


#==========================
# BUTTONS
# =========================            

    ctk.CTkButton(
        button_frame,
        text="Mean",
        fg_color="#00BFFF",
        hover_color="#009ACD",
        command= calculate_mean,
        width=140
    ).grid(row=0, column=0, padx=5, pady=5)

    ctk.CTkButton(
        button_frame,
        text="Median",
        fg_color="#00CED1",
        hover_color="#008B8B",
        command= calculate_median,
        width=140
    ).grid(row=0, column=1, padx=5, pady=5)

    ctk.CTkButton(
        button_frame,
        text="Mode",
        fg_color="#32CD32",
        hover_color="#228B22",
        command= calculate_mode,
        width=140
    ).grid(row=1, column=0, padx=5, pady=5)

    ctk.CTkButton(
        button_frame,
        text="Range",
        fg_color="#BA55D3",
        hover_color="#9932CC",
        command=calculate_range,
        width=140
    ).grid(row=1, column=1, padx=5, pady=5)

    ctk.CTkButton(
        button_frame,
        text="Variance",
        fg_color="#FF8C00",
        hover_color="#FF7F50",
        command=calculate_variance,
        width=140
    ).grid(row=2, column=0, padx=5, pady=5)

    ctk.CTkButton(
        button_frame,
        text="Std Dev",
        fg_color="#FF1493",
        hover_color="#C71585",
        command=calculate_std_dev,
        width=140
    ).grid(row=2, column=1, padx=5, pady=5)

    ctk.CTkButton(
        button_frame,
        text="Copy Result",
        fg_color="#1E90FF",
        hover_color="#1874CD",
        command=copy_result,
        width=140
    ).grid(row=3, column=0, padx=5, pady=5)

    ctk.CTkButton(
        button_frame,
        text="Clear",
        fg_color="red",
        command=clear_all,
        width=140
    ).grid(row=3, column=1, padx=5, pady=5)

    ctk.CTkButton(
    right_frame,
    text="Clear History",
    fg_color="red",
    command=clear_history
).pack(pady=5)
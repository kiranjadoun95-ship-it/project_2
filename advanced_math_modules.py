import customtkinter as ctk
import math
import tkinter as tk
from colors import *

def clear_frame(frame):
 for widget in frame.winfo_children():
  widget.destroy()

def show_algebra_calculator(parent):

    clear_frame(parent)

    history = []

    title = ctk.CTkLabel(
        parent,
        text="📘 Algebra Calculator V3",
        font=("Segoe UI", 20, "bold")
    )
    title.pack(pady=10)

        # =========================
    # COMPACT MAIN LAYOUT
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
        width=180
    )
    right_frame.pack(
        side="right",
        fill="y",
        padx=(2, 5),
        pady=5
    )

    right_frame.pack_propagate(False)
    input_label = ctk.CTkLabel(
                left_frame,
                text="Enter Expression / Equation",
                font=("Segoe UI", 14, "bold")
            )
    input_label.pack(pady=(10, 5))

    equation_entry = ctk.CTkEntry(
            left_frame,
            width=380,
            height=35
        )
    equation_entry.pack(pady=5)

    result_var = tk.StringVar()
    result_var.set("Result will appear here")

    result_label = ctk.CTkLabel(
            left_frame,
            textvariable=result_var,
            font=("Segoe UI", 16, "bold")
        )
    result_label.pack(pady=10)
            # ==========================
            # STEPS BOX
            # ==========================

    steps_title = ctk.CTkLabel(
            left_frame,
            text="Solution Steps",
            font=("Segoe UI", 14, "bold")
        )
    steps_title.pack()

    steps_box = ctk.CTkTextbox(
            left_frame,
            width=500,
            height=180
        )
    steps_box.pack(pady=5)

    # ==========================
    # HISTORY
    # ==========================

    history_title = ctk.CTkLabel(
        right_frame,
        text="📜 History",
        font=("Segoe UI", 16, "bold")
    )
    history_title.pack(pady=10)
    history_box = ctk.CTkTextbox(
    right_frame,
    width=180,
    height=280
    )
    history_box.pack(padx=5, pady=5)

    

    def add_history(text):
        history_box.insert("end", text + "\n")
        history_box.see("end")

    def clear_history():
        history_box.delete("1.0", "end")
    ctk.CTkButton(
    right_frame,
    text="Clear History",
    fg_color="red",
    command=clear_history
).pack(pady=5)    

    def copy_result():
        parent.clipboard_clear()
        parent.clipboard_append(result_var.get())

    # ==========================
        # BUTTON FRAME
        # ==========================

        button_frame = ctk.CTkFrame(left_frame)
        button_frame.pack(pady=10)

    # ==========================
        # SOLVERS
        # ==========================

    def solve_linear():
        try:
            eq = equation_entry.get().replace(" ", "")

            left, right = eq.split("=")

            if "x" not in left:
                result_var.set("Variable x missing")
                return

            coeff = ""
            constant = ""

            pos = left.find("x")

            coeff = left[:pos]

            if coeff == "":
                a = 1
            elif coeff == "-":
                a = -1
            else:
                a = float(coeff)

            remaining = left[pos+1:]

            if remaining == "":
                b = 0
            else:
                b = float(remaining)

            c = float(right)

            x = (c - b) / a

            result_var.set(f"x = {round(x,4)}")

            steps_box.delete("1.0", "end")

            steps_box.insert(
                "end",
                f"Equation: {eq}\n\n"
                f"{a}x + ({b}) = {c}\n\n"
                f"{a}x = {c} - ({b})\n\n"
                f"{a}x = {c-b}\n\n"
                f"x = {(c-b)}/{a}\n\n"
                f"x = {x}"
            )

            add_history(f"Linear → {eq} = x:{round(x,4)}")

        except:
            result_var.set("Example: 2x+5=15")


    def solve_quadratic():

        try:
            values = equation_entry.get().split(",")

            if len(values) != 3:
                    result_var.set("Enter: a,b,c")
                    return

            a = float(values[0])
            b = float(values[1])
            c = float(values[2])

            d = (b ** 2) - (4 * a * c)

            steps_box.delete("1.0", "end")

            steps_box.insert(
                    "end",
                    f"Given:\n"
                    f"a = {a}\n"
                    f"b = {b}\n"
                    f"c = {c}\n\n"
                    f"Discriminant:\n"
                    f"D = b² - 4ac\n"
                    f"D = ({b})² - 4({a})({c})\n"
                    f"D = {d}\n\n"
                )

            if d < 0:
                    result_var.set("No Real Roots")
                    steps_box.insert(
                        "end",
                        "D < 0\nNo Real Roots"
                    )
                    add_history(f"Quadratic: {a},{b},{c} -> No Real Roots")
                    return

            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)

            result_var.set(
                    f"x₁ = {round(x1,4)}   x₂ = {round(x2,4)}"
                )

            steps_box.insert(
                    "end",
                    f"x₁ = (-b + √D)/(2a)\n"
                    f"x₁ = {x1}\n\n"
                    f"x₂ = (-b - √D)/(2a)\n"
                    f"x₂ = {x2}"
                )

            add_history(
                    f"Quadratic: {a},{b},{c} -> "
                    f"{round(x1,2)}, {round(x2,2)}"
                )

        except Exception:
            result_var.set("Example: 1,-5,6")
    
    def polynomial_value():

        try:
            exp, xval = equation_entry.get().split(",")

            xval = float(xval)

            result = eval(exp.replace("x", str(xval)))

            result_var.set(f"Result = {result}")

            steps_box.delete("1.0", "end")
            steps_box.insert(
                "end",
                f"Expression = {exp}\n"
                f"x = {xval}\n\n"
                f"Substitute x:\n"
                f"{exp.replace('x', str(xval))}\n\n"
                f"Result = {result}"
            )

            add_history(
                f"Polynomial: {exp}, x={xval} -> {result}"
            )

        except Exception:
            result_var.set("Example: x**2+5*x+6,2")


    def factorize_quadratic():

        try:
            values = equation_entry.get().split(",")

            if len(values) != 3:
                result_var.set("Enter: a,b,c")
                return

            a = int(values[0])
            b = int(values[1])
            c = int(values[2])

            found = False

            for i in range(-100, 101):
                for j in range(-100, 101):

                    if i * j == a * c and i + j == b:

                        steps_box.delete("1.0", "end")
                        steps_box.insert(
                            "end",
                            f"a = {a}\n"
                            f"b = {b}\n"
                            f"c = {c}\n\n"
                            f"Need two numbers:\n"
                            f"Product = {a*c}\n"
                            f"Sum = {b}\n\n"
                            f"Numbers found:\n"
                            f"{i} and {j}"
                        )

                        result_var.set(
                            f"Factors Found: {i}, {j}"
                        )

                        add_history(
                            f"Factorize: {a},{b},{c}"
                        )

                        found = True
                        break

                if found:
                    break

            if not found:
                result_var.set("Factors not found")

        except Exception:
            result_var.set("Example: 1,-5,6")
            # ==========================
    # BUTTON FRAME
    # ==========================

    button_frame = ctk.CTkFrame(left_frame)
    button_frame.pack(pady=10)        

                # ============================
    # BUTTONS
    # ============================

    ctk.CTkButton(
    button_frame,
    text="Linear Solver",
    fg_color="#00BFFF",
    hover_color="#009ACD",
    command=solve_linear,
    width=140
).grid(row=0, column=0, padx=5, pady=5)

    ctk.CTkButton(
    button_frame,
    text="Quadratic",
    fg_color="#00CED1",
    hover_color="#008B8B",
    command=solve_quadratic,
    width=140
).grid(row=0, column=1, padx=5, pady=5)

    ctk.CTkButton(
    button_frame,
    text="Polynomial",
    fg_color="#32CD32",
    hover_color="#228B22",
    command=polynomial_value,
    width=140
).grid(row=1, column=0, padx=5, pady=5)
    
    ctk.CTkButton(
    button_frame,
    text="Factorize",
    fg_color="#BA55D3",
    hover_color="#9932CC",
    command=factorize_quadratic,
    width=140
).grid(row=1, column=1, padx=5, pady=5)
    
    ctk.CTkButton(
        button_frame,
        text="Copy Result",
        fg_color="#FF8C00",
        hover_color="#FF7F50",
        command=copy_result,
        width=140
    ).grid(row=2, column=0, padx=5, pady=5)

    ctk.CTkButton(
        button_frame,
        text="Clear",
        fg_color="red",
        hover_color="#B22222",
        command=lambda: (
            equation_entry.delete(0, "end"),
            result_var.set("Result will appear here"),
            steps_box.delete("1.0", "end")
        ),
        width=140
    ).grid(row=2, column=1, padx=5, pady=5)

    
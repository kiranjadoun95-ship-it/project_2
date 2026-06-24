import customtkinter as ctk
from tkinter import messagebox
from colors import *
from fonts import *
import numpy as np

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def show_matrix_calculator(parent):

    clear_frame(parent)

    title = ctk.CTkLabel(
        parent,
        text="📐 Matrix Calculator",
        font=TITLE_FONT,
        text_color=TEXT_WHITE
    )
    title.pack(pady=15)

    main_frame = ctk.CTkFrame(
        parent,
        fg_color=BG_COLOR
    )
    main_frame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=10
    )
    main_container = ctk.CTkFrame(main_frame)
    main_container.pack(
        fill="both",
        expand=True
    )

    left_panel = ctk.CTkFrame(main_container)
    left_panel.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(0,10)
    )

    right_panel = ctk.CTkFrame(
        main_container,
        width=220
    )

    right_panel.pack(
        side="right",
        fill="y"
    )

    right_panel.pack_propagate(False)

    right_panel.pack_propagate(False)

    matrix_size = ctk.StringVar(value="2x2")

    
    matrix_frame = ctk.CTkFrame(main_frame)
    matrix_frame.pack(
         in_=left_panel,pady=15
    )

    entries_a = []
    entries_b = []

    def change_matrix_size(choice):

        create_matrix_entries(
        int(choice[0])
        )

    def create_matrix_entries(size):

        for widget in left_frame.winfo_children():
            widget.destroy()

        for widget in right_frame.winfo_children():
            widget.destroy()

        entries_a.clear()
        entries_b.clear()

        ctk.CTkLabel(
            left_frame,
            text="Matrix A",
            font=BUTTON_FONT
        ).pack(pady=5)

        for i in range(size):

            row = []

            row_frame = ctk.CTkFrame(left_frame)
            row_frame.pack()

            for j in range(size):

                e = ctk.CTkEntry(
                    row_frame,
                    width=60
                )

                e.pack(side="left", padx=3, pady=3)

                row.append(e)

            entries_a.append(row)

        ctk.CTkLabel(
            right_frame,
            text="Matrix B",
            font=BUTTON_FONT
        ).pack(pady=5)

        for i in range(size):

            row = []

            row_frame = ctk.CTkFrame(right_frame)
            row_frame.pack()

            for j in range(size):

                e = ctk.CTkEntry(
                    row_frame,
                    width=60
                )

                e.pack(side="left", padx=3, pady=3)

                row.append(e)

            entries_b.append(row)

    left_frame = ctk.CTkFrame(
        matrix_frame,
        fg_color=SIDEBAR_COLOR
    )
    left_frame.pack(
        side="left",
        padx=20,
        pady=10
    )

    right_frame = ctk.CTkFrame(
        matrix_frame,
        fg_color=SIDEBAR_COLOR
    )
    right_frame.pack(
        side="left",
        padx=20,
        pady=10
    )

    
    create_matrix_entries(2)

    size_menu = ctk.CTkOptionMenu(
    left_panel,
    values=["2x2", "3x3"],
    variable=matrix_size,
    command=change_matrix_size
)

    size_menu.pack(pady=5)

    result_box = ctk.CTkTextbox(
            main_frame,
            height=90,
            font=("Consolas",16,"bold")
        )
    result_box.pack(
            in_=left_panel,
            fill="x",
            padx=10,
            pady=10
        )
    history_frame = ctk.CTkFrame(
        right_panel,
        fg_color=SIDEBAR_COLOR
        )
    history_frame.pack(
            fill="both",
            expand=True,
            padx=5,
            pady=5
        )

    ctk.CTkLabel(
            history_frame,
            text="History",
            font=BUTTON_FONT
        ).pack(pady=5)

    history_box = ctk.CTkTextbox(
            history_frame,
            height=120
        )

    history_box.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )
    def clear_history():
        history_box.delete("1.0", "end")

    ctk.CTkButton(
        history_frame,
        text="Clear History",
        fg_color="#E74C3C",
        hover_color="#C0392B",
        command=clear_history
    ).pack(pady=5)

    def get_matrix(entries):
                        return [
                            [float(cell.get()) for cell in row]
                            for row in entries
                        ]
    
    def get_size():
        return len(entries_a)

    def show_result(matrix):

            result_box.delete("1.0", "end")

            text = ""

            for row in matrix:
                text += "  ".join(str(x) for x in row) + "\n"

            result_box.insert("end", text)

            history_box.insert(
                "end",
                text + "\n----------------\n"
            )
    def add_history(text):

                history_box.insert(
                    "end",
                    text + "\n"
                )

                history_box.see("end")        

    def add_matrix():

                try:

                    A = get_matrix(entries_a)
                    B = get_matrix(entries_b)

                    size = get_size()

                    result = [
                        [
                             A[i][j] + B[i][j]
                             for j in range(size)
                        ]
                        for i in range(size)
                    ]

                    show_result(result)
                    add_history("A+B")

                except:
                    messagebox.showerror(
                        "Error",
                        "Invalid Input"
                    )

    def subtract_matrix():

            try:

                A = get_matrix(entries_a)
                B = get_matrix(entries_b)

                size = get_size()

                result = [
                    [
                         A[i][j] - B[i][j]
                         for j in range(size)
                    ]
                    for i in range(size)
                ]

                show_result(result)
                add_history("A-B")

            except:
                messagebox.showerror(
                    "Error",
                    "Invalid Input"
                )
    def multiply_matrix():

        try:

            A = np.array(get_matrix(entries_a))
            B = np.array(get_matrix(entries_b))

            result = np.matmul(A, B)

            show_result(result.tolist())

            add_history("A × B")

        except:

            messagebox.showerror(
                "Error",
                "Invalid Input"
            )
    def transpose_matrix():
            
            try:

                    A = get_matrix(entries_a)

                    size = get_size()

                    result = [
                        [A[j][i] for j in range(size)]
                        for i in range(size)
                    ]

                    show_result(result)
                    add_history("Transpose A")

            except:

                    messagebox.showerror(
                        "Error",
                        "Invalid Input"
                    )


    def determinant_matrix():

        try:

            A = np.array(get_matrix(entries_a))

            det = round(np.linalg.det(A), 2)

            result_box.delete("1.0", "end")

            result_box.insert(
                "end",
                f"Determinant A = {det}"
            )

            add_history(f"Det A = {det}")

        except:

            messagebox.showerror(
                "Error",
                "Invalid Input"
            )

    def inverse_matrix():

        try:

            A = np.array(get_matrix(entries_a))

            inv = np.linalg.inv(A)

            result = np.round(inv, 2)

            show_result(result.tolist())

            add_history("Inverse A")

        except:

            messagebox.showerror(
                "Error",
                "Inverse does not exist"
            )
    def determinant_b():

        try:

            B = np.array(get_matrix(entries_b))

            det = round(np.linalg.det(B), 2)

            result_box.delete("1.0", "end")

            result_box.insert(
                "end",
                f"Determinant B = {det}"
            )

            add_history(f"Det B = {det}")

        except:

            messagebox.showerror(
                "Error",
                "Invalid Input"
            )

    def inverse_b():

        try:

            B = np.array(get_matrix(entries_b))

            inv = np.linalg.inv(B)

            result = np.round(inv, 2)

            show_result(result.tolist())

            add_history("Inverse B")

        except:

            messagebox.showerror(
                "Error",
                "Inverse does not exist"
            )

    def identity_matrix():

        size = get_size()

        result = np.identity(size)

        show_result(result.tolist())

        add_history(f"Identity {size}x{size}")

    def clear_all():

                    for row in entries_a:
                        for cell in row:
                            cell.delete(0, "end")

                    for row in entries_b:
                        for cell in row:
                            cell.delete(0, "end")

                    result_box.delete("1.0", "end")
                    

    def copy_result():

        text = result_box.get("1.0", "end").strip()

        if text:
            parent.clipboard_clear()
            parent.clipboard_append(text)

            messagebox.showinfo(
                "Copied",
                "Result copied successfully"
            )                   

    button_frame = ctk.CTkFrame(main_frame)
    button_frame.pack(
            in_=left_panel,
            pady=10
        )    

    ctk.CTkButton(
            button_frame,
            text="A + B",
            width=125,
            fg_color=BUTTON_GREEN,
            command=add_matrix
        ).grid(row=0,column=0,padx=5,pady=5)

    ctk.CTkButton(
            button_frame,
            text="A - B",
            width=125,
            fg_color=BUTTON_BLUE,
            command=subtract_matrix
        ).grid(row=0,column=1, padx=5,pady=5)

    ctk.CTkButton(
            button_frame,
            text="A × B",
            width=125,
            fg_color=BUTTON_PURPLE,
            command=multiply_matrix
        ).grid(row=0, column=2, padx=5,pady=5)

    ctk.CTkButton(
            button_frame,
            text="Transpose A",
            width=125,
            fg_color=BUTTON_BLUE,
            command=transpose_matrix
        ).grid(row=1,column=0, padx=5,pady=5)

    ctk.CTkButton(
            button_frame,
            text="Det A",
            width=125,
            fg_color=BUTTON_GREEN,
            command=determinant_matrix
        ).grid(row=1,column=1, padx=5,pady=5)

    ctk.CTkButton(
            button_frame,
            text="Inverse A",
            width=125,
            fg_color=BUTTON_PURPLE,
            command=inverse_matrix
        ).grid(row=1,column=2, padx=5,pady=5)

    ctk.CTkButton(
            button_frame,
            text="Clear",
            width= 125,
            fg_color="#E74C3C",
            command=clear_all
        ).grid(row=3,column=1, padx=5,pady=5)

    ctk.CTkButton(
        button_frame,
        text="Copy Result",
        width=125,
        fg_color="#F39C12",
        command=copy_result
    ).grid(row=3, column=0, padx=5, pady=5)
        
    ctk.CTkButton(
        button_frame,
        text="Det B",
        width=125,
        fg_color=BUTTON_GREEN,
        command=determinant_b
    ).grid(row=2, column=0, padx=5, pady=5)
        
    ctk.CTkButton(
        button_frame,
        text="Inverse B",
        width=125,
        fg_color=BUTTON_PURPLE,
        command=inverse_b
    ).grid(row=2, column=1, padx=5, pady=5)
        
    ctk.CTkButton(
        button_frame,
        text="Identity",
        width= 125,
        fg_color=BUTTON_BLUE,
        command=identity_matrix
    ).grid(row=2, column=2, padx=5, pady=5)
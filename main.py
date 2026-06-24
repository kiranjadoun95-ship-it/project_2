import customtkinter as ctk
from math_modules import show_standard_calculator
from math_modules import show_scientific_calculator
from math_modules import show_trigonometry_calculator
from advanced_math_modules import show_algebra_calculator
from matrix_modules import show_matrix_calculator
from statistics_modules import show_statistics_calculator
from currency_crypto_module import show_currency_crypto_converter
from finance_modules import show_finance_tools
from utility_modules import show_unit_converter
from health_modules import show_health_bmi
from date_time_modules import show_date_time_calculator
from gpa_modules import show_gpa_calculator
from programmer_modules import show_programmer_calculator
from graph_modules import show_graph_plotter
from colors import *
from fonts import *

# ----------------------------
# APP SETTINGS
# ----------------------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.title("CalcMaster Pro")
app.geometry("1150x680")
app.minsize(1000, 600)

# ----------------------------
# SCROLLABLE SIDEBAR
# ----------------------------

sidebar = ctk.CTkScrollableFrame(
    app,
    width=230,
    fg_color=SIDEBAR_COLOR,
    corner_radius=0
)

sidebar.pack(side="left", fill="y")

# ----------------------------
# TITLE
# ----------------------------

title_label = ctk.CTkLabel(
    sidebar,
    text="CalcMaster Pro",
    font=TITLE_FONT,
    text_color=TEXT_WHITE
)

title_label.pack(pady=(15, 20))

# ----------------------------
# MAIN AREA
# ----------------------------

main_area = ctk.CTkFrame(
    app,
    fg_color=BG_COLOR
)

main_area.pack(
    side="right",
    fill="both",
    expand=True
)


# ----------------------------
# DASHBOARD FUNCTION
# ----------------------------

def show_dashboard():

    for widget in main_area.winfo_children():
        widget.destroy()

    header_frame = ctk.CTkFrame(
    main_area,
    height=120,
    fg_color=CARD_COLOR,
    corner_radius=20
)

    header_frame.pack(
        fill="x",
        padx=20,
        pady=(20,10)
    )

    title_label = ctk.CTkLabel(
        header_frame,
        text="🚀 CalcMaster Pro Dashboard",
        font=("Segoe UI", 28, "bold")
    )

    title_label.pack(pady=(15,5))

    info_label = ctk.CTkLabel(
        header_frame,
        text="14 modules, All system ready",
        font=("Segoe UI", 14)
    )

    info_label.pack()

    # =========================
    # DASHBOARD CARDS
    # =========================

    dashboard_frame = ctk.CTkScrollableFrame(
        main_area,
        fg_color=BG_COLOR
    )

    dashboard_frame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=(0,10)
    )

    cards = [

        ("🧮 Standard", "Basic Calculator", "#2E8B57", lambda: show_standard_calculator(main_area)),
        ("🔬 Scientific", "Advanced Functions", "#1E90FF", lambda: show_scientific_calculator(main_area)),
        ("📐 Trigonometry", "Sin Cos Tan", "#FF8C00", lambda: show_trigonometry_calculator(main_area)),

        ("📘 Algebra", "Equation Solver", "#6A5ACD", lambda: show_algebra_calculator(main_area)),
        ("🔢 Matrix", "Matrix Operations", "#DC143C", lambda: show_matrix_calculator(main_area)),
        ("📊 Statistics", "Data Analysis", "#4682B4", lambda: show_statistics_calculator(main_area)),

        ("💱 Currency", "Forex & Crypto", "#32CD32", lambda: show_currency_crypto_converter(main_area)),
        ("💰 Finance", "EMI SIP FD", "#20B2AA", lambda: show_finance_tools(main_area)),
        ("📏 Converter", "Unit Conversion", "#DAA520", lambda: show_unit_converter(main_area)),

        ("❤️ Health", "BMI & Health", "#3CB371", lambda: show_health_bmi(main_area)),
        ("📅 Date & Time", "Age & Time Tools", "#9370DB", lambda: show_date_time_calculator(main_area)),
        ("🎓 GPA", "CGPA Calculator", "#4169E1", lambda: show_gpa_calculator(main_area)),

        ("💻 Programmer", "Binary Hex Oct", "#228B22", lambda: show_programmer_calculator(main_area)),
        ("📈 Graph Plotter", "Function Graphs", "#483D8B", lambda: show_graph_plotter(main_area))

    ]

    row = 0
    col = 0

    for title, subtitle, color, command in cards:

        card_frame = ctk.CTkFrame(
            dashboard_frame,
            width=280,
            height=180,
            fg_color=color,
            corner_radius=20,
            border_width=2
        )

        card_frame.grid(
            row=row,
            column=col,
            padx=15,
            pady=15,
            sticky="nsew"
        )

        card_frame.grid_propagate(False)

        title_lbl = ctk.CTkLabel(
            card_frame,
            text=title,
            font=("Segoe UI", 22, "bold")
        )

        title_lbl.pack(pady=(20,5))

        sub_lbl = ctk.CTkLabel(
            card_frame,
            text=subtitle,
            font=("Segoe UI", 12)
        )

        sub_lbl.pack()

        
            
        open_btn = ctk.CTkButton(
            card_frame,
            text="OPEN",
            width=150,
            command=command,
            hover_color="#87CEFA"
        )

        open_btn.pack(pady=20)

        col += 1

        if col > 2:
            col = 0
            row += 1

    for i in range(3):
        dashboard_frame.grid_columnconfigure(i, weight=1)
# ----------------------------
# MENU BUTTONS
# ----------------------------

menu_items = [
    "Dashboard",
    "Standard",
    "Scientific",
    "Trigonometry",
    "Algebra",
    "Matrix",
    "Statistics",
    "Currency & Crypto",
    "Finance Tools",
    "Unit Converter",
    "Health & BMI",
    "Date & Time",
    "GPA Calculator",
    "Programmer calculator",
    "Graph Plotter"
]

for item in menu_items:

    if item == "Dashboard":

        btn = ctk.CTkButton(
            sidebar,
            text=item,
            width=190,
            height=32,
            font=("Segoe UI", 13, "bold"),
            fg_color=CARD_COLOR,
            hover_color=BUTTON_BLUE,
            corner_radius=8,
            command=show_dashboard
        )

    elif item == "Standard":

        btn = ctk.CTkButton(
            sidebar,
            text=item,
            width=190,
            height=32,
            font=("Segoe UI", 13, "bold"),
            fg_color=CARD_COLOR,
            hover_color=BUTTON_BLUE,
            corner_radius=8,
            command=lambda: show_standard_calculator(main_area)
        )
    elif item == "Scientific":
     btn = ctk.CTkButton(
        sidebar,
        text=item,
        width=190,
        height=32,
        font=("Segoe UI", 13, "bold"),
        fg_color=CARD_COLOR,
        hover_color=BUTTON_BLUE,
        corner_radius=8,
        command=lambda: show_scientific_calculator(main_area)
    )
    elif item == "Trigonometry":
     btn = ctk.CTkButton(
        sidebar,
        text=item,
        width=190,
        height=32,
        font=("Segoe UI", 13, "bold"),
        fg_color=CARD_COLOR,
        hover_color=BUTTON_BLUE,
        corner_radius=8,
        command=lambda: show_trigonometry_calculator(main_area)
    )
    elif item == "Algebra":
        btn = ctk.CTkButton(
            sidebar,
            text=item,
            width=190,
            height=32,
            font=("Segoe UI", 13, "bold"),
            fg_color=CARD_COLOR,
            hover_color=BUTTON_BLUE,
            corner_radius=8,
            command=lambda: show_algebra_calculator(main_area)
        )
    elif item == "Matrix":
     btn = ctk.CTkButton(
        sidebar,
        text=item,
        width=190,
        height=32,
        font=("Segoe UI", 13, "bold"),
        fg_color=CARD_COLOR,
        hover_color=BUTTON_BLUE,
        corner_radius=8,
        command=lambda: show_matrix_calculator(main_area)
    )
    elif item == "Statistics":
     btn = ctk.CTkButton(
        sidebar,
        text=item,
        width=190,
        height=32,
        font=("Segoe UI", 13, "bold"),
        fg_color=CARD_COLOR,
        hover_color=BUTTON_BLUE,
        corner_radius=8,
        command=lambda: show_statistics_calculator(main_area)
    )
    elif item == "Currency & Crypto":
     btn = ctk.CTkButton(
        sidebar,
        text=item,
        width=190,
        height=32,
        font=("Segoe UI", 13, "bold"),
        fg_color=CARD_COLOR,
        hover_color=BUTTON_BLUE,
        corner_radius=8,
        command=lambda: show_currency_crypto_converter(main_area)
    )
    elif item == "Finance Tools":
     btn = ctk.CTkButton(
        sidebar,
        text=item,
        width=190,
        height=32,
        font=("Segoe UI", 13, "bold"),
        fg_color=CARD_COLOR,
        hover_color=BUTTON_BLUE,
        corner_radius=8,
        command=lambda: show_finance_tools(main_area)
    )
    elif item == "Unit Converter":
     btn = ctk.CTkButton(
        sidebar,
        text=item,
        width=190,
        height=32,
        font=("Segoe UI", 13, "bold"),
        fg_color=CARD_COLOR,
        hover_color=BUTTON_BLUE,
        corner_radius=8,
        command=lambda: show_unit_converter(main_area)
    )
    elif item == "Health & BMI":

     btn = ctk.CTkButton(
        sidebar,
        text=item,
        width=190,
        height=32,
        font=("Segoe UI", 13, "bold"),
        fg_color=CARD_COLOR,
        hover_color=BUTTON_BLUE,
        corner_radius=8,
        command=lambda: show_health_bmi(main_area)
    )
    elif item == "Date & Time":

     btn = ctk.CTkButton(

        sidebar,

        text=item,

        width=190,

        height=32,

        font=("Segoe UI", 13, "bold"),

        fg_color=CARD_COLOR,

        hover_color=BUTTON_BLUE,

        corner_radius=8,

        command=lambda: show_date_time_calculator(main_area)

    )
    elif item == "GPA Calculator":

     btn = ctk.CTkButton(
        sidebar,
        text=item,
        width=190,
        height=32,
        font=("Segoe UI", 13, "bold"),
        fg_color=CARD_COLOR,
        hover_color=BUTTON_BLUE,
        corner_radius=8,
        command=lambda: show_gpa_calculator(main_area)
    )
    elif item == "Programmer calculator":

     btn = ctk.CTkButton(
        sidebar,
        text=item,
        width=190,
        height=32,
        font=("Segoe UI", 13, "bold"),
        fg_color=CARD_COLOR,
        hover_color=BUTTON_BLUE,
        corner_radius=8,
        command=lambda: show_programmer_calculator(main_area)
    )
    elif item == "Graph Plotter":

     btn = ctk.CTkButton(
        sidebar,
        text=item,
        width=190,
        height=32,
        font=("Segoe UI", 13, "bold"),
        fg_color=CARD_COLOR,
        hover_color=BUTTON_BLUE,
        corner_radius=8,
        command=lambda: show_graph_plotter(main_area)
    )                                                   
    

    else:
     btn = ctk.CTkButton(
        sidebar,
        text=item,
        width=190,
        height=32,
        font=("Segoe UI", 13, "bold"),
        fg_color=CARD_COLOR,
        hover_color=BUTTON_BLUE,
        corner_radius=8
    )
    btn.pack(pady=3,padx=8)

show_dashboard()
app.mainloop()


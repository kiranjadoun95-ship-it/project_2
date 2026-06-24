import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk


from colors import *
from fonts import *


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def show_graph_plotter(parent):

    clear_frame(parent)

    title = ctk.CTkLabel(
        parent,
        text="📈 Graph Plotter",
        font=TITLE_FONT
    )
    title.pack(pady=10)

    main_frame = ctk.CTkFrame(
        parent,
        fg_color="transparent"
    )

    main_frame.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    control_frame = ctk.CTkFrame(
        main_frame,
        fg_color=CARD_COLOR,
        width=320
    )

    control_frame.pack(
        side="left",
        fill="y",
        padx=(0, 10)
    )

    control_frame.pack_propagate(False)

    graph_frame = ctk.CTkFrame(
        main_frame,
        fg_color=CARD_COLOR
    )

    graph_frame.pack(
        side="right",
        fill="both",
        expand=True
    )

    ctk.CTkLabel(
        control_frame,
        text="Enter Function",
        font=SUBTITLE_FONT
    ).pack(pady=(20, 5))

    function_entry = ctk.CTkEntry(
        control_frame,
        height=40,
        font=ENTRY_FONT
    )

    function_entry.pack(
        fill="x",
        padx=20
    )


    function_entry.insert(0, "x**2")

    def auto_plot(event=None):
        plot_graph()

    function_entry.bind("<KeyRelease>", auto_plot)    

    examples = ctk.CTkLabel(
            control_frame,
            text="Examples:\nx**2\nnp.sin(x)\nnp.sin(x), np.cos(x)\nx**2, x**3",
            font=TEXT_FONT,
            justify="left"
        )

    examples.pack(
        pady=15,
        padx=20,
        anchor="w"
    )

    details_frame = ctk.CTkFrame(
    control_frame,
    fg_color=BG_COLOR,
    height=130
)

    
    details_frame.pack(
        fill="x",
        padx=15,
        pady=10
    )

    details_title = ctk.CTkLabel(
        details_frame,
        text="📊 Graph Details",
        font=SUBTITLE_FONT
    )

    details_title.pack(pady=(5, 2))

    details_label = ctk.CTkLabel(
        details_frame,
        text="No Graph Plotted",
        font=TEXT_FONT,
        justify="left"
    )

    details_label.pack(
        padx=10,
        pady=(0, 2),
        anchor="w"
    )

    

    canvas_widget = None
    toolbar = None
    current_figure = None
    graph_history= ""
    x_start= -10
    x_end = 10
    y_start = -10
    y_end = 10

    def plot_graph():

        nonlocal canvas_widget,toolbar,current_figure,graph_history, x_start,x_end,y_start,y_end

        try:

            expression = function_entry.get()

            functions = expression.split(",")
            graph_history += expression + "\n"

            x = np.linspace(x_start, x_end,500)

            fig = plt.Figure(
                figsize=(6, 4),
                dpi=100
            )

            current_figure = fig

            ax = fig.add_subplot(111)

            functions = expression.split(",")

            for func in functions:

                func = func.strip()

                y = eval(
                    func,
                    {"np": np, "x": x}
                )

                ax.plot(
                    x,
                    y,
                    label=func
                )

            ax.set_title("Graph Plotter")

            ax.legend()

            ax.set_ylim(y_start,y_end)

            ax.grid(True)
            if canvas_widget:canvas_widget.get_tk_widget().destroy()

            details_text = (
            f"Functions: {len(functions)}\n"
            f"X Range: {x_start} to {x_end}\n"
            f"Y Range: {y_start} to {y_end}\n"
            f"Points: 500\n"
            f"{expression}"
            )
            

            details_label.configure(
                text=details_text
            )

            if toolbar:
                toolbar.destroy()

            canvas_widget = FigureCanvasTkAgg(
                fig,
                master=graph_frame
            )

            canvas_widget.draw()

            canvas_widget.get_tk_widget().pack(
                fill="both",
                expand=True,
                padx=10,
                pady=10
            )

            toolbar = NavigationToolbar2Tk(
                canvas_widget,
                graph_frame
            )

            toolbar.update()

        except Exception:

            error_label.configure(
                text="Invalid Function"
            )


    def clear_graph():

        nonlocal canvas_widget,toolbar

        if canvas_widget:
            canvas_widget.get_tk_widget().destroy()
            canvas_widget = None

        if toolbar:
            toolbar.destroy()
            toolbar = None    

        error_label.configure(text="")

        details_label.configure(
            text="No Graph Plotted"
        )

    def save_graph():

        nonlocal current_figure

        if current_figure is None:
            error_label.configure(
            text="No graph to save"
            )
            return

        file_path = filedialog.asksaveasfilename(
             defaultextension=".png",
             filetypes=[("PNG Files", "*.png")]
        )

        if file_path:

             current_figure.savefig(file_path)

             error_label.configure(
             text="Graph Saved Successfully!"
            )

    def show_range_settings():

        nonlocal x_start, x_end,y_start,y_end

        settings_window = ctk.CTkToplevel(parent)

        settings_window.title("Graph Range")

        settings_window.geometry("300x350")

        settings_window.grab_set()

        ctk.CTkLabel(
            settings_window,
            text="X Start"
        ).pack(pady=(15, 5))

        start_entry = ctk.CTkEntry(settings_window)

        start_entry.pack(padx=20, fill="x")

        start_entry.insert(0, str(x_start))

        ctk.CTkLabel(
            settings_window,
            text="X End"
        ).pack(pady=(10, 5))

        end_entry = ctk.CTkEntry(settings_window)

        end_entry.pack(padx=20, fill="x")

        end_entry.insert(0, str(x_end))

        ctk.CTkLabel(
            settings_window,
            text="Y Start"
        ).pack(pady=(10, 5))

        y_start_entry = ctk.CTkEntry(settings_window)

        y_start_entry.pack(
            padx=20,
            fill="x"
        )

        y_start_entry.insert(
            0,
            str(y_start)
        )

        ctk.CTkLabel(
            settings_window,
            text="Y End"
        ).pack(pady=(10, 5))

        y_end_entry = ctk.CTkEntry(settings_window)

        y_end_entry.pack(
            padx=20,
            fill="x"
        )

        y_end_entry.insert(
            0,
            str(y_end)
        )
     
        def apply_range():

            nonlocal x_start, x_end,y_start,y_end

            try:

                x_start = float(start_entry.get())
                x_end = float(end_entry.get())
                y_start = float(y_start_entry.get())
                y_end = float(y_end_entry.get())

                settings_window.destroy()

                plot_graph()

            except:

                pass

        ctk.CTkButton(
            settings_window,
            text="Apply",
            command=apply_range
        ).pack(pady=20)

    edit_range_btn = ctk.CTkButton(
        details_frame,
        text="⚙ Edit Range",
        command= show_range_settings,
        height=28,
        font=TEXT_FONT,
        fg_color=BUTTON_BLUE
    )

    edit_range_btn.pack(
        padx=10,
        pady=(0, 4),
        fill="x"
    )                 

    def show_history():

        history_window = ctk.CTkToplevel(parent)

        history_window.title("Graph History")

        history_window.geometry("500x350")

        history_window.grab_set()

        ctk.CTkLabel(
            history_window,
            text="📜 Graph History",
            font=SUBTITLE_FONT
        ).pack(pady=10)

        history_box = ctk.CTkTextbox(
            history_window,
            font=TEXT_FONT
        )

        history_box.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        history_box.insert(
            "1.0",
            graph_history
        )

        def clear_history():

            nonlocal graph_history

            graph_history = ""

            history_box.delete("1.0", "end")

            history_box.insert(
                "1.0",
                "History cleared."
            )

        ctk.CTkButton(
            history_window,
            text="🗑 Clear History",
            command=clear_history,
            fg_color=CLEAR_BTN,
            hover_color=CLEAR_HOVER,
            text_color="black"
        ).pack(pady=(0, 10))
        
    ctk.CTkButton(
        control_frame,
        text="Plot Graph",
        command=plot_graph,
        fg_color=BUTTON_GREEN,
        font=BUTTON_FONT
    ).pack(
        fill="x",
         padx=20,
        pady=(5, 2)
    )

    ctk.CTkButton(
        control_frame,
        text="Clear Graph",
        command=clear_graph,
        fg_color=CLEAR_BTN,
        hover_color=CLEAR_HOVER,
        text_color="black",
        font=BUTTON_FONT
    ).pack(
        fill="x",
        padx=20,
        pady=2
    )

    ctk.CTkButton(
        control_frame,
        text="View History",
        command=show_history,
        fg_color=BUTTON_BLUE,
        font=BUTTON_FONT
    ).pack(
        fill="x",
        padx=20,
        pady=2
    )

    ctk.CTkButton(
        control_frame,
        text="💾 Save PNG",
        command=save_graph,
        fg_color=BUTTON_GREEN,
        font=BUTTON_FONT
    ).pack(
        fill="x",
        padx=20,
        pady=(2,2)
    ) 

    error_label = ctk.CTkLabel(
        control_frame,
        text="",
        text_color="red",
        font=TEXT_FONT
    )

    error_label.pack(
        pady=10
    )
    plot_graph()
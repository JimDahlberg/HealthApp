import tkinter as tk
import Page

class Gui:
    """Creates the main window and mainframe for the application, calls on the LoginGui class on application startup"""
    def __init__(self):
        
        self._root = tk.Tk()
        self._root.title("Health Application")
        self._root.geometry(
            f"{self._root.winfo_screenwidth()}x{self._root.winfo_screenheight()-300}"
        )
        # self._root.state(
        #     "zoomed"
        # )

        self._main_frame = tk.Frame(self._root)
        self._main_frame.pack(
            fill=tk.BOTH,
            expand=1
        )

        self._main_canvas = tk.Canvas(self._main_frame)
        self._main_canvas.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            expand=1
        )

        self._y_scrollbar = tk.Scrollbar(
            self._main_frame,
            orient=tk.VERTICAL,
            command=self._main_canvas.yview
        )
        self._y_scrollbar.pack(
            side=tk.RIGHT,
            fill=tk.Y
        )

        self._x_scrollbar = tk.Scrollbar(
            self._root,
            orient=tk.HORIZONTAL,
            command=self._main_canvas.xview
        )
        self._x_scrollbar.pack(
            side=tk.BOTTOM,
            fill=tk.X
        )

        self._main_canvas.configure(
            yscrollcommand=self._y_scrollbar.set, 
            xscrollcommand=self._x_scrollbar.set
            )
        self._main_canvas.bind(
            "<Configure>",
            lambda e: self._main_canvas.configure(scrollregion=self._main_canvas.bbox("all"))
        )

        self._window_frame = tk.Frame(self._main_canvas)
        self._main_canvas.create_window(
            (0,0),
            window=self._window_frame,
            anchor=tk.NW
        )

        self._test = Page.LoginGUI(self._root, self._window_frame)

    def mainloop(self):
        self._root.mainloop()
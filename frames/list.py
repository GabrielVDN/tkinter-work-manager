import tkinter as tk
from tkinter import ttk


class List(ttk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        label_1 = ttk.Label(
            self, text="Double Click To Copy Password"
        )
        label_1.grid(row=0, column=0)


        for child in self.winfo_children():
            child.grid_configure(padx=8, pady=8)
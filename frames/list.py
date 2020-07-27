import tkinter as tk
from tkinter import ttk


class List(ttk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Center your Frame in the middle-top.
        self.columnconfigure(0, weight=1)

        # Adding the Treeview
        label_1 = ttk.Label(self, text="Double Click to copy password")
        label_1.grid(row=0, column=0)

        btn_back = ttk.Button(
            self,
            text="🔙",
            command=lambda: controller.show_frame("Home"),
            cursor="hand2",
            width=3
        )
        btn_back.grid(row=0, column=1, sticky="E")

        scroll = ttk.Scrollbar(self, orient='vertical', takefocus=True)
        self.tree = ttk.Treeview(self, columns=headings, show="headings")
        scroll.config(command=self.tree.yview)
        self.tree.configure(yscroll=scroll.set)

        scroll.grid(row=1, columnspan=2)
        self.tree.grid(row=1, column=1)

        # Adding headings to the columns and resp. cmd's
        for heading in headings:
            self.tree.heading(
                heading, text=heading,
                command=lambda c=heading: self.sortby(self.tree, c, 0))
            self.tree.column(heading, width=400)


        for child in self.winfo_children():
            child.grid_configure(padx=8, pady=8)
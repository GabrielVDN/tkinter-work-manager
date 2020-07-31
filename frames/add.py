import tkinter as tk
from tkinter import ttk
import json
from tkinter import messagebox


class Add(ttk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # Center your Frame in the middle-top.
        self.columnconfigure(0, weight=1)
        
        label_service = ttk.Label(self, text="Service*")
        label_service.grid(row=0, columnspan=2, padx=8, pady=8)
        
        btn_back = ttk.Button(
            self,
            text="🔙",
            command=lambda: [controller.show_frame("Home"), self.empty_entry()],
            cursor="hand2",
            width=3
        )
        btn_back.grid(row=0, column=1, sticky="E", padx=8, pady=8)

        self.entry_service = ttk.Entry(
            self,
            width=18,
            textvariable=controller.add_service,
            font=("TkDefaultFont", 16)
        )
        self.entry_service.grid(row=1, columnspan=2, padx=8, pady=(8, 18))

        label_username = ttk.Label(
            self, text="Username"
        )
        label_username.grid(row=2, columnspan=2, padx=8, pady=8)

        self.entry_username = ttk.Entry(
            self,
            width=18,
            textvariable=controller.add_username,
            font=("TkDefaultFont", 16)
        )
        self.entry_username.grid(row=3, columnspan=2, padx=8, pady=(8, 18))

        label_password = ttk.Label(
            self, text="Password*"
        )
        label_password.grid(row=4, columnspan=2, padx=8, pady=8)

        self.entry_password = ttk.Entry(
            self,
            width=18,
            textvariable=controller.add_password,
            font=("TkDefaultFont", 16)
        )
        self.entry_password.grid(row=5, columnspan=2, padx=8, pady=(8, 18))

        btn_add = ttk.Button(
            self,
            text="Add To Manager",
            cursor="hand2",
            width=18,
            command=lambda: self.add_data()
        )
        btn_add.grid(row=6, columnspan=2, padx=8, pady=(8, 18))

        self.credential_nmr = tk.IntVar(value=1)


    def add_data(self):
        if self.controller.add_service.get().strip() != '' and self.controller.add_password.get().strip() != '':
            with open('data.txt') as json_file:
                data_list = json.load(json_file)

            data = {}
            data[self.credential_nmr.get()] = []
            data[self.credential_nmr.get()].append({
                'Service': self.controller.add_service.get().strip(),
                'Username': self.controller.add_username.get().strip(),
                'Password': self.controller.add_password.get().strip()
            })
            data_list.append(data)

            with open('data.txt', 'w') as outfile:
                json.dump(data_list, outfile, indent=2)

            self.credential_nmr.set(self.credential_nmr.get() + 1)

            self.empty_entry()
        else:
            messagebox.showerror("No Input", "You need to input something in Service and Password!")

    def empty_entry(self):
        self.entry_password.delete(0,'end')
        self.entry_service.delete(0,'end')
        self.entry_username.delete(0,'end')
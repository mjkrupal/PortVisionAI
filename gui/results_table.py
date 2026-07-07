import tkinter as tk
from tkinter import ttk
import customtkinter as ctk


class ResultsTable(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        title = ctk.CTkLabel(
            self,
            text="📋 Scan Results",
            font=("Consolas", 18, "bold")
        )
        title.pack(anchor="w", padx=15, pady=(10, 5))

        columns = (
            "Port",
            "Service",
            "Protocol",
            "Status",
            "Banner",
            "Version"
        )

        self.tree = ttk.Treeview(
            self,
            columns=columns,
            show="headings",
            height=12
        )

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor="center")

        scrollbar = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
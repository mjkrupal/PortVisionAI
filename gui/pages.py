import customtkinter as ctk
from gui.theme import Theme


class BasePage(ctk.CTkFrame):
    def __init__(self, parent, title):

        super().__init__(
            parent,
            fg_color=Theme.WINDOW_BG
        )

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        heading = ctk.CTkLabel(
            self,
            text=title,
            font=(Theme.FONT, 28, "bold"),
            text_color=Theme.ACCENT
        )

        heading.grid(row=0, column=0, sticky="w", padx=25, pady=25)
import customtkinter as ctk
from gui.theme import Theme


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent, callback):

        super().__init__(
            parent,
            width=220,
            fg_color=Theme.SIDEBAR_BG
        )

        self.callback = callback

        title = ctk.CTkLabel(
            self,
            text="PORTVISION AI",
            font=("Segoe UI", 22, "bold"),
            text_color=Theme.ACCENT
        )

        title.pack(pady=30)

        buttons = {
            "Dashboard": "dashboard",
            "Scan": "scan",
            "AI Assistant": "ai",
            "Reports": "reports",
            "History": "history",
            "Settings": "settings",
            "About": "about",
        }

        for text, page in buttons.items():

            btn = ctk.CTkButton(
                self,
                text=text,
                command=lambda p=page: self.callback(p),
                anchor="w"
            )

            btn.pack(fill="x", padx=15, pady=6)
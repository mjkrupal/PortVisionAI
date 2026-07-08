import customtkinter as ctk
from gui.theme import Theme


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            width=230,
            fg_color=Theme.SIDEBAR_BG,
            corner_radius=0
        )

        self.pack_propagate(False)

        title = ctk.CTkLabel(
            self,
            text="PORTVISION AI",
            font=(Theme.FONT, 22, "bold"),
            text_color=Theme.ACCENT
        )

        title.pack(pady=(30, 20))

        buttons = [
            "🏠 Dashboard",
            "🔍 Scan",
            "🤖 AI Chat",
            "📊 Reports",
            "📜 History",
            "⚙ Settings",
            "ℹ About"
        ]

        for text in buttons:

            btn = ctk.CTkButton(
                self,
                text=text,
                height=45,
                anchor="w",
                fg_color="transparent",
                hover_color="#1f2937"
            )

            btn.pack(fill="x", padx=15, pady=5)
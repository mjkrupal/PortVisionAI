import customtkinter as ctk

class Sidebar(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(
            parent,
            width=220,
            corner_radius=0
        )

        self.pack_propagate(False)

        title = ctk.CTkLabel(
            self,
            text="PortPilot AI",
            font=("Consolas", 24, "bold")
        )

        title.pack(pady=(25, 20))

        buttons = [
            "🏠 Dashboard",
            "🔍 New Scan",
            "📜 History",
            "📄 Reports",
            "⚙ Settings",
            "ℹ About"
        ]

        for item in buttons:
            btn = ctk.CTkButton(
                self,
                text=item,
                width=180,
                height=40
            )
            btn.pack(pady=8)
import customtkinter as ctk

class Header(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, height=70)

        self.pack_propagate(False)

        title = ctk.CTkLabel(
            self,
            text="PortPilot AI v1.0",
            font=("Consolas", 24, "bold")
        )

        title.pack(side="left", padx=20)

        status = ctk.CTkLabel(
            self,
            text="🟢 Ready",
            font=("Consolas", 14)
        )

        status.pack(side="right", padx=20)
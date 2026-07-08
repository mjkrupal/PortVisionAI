import customtkinter as ctk
from gui.theme import Theme


class Dashboard(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color=Theme.WINDOW_BG
        )

        title = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=(Theme.FONT, 28, "bold"),
            text_color=Theme.ACCENT
        )

        title.pack(anchor="w", padx=30, pady=(30, 20))

        welcome = ctk.CTkLabel(
            self,
            text="Welcome to PortVision AI",
            font=(Theme.FONT, 18),
            text_color="white"
        )

        welcome.pack(anchor="w", padx=30)

        self.create_cards()

    def create_cards(self):

        frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        frame.pack(fill="x", padx=30, pady=25)

        cards = [
            ("Open Ports", "0"),
            ("Risk Score", "0"),
            ("CVEs", "0"),
            ("Last Scan", "--")
        ]

        for title, value in cards:

            card = ctk.CTkFrame(
                frame,
                width=220,
                height=120,
                fg_color=Theme.CARD_BG
            )

            card.pack(side="left", padx=10)

            card.pack_propagate(False)

            ctk.CTkLabel(
                card,
                text=title,
                font=(Theme.FONT, 16),
                text_color="gray"
            ).pack(pady=(20, 5))

            ctk.CTkLabel(
                card,
                text=value,
                font=(Theme.FONT, 30, "bold"),
                text_color=Theme.ACCENT
            ).pack()
import customtkinter as ctk
from gui.pages import BasePage
from gui.theme import Theme
from utils.app_state import state

class Dashboard(BasePage):

    def __init__(self, parent):

        super().__init__(parent, "Dashboard")

        self.create_cards()
        self.create_ai_status()
        self.create_recent_activity()
        self.create_quick_actions()

    def create_cards(self):

        frame = ctk.CTkFrame(self)

        frame.grid(
            row=1,
            column=0,
            padx=20,
            pady=15,
            sticky="ew"
        )

        frame.grid_columnconfigure((0,1,2,3,4,5),weight=1)

        cards = [
            ("Open Ports","0"),
            ("Closed","0"),
            ("Filtered","0"),
            ("Risk","Low"),
            ("Duration","0 sec"),
            ("Threads","200")
        ]

        for i,(title,value) in enumerate(cards):

            card = ctk.CTkFrame(frame)

            card.grid(
                row=0,
                column=i,
                padx=8,
                pady=8,
                sticky="nsew"
            )

            ctk.CTkLabel(
                card,
                text=title,
                text_color="gray"
            ).pack(pady=(15,5))

            ctk.CTkLabel(
                card,
                text=value,
                font=(Theme.FONT,22,"bold"),
                text_color=Theme.ACCENT
            ).pack(pady=(0,15))

    def create_ai_status(self):

        frame=ctk.CTkFrame(self)

        frame.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=20,
            pady=10
        )

        ctk.CTkLabel(
            frame,
            text="AI Status",
            font=(Theme.FONT,20,"bold"),
            text_color=Theme.ACCENT
        ).pack(anchor="w",padx=15,pady=(15,5))

        ctk.CTkLabel(
            frame,
            text="Model : llama3.2\nStatus : Waiting for Ollama",
            justify="left"
        ).pack(anchor="w",padx=15,pady=(0,15))

    def create_recent_activity(self):

        frame=ctk.CTkFrame(self)

        frame.grid(
            row=3,
            column=0,
            sticky="nsew",
            padx=20,
            pady=10
        )

        ctk.CTkLabel(
            frame,
            text="Recent Activity",
            font=(Theme.FONT,20,"bold"),
            text_color=Theme.ACCENT
        ).pack(anchor="w",padx=15,pady=(15,10))

        self.activity=ctk.CTkTextbox(
            frame,
            height=140
        )

        self.activity.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0,15)
        )

        self.activity.insert(
            "end",
            "• PortVision AI Ready\n"
            "• Waiting for first scan...\n"
        )

    def create_quick_actions(self):

        frame=ctk.CTkFrame(self)

        frame.grid(
            row=4,
            column=0,
            sticky="ew",
            padx=20,
            pady=10
        )

        buttons=[
            "New Scan",
            "AI Assistant",
            "Reports",
            "History"
        ]

        for text in buttons:

            btn=ctk.CTkButton(
                frame,
                text=text
            )

            btn.pack(
                side="left",
                padx=10,
                pady=15
            )
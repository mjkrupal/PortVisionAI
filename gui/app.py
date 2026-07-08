"""
Main Application Window
"""

import customtkinter as ctk

from config import (
    APP_NAME,
    APP_VERSION,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
)

from gui.theme import Theme


class PortVisionApp(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title(f"{APP_NAME} {APP_VERSION}")

        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        self.minsize(1200, 700)

        self.configure(
            fg_color=Theme.WINDOW_BG
        )

        self.build_ui()

    def build_ui(self):

        title = ctk.CTkLabel(
            self,
            text="PortVision AI",
            font=(
                Theme.FONT,
                Theme.TITLE_SIZE,
                "bold",
            ),
            text_color=Theme.ACCENT,
        )

        title.pack(
            pady=(40, 10)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="AI Powered Intelligent Network Port Scanner",
            font=(
                Theme.FONT,
                16,
            ),
            text_color=Theme.SUBTEXT,
        )

        subtitle.pack()

        button = ctk.CTkButton(
            self,
            text="Start Scanning",
            width=220,
            height=45,
        )

        button.pack(
            pady=40
        )
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

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        from gui.sidebar import Sidebar
        from gui.dashboard import Dashboard

        self.sidebar = Sidebar(self)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        self.dashboard = Dashboard(self)
        self.dashboard.grid(row=0, column=1, sticky="nsew")
"""
Main Application Window
"""

import customtkinter as ctk

from config import APP_NAME, APP_VERSION, WINDOW_WIDTH, WINDOW_HEIGHT
from gui.theme import Theme

from gui.sidebar import Sidebar

from gui.dashboard import Dashboard
from gui.scan_page import ScanPage
from gui.ai_chat import AIChatPage
from gui.report_page import ReportPage
from gui.history_page import HistoryPage
from gui.settings_page import SettingsPage
from gui.about_page import AboutPage


class PortVisionApp(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title(f"{APP_NAME} {APP_VERSION}")

        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        self.minsize(1200, 700)

        self.configure(fg_color=Theme.WINDOW_BG)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar = Sidebar(self, self.show_page)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        # Main Content Area
        self.container = ctk.CTkFrame(
            self,
            fg_color=Theme.WINDOW_BG
        )

        self.container.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Pages
        self.pages = {
            "dashboard": Dashboard(self.container),
            "scan": ScanPage(self.container),
            "ai": AIChatPage(self.container),
            "reports": ReportPage(self.container),
            "history": HistoryPage(self.container),
            "settings": SettingsPage(self.container),
            "about": AboutPage(self.container),
        }

        # Place every page in same position
        for page in self.pages.values():
            page.grid(row=0, column=0, sticky="nsew")

        # Show dashboard first
        self.show_page("dashboard")

    def show_page(self, page_name):

        self.pages[page_name].tkraise()
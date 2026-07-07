import customtkinter as ctk
from gui.results_table import ResultsTable
from controller.app_controller import AppController
from config import *

from gui.sidebar import Sidebar
from gui.header import Header
from gui.prompt_panel import PromptPanel
from gui.stat_cards import StatCards


class Dashboard(ctk.CTk):

    def __init__(self):

        super().__init__()
        self.controller = AppController()
        self.title(APP_NAME)
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar = Sidebar(self)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        # Main Area
        self.main = ctk.CTkFrame(self)
        self.main.grid(row=0, column=1, sticky="nsew")

        self.main.grid_columnconfigure(0, weight=1)

        # Header
        self.header = Header(self.main)
        self.header.pack(fill="x")

        # Prompt Panel
        self.prompt_panel = PromptPanel(
        self.main,
        self.controller
      )
        self.prompt_panel.pack(fill="x", padx=15, pady=10)

        # Statistics Cards
        self.cards = StatCards(self.main)
        self.cards.pack(fill="x", padx=15)

        self.results = ResultsTable(self.main)
        self.results.pack(fill="both", expand=True, padx=15, pady=10)
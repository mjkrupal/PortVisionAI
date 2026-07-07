import customtkinter as ctk

from config import *

from controller.app_controller import AppController

from gui.sidebar import Sidebar
from gui.header import Header
from gui.prompt_panel import PromptPanel
from gui.manual_scan_panel import ManualScanPanel
from gui.stat_cards import StatCards
from gui.results_table import ResultsTable
from gui.terminal_panel import TerminalPanel
from gui.analysis_panel import AnalysisPanel
from gui.footer import Footer


class Dashboard(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title(APP_NAME)
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        self.controller = AppController()

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar = Sidebar(self)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        # Main Frame
        self.main = ctk.CTkFrame(self)
        self.main.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.main.grid_columnconfigure(0, weight=1)
        self.main.grid_columnconfigure(1, weight=1)

        # Header
        self.header = Header(self.main)
        self.header.grid(row=0, column=0, columnspan=2, sticky="ew", pady=5)

        # Prompt
        self.prompt = PromptPanel(self.main, self.controller)
        self.prompt.grid(row=1, column=0, columnspan=2, sticky="ew", pady=5)

        # Manual Panel
        self.manual = ManualScanPanel(self.main)
        self.manual.grid(row=2, column=0, columnspan=2, sticky="ew", pady=5)

        # Cards
        self.cards = StatCards(self.main)
        self.cards.grid(row=3, column=0, columnspan=2, sticky="ew", pady=5)

        # Results
        self.results = ResultsTable(self.main)
        self.results.grid(row=4, column=0, columnspan=2, sticky="nsew", pady=5)

        # Terminal
        self.terminal = TerminalPanel(self.main)
        self.terminal.grid(row=5, column=0, sticky="nsew", padx=(0, 5), pady=5)

        # AI Analysis
        self.analysis = AnalysisPanel(self.main)
        self.analysis.grid(row=5, column=1, sticky="nsew", padx=(5, 0), pady=5)

        # Footer
        self.footer = Footer(self.main)
        self.footer.grid(row=6, column=0, columnspan=2, sticky="ew")

        self.main.grid_rowconfigure(4, weight=3)
        self.main.grid_rowconfigure(5, weight=2)
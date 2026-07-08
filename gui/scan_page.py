import threading
import time
import customtkinter as ctk
from tkinter import ttk

from gui.pages import BasePage
from scanner.scan_engine import ScanEngine


class ScanPage(BasePage):

    def __init__(self, parent):

        super().__init__(parent, "Scan Center")

        self.engine = ScanEngine()

        self.build_ui()

    def build_ui(self):

        # ---------- Top Controls ----------

        top = ctk.CTkFrame(self)
        top.grid(row=1, column=0, sticky="ew", padx=20)

        top.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(
            top,
            text="Target"
        ).grid(row=0, column=0, padx=10, pady=15)

        self.target = ctk.CTkEntry(
            top,
            placeholder_text="127.0.0.1"
        )

        self.target.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=10
        )

        self.scan_btn = ctk.CTkButton(
            top,
            text="▶ Start Scan",
            command=self.start_scan
        )

        self.scan_btn.grid(row=0, column=2, padx=10)

        self.stop_btn = ctk.CTkButton(
            top,
            text="■ Stop",
            fg_color="red"
        )

        self.stop_btn.grid(row=0, column=3)

        # ---------- Progress ----------

        self.progress = ctk.CTkProgressBar(self)

        self.progress.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=20,
            pady=15
        )

        self.progress.set(0)

        # ---------- Results ----------

        self.tree = ttk.Treeview(
            self,
            columns=("Port",),
            show="headings",
            height=12
        )

        self.tree.heading("Port", text="Open Port")

        self.tree.grid(
            row=3,
            column=0,
            sticky="nsew",
            padx=20
        )

        # ---------- Activity ----------

        self.log = ctk.CTkTextbox(
            self,
            height=180
        )

        self.log.grid(
            row=4,
            column=0,
            sticky="ew",
            padx=20,
            pady=20
        )

        self.grid_rowconfigure(3, weight=1)

    def start_scan(self):

        threading.Thread(
            target=self.run_scan,
            daemon=True
        ).start()

    def run_scan(self):

        self.progress.set(0)

        self.tree.delete(*self.tree.get_children())

        target = self.target.get().strip()

        if target == "":
            target = "127.0.0.1"

        self.log.insert(
            "end",
            f"\nScanning {target}...\n"
        )

        start = time.time()

        ports = self.engine.scan(
            target,
            "Top 100"
        )

        elapsed = round(
            time.time()-start,
            2
        )

        for port in ports:

            self.tree.insert(
                "",
                "end",
                values=(port,)
            )

            self.log.insert(
                "end",
                f"OPEN : {port}\n"
            )

        self.progress.set(1)

        self.log.insert(
            "end",
            f"\nFinished in {elapsed} sec\n"
        )

        self.log.see("end")
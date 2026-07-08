import threading
import time
import customtkinter as ctk
from tkinter import ttk

from gui.pages import BasePage
from scanner.scan_engine import ScanEngine
from scanner.scan_controller import ScanController


class ScanPage(BasePage):

    def __init__(self, parent):

        super().__init__(parent, "Scan Center")

        self.controller = ScanController(
            progress_callback=self.update_progress,
            result_callback=self.add_result,
            finished_callback=self.scan_finished,
        )

        self.build_ui()

    def build_ui(self):

        # ===========================
        # Top Controls
        # ===========================

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

        self.scan_btn.grid(
            row=0,
            column=2,
            padx=10
        )

        self.stop_btn = ctk.CTkButton(
            top,
            text="■ Stop",
            fg_color="red",
            command=self.controller.stop_scan
        )

        self.stop_btn.grid(
            row=0,
            column=3,
            padx=10
        )

        # ===========================
        # Progress Bar
        # ===========================

        self.progress = ctk.CTkProgressBar(self)

        self.progress.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=20,
            pady=15
        )

        self.progress.set(0)

        # ===========================
        # Results Table
        # ===========================

        columns = (
            "Port",
            "Service",
            "Status",
            "Latency"
        )

        self.tree = ttk.Treeview(
            self,
            columns=columns,
            show="headings",
            height=12
        )

        for col in columns:

            self.tree.heading(col, text=col)

            self.tree.column(
                col,
                anchor="center",
                width=150
            )

        self.tree.grid(
            row=3,
            column=0,
            sticky="nsew",
            padx=20
        )

        # ===========================
        # Activity Log
        # ===========================

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

        target = self.target.get().strip()

        if not target:
            target = "127.0.0.1"

        self.progress.set(0)

        self.tree.delete(*self.tree.get_children())

        self.log.delete("1.0", "end")

        self.log.insert(
            "end",
            f"[*] Starting scan on {target}\n\n"
        )

        self.controller.start_scan(
            target,
            "Top 100",
        )

    def run_scan(self):

        self.progress.set(0)

        self.tree.delete(*self.tree.get_children())

        self.log.delete("1.0", "end")

        target = self.target.get().strip()

        if target == "":
            target = "127.0.0.1"

        self.log.insert(
            "end",
            f"[*] Starting scan on {target}\n\n"
        )

        start = time.time()

        results = self.engine.scan(
            target,
            "Top 100"
        )

        elapsed = round(
            time.time() - start,
            2
        )

        if not results:

            self.log.insert(
                "end",
                "[!] No open ports found.\n"
            )

        else:

            for result in results:

                self.tree.insert(
                    "",
                    "end",
                    values=(
                        result.port,
                        result.service,
                        result.status,
                        f"{result.latency:.4f}s"
                    )
                )

                self.log.insert(
                    "end",
                    f"[OPEN] Port {result.port:<5} "
                    f"Service: {result.service:<15} "
                    f"Latency: {result.latency:.4f}s\n"
                )

        self.progress.set(1)

        self.log.insert(
            "end",
            f"\n[✓] Scan completed in {elapsed} seconds\n"
        )

        self.log.see("end")

    def scan_finished(self, results):

        def finish():

            self.progress.set(1)

            self.log.insert(
                "end",
                f"\n[✓] Scan Complete\n"
            )

            self.log.see("end")

        self.after(0, finish)

    def update_progress(self, event):
        """
        Update progress bar from ScanEngine.
        """
        self.after(
            0,
            lambda: self.progress.set(event.percent)
        )


    def add_result(self, event):
        """
        Receive a ScanResult from the engine.
        """
        self.after(
            0,
            lambda: self.insert_result(event.result)
        )


    def insert_result(self, result):
        """
        Add one result to the table and log.
        """
        self.tree.insert(
            "",
            "end",
            values=(
                result.port,
                result.service,
                result.status,
                f"{result.latency:.4f}s",
            )
        )

        self.log.insert(
            "end",
            f"[OPEN] {result.port:<5} {result.service}\n"
        )

        self.log.see("end")
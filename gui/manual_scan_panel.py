import customtkinter as ctk


class ManualScanPanel(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        # ---------- Title ----------
        title = ctk.CTkLabel(
            self,
            text="⚙ Manual Scan Configuration",
            font=("Consolas", 18, "bold")
        )

        title.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=15,
            pady=(15, 20),
            sticky="w"
        )

        # ---------- Target ----------
        ctk.CTkLabel(
            self,
            text="Target"
        ).grid(row=1, column=0, padx=15, pady=8, sticky="w")

        self.target_entry = ctk.CTkEntry(
            self,
            width=350,
            placeholder_text="scanme.nmap.org or 192.168.1.10"
        )

        self.target_entry.grid(
            row=1,
            column=1,
            padx=15,
            pady=8,
            sticky="ew"
        )

        # ---------- Port Range ----------
        ctk.CTkLabel(
            self,
            text="Port Range"
        ).grid(row=2, column=0, padx=15, pady=8, sticky="w")

        self.port_entry = ctk.CTkEntry(
            self,
            width=350,
            placeholder_text="1-1024"
        )

        self.port_entry.insert(0, "1-1024")

        self.port_entry.grid(
            row=2,
            column=1,
            padx=15,
            pady=8,
            sticky="ew"
        )

        # ---------- Threads ----------
        ctk.CTkLabel(
            self,
            text="Threads"
        ).grid(row=3, column=0, padx=15, pady=8, sticky="w")

        self.thread_entry = ctk.CTkEntry(
            self,
            width=350
        )

        self.thread_entry.insert(0, "100")

        self.thread_entry.grid(
            row=3,
            column=1,
            padx=15,
            pady=8,
            sticky="ew"
        )

        # ---------- Timeout ----------
        ctk.CTkLabel(
            self,
            text="Timeout"
        ).grid(row=4, column=0, padx=15, pady=8, sticky="w")

        self.timeout_entry = ctk.CTkEntry(
            self,
            width=350
        )

        self.timeout_entry.insert(0, "1")

        self.timeout_entry.grid(
            row=4,
            column=1,
            padx=15,
            pady=8,
            sticky="ew"
        )

        # ---------- Protocol ----------
        ctk.CTkLabel(
            self,
            text="Protocol"
        ).grid(row=5, column=0, padx=15, pady=8, sticky="w")

        self.protocol = ctk.CTkOptionMenu(
            self,
            values=[
                "TCP",
                "UDP"
            ]
        )

        self.protocol.grid(
            row=5,
            column=1,
            padx=15,
            pady=8,
            sticky="w"
        )

        self.grid_columnconfigure(1, weight=1)
import customtkinter as ctk


class TerminalPanel(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        title = ctk.CTkLabel(
            self,
            text="💻 Activity Log",
            font=("Consolas", 18, "bold")
        )

        title.pack(anchor="w", padx=15, pady=(10, 5))

        self.log = ctk.CTkTextbox(
            self,
            height=180,
            font=("Consolas", 12)
        )

        self.log.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        self.write("CyberEye AI initialized...")
        self.write("Waiting for user input...")

    def write(self, message):
        self.log.insert("end", f"[INFO] {message}\n")
        self.log.see("end")

    def clear(self):
        self.log.delete("1.0", "end")
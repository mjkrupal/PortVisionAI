import customtkinter as ctk


class AnalysisPanel(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        title = ctk.CTkLabel(
            self,
            text="🧠 AI Security Analysis",
            font=("Consolas", 18, "bold")
        )

        title.pack(anchor="w", padx=15, pady=(10, 5))

        self.analysis = ctk.CTkTextbox(
            self,
            font=("Consolas", 12)
        )

        self.analysis.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

        self.write("Waiting for scan results...")

    def write(self, text):

        self.analysis.delete("1.0", "end")

        self.analysis.insert("end", text)
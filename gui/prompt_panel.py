import customtkinter as ctk


class PromptPanel(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        title = ctk.CTkLabel(
            self,
            text="🤖 AI Prompt",
            font=("Consolas", 18, "bold")
        )

        title.pack(anchor="w", padx=20, pady=(15, 5))

        self.prompt = ctk.CTkTextbox(
            self,
            height=100
        )

        self.prompt.pack(fill="x", padx=20)

        self.prompt.insert(
            "1.0",
            "Example:\nScan google.com for common web ports"
        )

        button_frame = ctk.CTkFrame(self)

        button_frame.pack(fill="x", padx=20, pady=15)

        self.interpret_btn = ctk.CTkButton(
        button_frame,
        text="Interpret AI",
        command=self.controller.interpret_prompt
        )

        self.interpret_btn.pack(side="left", padx=5)

        self.scan_btn = ctk.CTkButton(
        button_frame,
        text="Start Scan",
        command=self.controller.start_scan
        )

        self.scan_btn.pack(side="left", padx=5)

        self.stop_btn = ctk.CTkButton(
        button_frame,
        text="Stop Scan",
        fg_color="red",
        hover_color="#8B0000",
        command=self.controller.stop_scan
        )

        self.stop_btn.pack(side="left", padx=5)

       
import customtkinter as ctk

from gui.pages import BasePage
from gui.theme import Theme
from ai.prompt_parser import PromptParser
from ai.scan_planner import ScanPlanner



class AIChatPage(BasePage):

    def __init__(self, parent):

        super().__init__(parent, "AI Assistant")

        self.build()

    def build(self):

        self.chat = ctk.CTkTextbox(
            self,
            height=420
        )

        self.chat.grid(
            row=1,
            column=0,
            padx=25,
            pady=10,
            sticky="nsew"
        )

        self.chat.insert(
            "end",
            "Welcome to PortVision AI\n\n"
            "Try asking:\n\n"
            "• Scan localhost quickly\n"
            "• Scan scanme.nmap.org\n"
            "• Explain port 22\n"
            "• Scan only web ports\n\n"
        )

        bottom = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        bottom.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=25,
            pady=15
        )

        bottom.grid_columnconfigure(0, weight=1)

        self.prompt = ctk.CTkEntry(
            bottom,
            placeholder_text="Type your prompt..."
        )

        self.prompt.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=(0, 10)
        )

        self.send = ctk.CTkButton(
            bottom,
            text="Send Prompt",
            command=self.fake_ai
        )

        self.send.grid(
            row=0,
            column=1
        )

    def fake_ai(self):

        prompt = self.prompt.get().strip()

        if not prompt:
            return

        self.chat.insert(
            "end",
            f"\n\nYou:\n{prompt}\n"
        )

        plan = PromptParser.parse(prompt)

        response = ScanPlanner.generate(plan)

        self.current_plan = plan

        self.chat.insert(
            "end",
            "\nAI Scan Planner\n"
        )

        self.chat.insert(
            "end",
            response
        )

        self.prompt.delete(0, "end")

        self.chat.see("end")
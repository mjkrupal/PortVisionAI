import customtkinter as ctk


class ScanPlanDialog(ctk.CTkToplevel):

    def __init__(self, parent, plan, on_start):

        super().__init__(parent)

        self.title("AI Scan Plan")

        self.geometry("550x520")

        self.resizable(False, False)

        self.plan = plan

        self.on_start = on_start

        self.build_ui()

    def build_ui(self):

        title = ctk.CTkLabel(
            self,
            text="AI Generated Scan Plan",
            font=("Segoe UI", 24, "bold")
        )

        title.pack(pady=20)

        info = ctk.CTkTextbox(
            self,
            height=280
        )

        info.pack(
            fill="both",
            expand=True,
            padx=20
        )

        info.insert(
            "end",
            f"""
Target
-------------------
{self.plan["target"]}

Scan Type
-------------------
{self.plan["scan_type"]}

Ports
-------------------
{self.plan["ports"]}

Threads
-------------------
{self.plan["threads"]}

Timeout
-------------------
{self.plan["timeout"]} sec

Estimated Time
-------------------
2-5 Seconds

Reason
-------------------
The AI selected this strategy based on
your prompt.

"""
        )

        info.configure(state="disabled")

        buttons = ctk.CTkFrame(self)

        buttons.pack(
            fill="x",
            pady=20,
            padx=20
        )

        start = ctk.CTkButton(
            buttons,
            text="Start Scan",
            command=self.start_scan
        )

        start.pack(
            side="left",
            expand=True,
            padx=10
        )

        cancel = ctk.CTkButton(
            buttons,
            text="Cancel",
            fg_color="red",
            command=self.destroy
        )

        cancel.pack(
            side="right",
            expand=True,
            padx=10
        )

    def start_scan(self):

        self.on_start()

        self.destroy()
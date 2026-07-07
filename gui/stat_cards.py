import customtkinter as ctk


class StatCards(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        cards = [
            ("Open Ports", "0"),
            ("Scanned Ports", "0"),
            ("Elapsed Time", "00:00"),
            ("Risk Level", "Low")
        ]

        for title, value in cards:

            frame = ctk.CTkFrame(
                self,
                width=180,
                height=90
            )

            frame.pack(side="left", padx=15, pady=15)

            frame.pack_propagate(False)

            lbl1 = ctk.CTkLabel(
                frame,
                text=title,
                font=("Consolas", 14)
            )

            lbl1.pack(pady=(15, 5))

            lbl2 = ctk.CTkLabel(
                frame,
                text=value,
                font=("Consolas", 22, "bold")
            )

            lbl2.pack()
from gui.pages import BasePage


class Dashboard(BasePage):

    def __init__(self, parent):

        super().__init__(parent, "Dashboard")

        body = self

        cards = [
            ("Open Ports", "0"),
            ("Closed", "0"),
            ("Risk Score", "0"),
            ("CVEs", "0"),
            ("Duration", "--"),
            ("Threads", "0"),
        ]

        import customtkinter as ctk

        frame = ctk.CTkFrame(
            body,
            fg_color="transparent"
        )

        frame.grid(row=1, column=0, padx=25, sticky="nsew")

        rows = 2
        cols = 3

        index = 0

        for r in range(rows):

            frame.grid_rowconfigure(r, weight=1)

            for c in range(cols):

                frame.grid_columnconfigure(c, weight=1)

                title, value = cards[index]

                card = ctk.CTkFrame(frame)

                card.grid(
                    row=r,
                    column=c,
                    padx=15,
                    pady=15,
                    sticky="nsew"
                )

                ctk.CTkLabel(
                    card,
                    text=title,
                    font=("Segoe UI", 16)
                ).pack(pady=(25, 8))

                ctk.CTkLabel(
                    card,
                    text=value,
                    font=("Segoe UI", 28, "bold")
                ).pack()

                index += 1
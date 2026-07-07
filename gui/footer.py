import customtkinter as ctk


class Footer(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent, height=35)

        self.pack_propagate(False)

        self.status = ctk.CTkLabel(
            self,
            text="Status : Ready",
            anchor="w"
        )

        self.status.pack(
            side="left",
            padx=15
        )

    def update_status(self, text):

        self.status.configure(
            text=f"Status : {text}"
        )
import customtkinter # type: ignore

class Frame(customtkinter.CTkFrame):
    """ Frame object with a label """

    def __init__(self, master, name="Add Name", **kwargs):
        super().__init__(master, **kwargs)

        # Setup frame
        self.grid_columnconfigure(0, weight=1)

        # Add label to frame
        self.label = customtkinter.CTkLabel(self, text=name)
        self.label.grid(row=0, column=0, padx=10)


class EntryFrame(Frame):
    """ Frame object with data entry option """

    def __init__(self, master, name="Add Name", entry="Write here...", button="Submit", **kwargs):
        super().__init__(master, name, **kwargs)

        # Add entry field
        self.entry_field = customtkinter.CTkEntry(self, placeholder_text=entry)
        self.entry_field.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        # Add button
        self.button =customtkinter.CTkButton(self, text=button)
        self.button.grid(row=2, column=0, padx=20, pady=5, sticky="ew")
import customtkinter # type: ignore

class Frame(customtkinter.CTkFrame):
    """ 
    A frame containing a label 
    :param name: The text to display on the label.
    """

    def __init__(self, master, name="Add Name", **kwargs):
        super().__init__(master, **kwargs)

        # Setup frame
        self.grid_columnconfigure(0, weight=1)

        # Add label to frame
        self.label = customtkinter.CTkLabel(self, text=name)
        self.label.grid(row=0, column=0, padx=10)


class EntryFrame(Frame):
    def __init__(
            self, master, callback, 
            name="Add Name", entry="Write here...",
            button="Submit", **kwargs
        ):
        """ 
        A frame containing a label, an entry field and a button.
        :param master: The parent widget.
        :param callback: A function to call when the button is pressed.
        :param name: The text for the label on the parent widget.
        :param entry: The text for the placeholder on the entry field.
        :param button: The text to display on the button widget.
        """
        super().__init__(master, name, **kwargs)
        
        # Reference to callback function for displaying message
        self.callback = callback

        # Add entry field
        self.entry_field = customtkinter.CTkEntry(self, placeholder_text=entry)
        self.entry_field.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        # Add button
        self.button =customtkinter.CTkButton(
            self, 
            text=button, 
            command=self.send_results
            )
        self.button.grid(row=2, column=0, padx=20, pady=5, sticky="ew")

    def send_results(self):
        """
        Pass the query results to the callback function.
        """
        results = "This is a TEST"
        # Pass results to callback function
        if self.callback:
            self.callback(results)



class MessageLabel(customtkinter.CTkLabel):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)


        self.close_button = customtkinter.CTkButton(
            self,
            text="X",
            width=20,
            height=20,
            fg_color="red",
            text_color="white",
            command=self.hide
        )

        # Place button on right corner
        self.close_button.place(
            x=self.winfo_x() + self.winfo_width() - 25,
            y=self.winfo_y() + 5
        )

    def hide(self):
        """ Clear the label text """
        self.configure(text="")
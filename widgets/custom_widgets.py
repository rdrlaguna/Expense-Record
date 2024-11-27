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
            command=self.add_entry
            )
        self.button.grid(row=2, column=0, padx=20, pady=5, sticky="ew")


    def add_entry(self):
        """
        Pass the value of the entry field to the callback function.
        """
        value = self.entry_field.get()
        # Pass results to callback function
        if self.callback:
            self.callback(value)


class FrameDisplay(customtkinter.CTkScrollableFrame):
    """
    A Scrollable frame Containing one label per element. 
    """
    def __init__(self, master, callback, values=None, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.callback = callback
        self.values = values
        self.labels = []

        if self.values != None:
            self.update(self.values)
    

    def update(self, values):
        """ Update labels inside frame. """
        self.values = values

        # Remove labels if any
        if self.labels:
            for label in self.labels:
                label.destroy()

        # Add new labels
        for i, (id, name) in enumerate(self.values):
                label_frame = CategoryLabel(
                    self,
                    callback=self.callback,
                    name=name.title(),
                    id=id,
                    corner_radius=5,
                    fg_color="gray20"
                )
                label_frame.grid(row=i, column=0, padx=10, pady=(0, 5), sticky="ew")
                self.labels.append(label_frame)



class CategoryLabel(Frame):
    def __init__(self, master, callback, name, id, **kwargs):

        """
        A frame containing one label and one button.
        :param name: The category name to display on the label.
        :param id: The category id to be able to delete it.
        """

        super().__init__( master, name, **kwargs)

        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.callback = callback
        self.category_id = id

        delete_button = customtkinter.CTkButton(
            self, 
            text="DELETE",
            fg_color="gray50",
            hover_color="gray40",
            command=self.get_id
        )
        delete_button.grid(row=0, column=2, padx=20, pady=10)

    def get_id(self):
        if self.callback:
            self.callback(self.category_id)
            



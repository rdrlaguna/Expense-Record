# Create classes for project
import customtkinter # type: ignore

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Expense Record")
        self.geometry("800x450")
        self.grid_columnconfigure((0, 1, 2), weight=1)

        # Add frame
        self.frame_1 = Frame(self, name="Add Element", height=400)
        self.frame_1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Category window
        self.toplevel_window = None
        # Button to open window
        self.add_category_button = customtkinter.CTkButton(
            self, 
            text="Add Category",
            command=self.add_category()
            ) 
        self.add_category_button.grid(row=1, column=0, padx=20, pady=5)

    def add_category(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            # Create window if it does not exists
            self.toplevel_window = ToplevelWindow(self)
        else:
            self.toplevel_window.focus()



class Frame(customtkinter.CTkFrame):
    def __init__(self, master, name="Add Name", **kwargs):
        super().__init__(master, **kwargs)

        # Add label to frame
        self.label = customtkinter.CTkLabel(self, text=name)
        self.label.grid(row=0, column=0, padx=10)



class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("400x300")

        self.label = customtkinter.CTkLabel(self, text="Add Category")
        self.label.pack(padx=20, pady=20)


# Create classes for project
import customtkinter # type: ignore

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Set up main window
        self.title("Expense Record")
        self.geometry("800x450")
        self.grid_columnconfigure((0, 1, 2), weight=1)

        # Add frame
        self.frame_1 = Frame(self, name="Add Element", height=400)
        self.frame_1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Add Category button to manage categories
        self.categories_button = customtkinter.CTkButton(self, text="Categories", command=self.open_categories_window)
        self.categories_button.grid(row=1, column=0, padx=20, pady=20)

        self.categories_window = None

    def open_categories_window(self):
        if self.categories_window is None or not self.categories_window.winfo_exists():
            # Create window if its None or destroyed
            self.categories_window = CategoryWindow(self, name="CATEGORIES")  
        else:
            # If window exists focus it
            self.categories_window.focus()     




class Frame(customtkinter.CTkFrame):
    def __init__(self, master, name="Add Name", **kwargs):
        super().__init__(master, **kwargs)

        # Add label to frame
        self.label = customtkinter.CTkLabel(self, text=name)
        self.label.grid(row=0, column=0, padx=10)



class CategoryWindow(customtkinter.CTkToplevel):
    def __init__(self, master, name="Title", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.geometry("400x300")
        self.title(name)

        self.label = customtkinter.CTkLabel(self, text=name)
        self.label.pack(padx=20, pady=20)


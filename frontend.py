# Create classes for project
import backend
import customtkinter # type: ignore
import widgets 


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Set up main window
        self.title("Expense Record")
        self.geometry("800x450")
        self.grid_columnconfigure((0, 1, 2), weight=1)

        # Add frame
        self.frame_1 = widgets.Frame(self, name="Add Element", height=400)
        self.frame_1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Add Category button to manage categories
        self.categories_button = customtkinter.CTkButton(self, text="Categories", command=self.open_categories_window)
        self.categories_button.grid(row=1, column=0, padx=20, pady=20)

        self.categories_window = None

    def open_categories_window(self):
        """ Open window to edit categories """
        if self.categories_window is None or not self.categories_window.winfo_exists():
            # Create window if its None or destroyed
            self.categories_window = CategoryWindow(self, name="CATEGORIES")  
        else:
            # If window exists focus it
            self.categories_window.focus()     


class CategoryWindow(customtkinter.CTkToplevel):
    """ Window to edit categories """

    def __init__(self, master, name="Title", *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # Set up category window
        self.title(name)
        self.geometry("400x300")
        self.grid_columnconfigure(0, weight=1)
        
        # Add frame to display messages to user
        self.message = customtkinter.CTkLabel(self, text=None, fg_color="transparent")
        self.message.grid(row=0, column=0, sticky="ew")

        # Add frame to add new category
        self.category_add = widgets.EntryFrame(
            self,
            callback=self.add_category,
            name="New Category",
            entry="Add new category...",
            button="Add"
            )
        self.category_add.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        

    def add_category(self, value):
        #TODO: Clean value

        # Pass value to backend as single tuple
        category_name = (value,)
        self.display_message(backend.create_category(category_name))
        

    def display_message(self, message):
        """ Show query status for 3 seconds. """

        if message != "":
            self.message.configure(text=message)
        else:
            self.message.configure(text="Empty")

        # Clear label after 3 seconds
        if self.message.cget("text") != "":
            self.after(3000, self.clear_message)


    def clear_message(self):
        """ Clear message label. """
        self.message.configure(text="")

        # TODO: 
        # Show categories
        # Edit category

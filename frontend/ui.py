# Create classes for project
import backend.backend as backend
import customtkinter # type: ignore
import widgets.custom_widgets as widgets


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
        self.geometry("400x600")
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

        # Add frame to display current categories
        self.categories_display = widgets.FrameDisplay(
            self,
            callback=self.delete_category, 
            values=backend.get_all_categories())
        self.categories_display.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
        

    def add_category(self, value):
        """
        Add category to the database.

        :param value: The name of the category provided by the user.
        """
        #TODO: Validate category name

        # Pass value to backend as single tuple
        category_name = value
        self.display_message(backend.create_category(category_name))

        # Update frame display with new category
        self.categories_display.update(backend.get_all_categories())
        

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


    def delete_category(self, category_id):
        """ Delete category from database. """

        # Delete category and show message to user
        self.display_message(backend.delete_category(category_id))

        # Update frame display with new category
        self.categories_display.update(backend.get_all_categories())
        
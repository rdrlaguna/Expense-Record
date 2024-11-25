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

        self.button_1 = customtkinter.CTkButton(self, text="open toplevel", command=self.open_toplevel)
        self.button_1.grid(row=1, column=0, padx=20, pady=20)

        self.toplevel_window = None

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self, name="Add Category")  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it   




class Frame(customtkinter.CTkFrame):
    def __init__(self, master, name="Add Name", **kwargs):
        super().__init__(master, **kwargs)

        # Add label to frame
        self.label = customtkinter.CTkLabel(self, text=name)
        self.label.grid(row=0, column=0, padx=10)



class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, master, name="Title", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.geometry("400x300")
        self.title(name)

        self.label = customtkinter.CTkLabel(self, text=name)
        self.label.pack(padx=20, pady=20)


# Create classes for project
import customtkinter # type: ignore

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Expense Record")
        self.geometry("400x150")
        self.grid_columnconfigure(0, weight=1)
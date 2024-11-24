# Entry file on project
from classes import App
import customtkinter  # type: ignore

def main():

    # Setup mode
    customtkinter.set_default_color_theme("green")

    # Create new app
    app = App()

    # Run app
    app.mainloop()


if __name__ == "__main__":
    main()
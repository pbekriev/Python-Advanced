from tkinter import Tk


def create_root():
    root = Tk()

    root.title("GUI Shop")
    root.resizable(False, False)
    root.geometry("700x600")

    return root


root = create_root()

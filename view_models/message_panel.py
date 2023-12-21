import customtkinter
from tkinter import CENTER


class MessagePanel(customtkinter.CTkToplevel):
    def __init__(self, text, width, height, text_color, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry(str(width) + "x" + str(height))
        customtkinter.set_appearance_mode("dark")
        self.label = customtkinter.CTkLabel(self, text=text, text_color=text_color)
        self.label.place(relx=0.5, rely=0.5, anchor=CENTER)

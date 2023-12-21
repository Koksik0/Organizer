import customtkinter
from tkinter import CENTER
from database.create_database import select_all_data
from modules.main_panel_manager import AppManager
from modules.main_panel_manager import all_id, all_descriptions, all_titles, all_deadlines, all_completed


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # Size of main frame, title, ane default background and color of buttons, labels etc
        width = 1400
        height = 700
        self.geometry(str(width) + "x" + str(height))
        self.title("Organizer")
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.data_manager = AppManager(self)

        # Left and right frame
        self.left_frame = customtkinter.CTkFrame(
            self,
            width=680,
            height=height - 20,
            fg_color="black",
            corner_radius=20
        )

        self.left_frame.grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        self.right_frame = customtkinter.CTkFrame(
            self,
            width=680,
            height=height - 20,
            fg_color="black",
            corner_radius=20
        )

        self.right_frame.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        check_var = customtkinter.StringVar(value="False")

        self.left_checkbox_search = customtkinter.CTkCheckBox(
            self,
            text="Search completed",
            variable=check_var,
            onvalue="True",
            offvalue="False",
            bg_color="black",
            command=lambda: self.data_manager.search()
        )

        # All data
        self.current_id = None
        self.tasks = select_all_data(self.left_checkbox_search.get())
        self.ids = all_id(self.tasks)
        self.titles = all_titles(self.tasks)
        self.descriptions = all_descriptions(self.tasks)
        self.deadlines = all_deadlines(self.tasks)
        self.completed = all_completed(self.tasks)

        self.left_option_menu = customtkinter.CTkOptionMenu(
            self,
            values=[x for x in self.titles],
            anchor=CENTER,
            width=300,
            dropdown_fg_color='gray',
            dropdown_hover_color='green'
        )

        self.left_option_menu.place(
            x=20,
            y=20
        )

        self.left_checkbox_search.place(
            x=350,
            y=23
        )

        self.left_label_deadline = customtkinter.CTkLabel(
            self,
            text="Deadline:",
            bg_color="black"
        )

        self.left_label_deadline.place(
            x=510,
            y=20
        )

        self.left_entry_date = customtkinter.CTkEntry(
            self,
            width=100
        )

        self.left_entry_date.place(
            x=580,
            y=20
        )

        self.left_entry = customtkinter.CTkEntry(
            self,
            width=300
        )

        self.left_entry.place(
            x=200,
            y=90
        )

        self.left_title = customtkinter.CTkLabel(
            self,
            text="Title: ",
            width=300,
            bg_color="black"
        )

        self.left_title.place(
            x=200,
            y=60
        )

        self.left_title_textbox = customtkinter.CTkLabel(
            self,
            text="Description: ",
            width=300,
            bg_color="black"
        )

        self.left_title_textbox.place(
            x=200,
            y=130
        )

        self.left_textbox = customtkinter.CTkTextbox(
            self,
            width=660,
            height=470
        )
        self.left_textbox.place(
            x=20,
            y=170
        )

        self.left_button_update = customtkinter.CTkButton(
            self,
            width=250,
            text="Update",
            command=lambda: self.data_manager.update_data()
        )

        self.left_button_update.place(
            x=20,
            y=650
        )

        self.left_button_delete = customtkinter.CTkButton(
            self,
            width=250,
            text="Delete",
            fg_color="red",
            command=lambda: self.data_manager.delete()
        )

        self.left_button_delete.place(
            x=290,
            y=650
        )

        check_var = customtkinter.StringVar(value="False")
        self.left_checkbox = customtkinter.CTkCheckBox(
            self,
            text="Completed",
            variable=check_var,
            onvalue="True",
            offvalue="False",
            width=100,
            bg_color="black"
        )

        self.left_checkbox.place(
            x=580,
            y=650
        )

        self.option_menu_var = customtkinter.StringVar()
        self.left_option_menu.configure(variable=self.option_menu_var)
        self.option_menu_var.trace_add('write', self.data_manager.update)

        self.right_title = customtkinter.CTkLabel(
            self,
            text="Title: ",
            bg_color="black"
        )

        self.right_title.place(
            x=720,
            y=20
        )

        self.right_entry = customtkinter.CTkEntry(
            self,
            width=300
        )

        self.right_entry.place(
            x=760,
            y=20
        )

        self.right_label_date = customtkinter.CTkLabel(
            self,
            text="Deadline:",
            bg_color="black"
        )

        self.right_label_date.place(
            x=1220,
            y=20
        )

        self.right_entry_date = customtkinter.CTkEntry(
            self,
            width=100,
            placeholder_text='YYYY-MM-DD'
        )

        self.right_entry_date.place(
            x=1280,
            y=20
        )

        self.right_description = customtkinter.CTkLabel(
            self,
            text="Description:",
            bg_color="black",
            width=300
        )

        self.right_description.place(
            x=900,
            y=60
        )

        self.right_textbox = customtkinter.CTkTextbox(
            self,
            width=660,
            height=540
        )

        self.right_textbox.place(
            x=720,
            y=100
        )

        self.left_button_delete = customtkinter.CTkButton(
            self,
            width=350,
            text="Insert",
            command=lambda: self.data_manager.insert()
        )

        self.left_button_delete.place(
            x=875,
            y=650
        )

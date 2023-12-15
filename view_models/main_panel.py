import customtkinter
from tkinter import CENTER
from database.create_database import select_all_data, update_data, insert_data, delete_record


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

        # All data
        self.current_id = None
        self.tasks = select_all_data()
        self.ids = self.all_id(self.tasks)
        self.titles = self.all_titles(self.tasks)
        self.descriptions = self.all_descriptions(self.tasks)
        self.deadlines = self.all_deadlines(self.tasks)
        self.completed = self.all_compleded(self.tasks)

        # Left and right frame
        self.left_frame = customtkinter.CTkFrame(
            self,
            width=width / 2 - 20,
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
            width=width / 2 - 20,
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

        self.left_option_menu = customtkinter.CTkOptionMenu(
            self,
            values=[x for x in self.titles],
            anchor=CENTER,
            width=300
        )

        # self.left_option_menu.set(titles[0].title)
        self.left_option_menu.place(
            x=20,
            y=20
        )

        check_var = customtkinter.StringVar(value="False")
        self.left_checkbox_search = customtkinter.CTkCheckBox(
            self,
            text="Search completed",
            variable=check_var,
            onvalue="True",
            offvalue="False",
            bg_color="black"
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
            width=width / 2 - 40,
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
            command=lambda: self.update_data()
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
            command=lambda: self.delete()
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
        self.option_menu_var.trace_add('write', self.update)

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
            width=100
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
            width=width / 2 - 40,
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
            command=lambda: self.insert()
        )

        self.left_button_delete.place(
            x=875,
            y=650
        )

    def update(self, *args):
        selected_option = self.option_menu_var.get()
        self.current_id = self.get_task_by_title(selected_option, self.tasks)
        self.left_entry.delete(0, customtkinter.END)
        self.left_entry.insert(
            index=0,
            string=selected_option
        )
        self.left_textbox.delete('1.0', customtkinter.END)
        self.left_textbox.insert('1.0', text=self.descriptions[self.ids.index(self.current_id)])
        self.left_entry_date.delete(0, customtkinter.END)
        self.left_entry_date.insert(0, self.deadlines[self.ids.index(self.current_id)])

    def get_task_by_title(self, title, tasks):
        for task in tasks:
            if task.title == title:
                return task.task_id

        return None

    def all_titles(self, tasks):
        return [task.title for task in tasks]

    def all_descriptions(self, tasks):
        return [task.description for task in tasks]

    def all_deadlines(self, tasks):
        return [task.due_date for task in tasks]

    def all_compleded(self, tasks):
        return [task.completed for task in tasks]

    def all_id(self, tasks):
        return [task.task_id for task in tasks]

    def update_all_attributes(self):
        self.tasks = select_all_data()
        self.tasks = select_all_data()
        self.titles = self.all_titles(self.tasks)
        self.descriptions = self.all_descriptions(self.tasks)
        self.deadlines = self.all_deadlines(self.tasks)
        self.completed = self.all_compleded(self.tasks)
        self.ids = self.all_id(self.tasks)
        self.left_option_menu.configure(values=[x for x in self.titles])

    def update_data(self):
        new_title = self.left_entry.get()
        new_description = self.left_textbox.get('1.0', customtkinter.END).strip()
        new_date = self.left_entry_date.get()
        new_completed = True if self.left_checkbox.get() == 'True' else False
        update_data(self.current_id, new_title, new_description, new_date, new_completed)
        print(self.current_id)
        self.update_all_attributes()

    def insert(self):
        title = self.right_entry.get()
        description = self.right_textbox.get('1.0', customtkinter.END).strip()
        deadline = self.right_entry_date.get()
        insert_data(title, description, deadline)
        self.update_all_attributes()

    def delete(self):
        delete_record(self.current_id )
        self.update_all_attributes()

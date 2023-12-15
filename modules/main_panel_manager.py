import customtkinter

from database.create_database import select_all_data, update_data, insert_data, delete_record


def get_task_by_title(title, tasks):
    for task in tasks:
        if task.title == title:
            return task.task_id
    return None


def all_titles(tasks):
    return [task.title for task in tasks]


def all_descriptions(tasks):
    return [task.description for task in tasks]


def all_deadlines(tasks):
    return [task.due_date for task in tasks]


def all_completed(tasks):
    return [task.completed for task in tasks]


def all_id(tasks):
    return [task.task_id for task in tasks]


class AppManager:
    def __init__(self, master):
        self.master = master

    def update_all_attributes(self):
        self.master.tasks = select_all_data()
        self.master.titles = all_titles(self.master.tasks)
        self.master.descriptions = all_descriptions(self.master.tasks)
        self.master.deadlines = all_deadlines(self.master.tasks)
        self.master.completed = all_completed(self.master.tasks)
        self.master.ids = all_id(self.master.tasks)
        self.master.left_option_menu.configure(values=[x for x in self.master.titles])

    def update(self, *args):
        selected_option = self.master.option_menu_var.get()
        self.current_id = self.master.data_manager.get_task_by_title(selected_option, self.master.tasks)
        self.master.left_entry.delete(0, customtkinter.END)
        self.master.left_entry.insert(
            index=0,
            string=selected_option
        )
        self.master.left_textbox.delete('1.0', customtkinter.END)
        self.master.left_textbox.insert('1.0', text=self.master.descriptions[self.master.ids.index(self.current_id)])
        self.master.left_entry_date.delete(0, customtkinter.END)
        self.master.left_entry_date.insert(0, self.master.deadlines[self.master.ids.index(self.current_id)])

    def update_menu(self, list_of_titles):
        self.master.left_option_menu.configure(values=[x for x in list_of_titles])

    def update_data(self):
        new_title = self.master.left_entry.get()
        new_description = self.master.left_textbox.get('1.0', customtkinter.END).strip()
        new_date = self.master.left_entry_date.get()
        new_completed = True if self.master.left_checkbox.get() == 'True' else False
        update_data(self.current_id, new_title, new_description, new_date, new_completed)
        self.master.data_manager.update_all_attributes()

    def insert(self):
        title = self.master.right_entry.get()
        description = self.master.right_textbox.get('1.0', customtkinter.END).strip()
        deadline = self.master.right_entry_date.get()
        insert_data(title, description, deadline)
        self.master.data_manager.update_all_attributes()

    def delete(self):
        delete_record(self.current_id)
        self.master.data_manager.update_all_attributes()

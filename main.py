from database.create_database import initialize_database, select_all_data, insert_data
from view_models.main_panel import App

if __name__ == "__main__":
    initialize_database()
    app = App()
    app.mainloop()

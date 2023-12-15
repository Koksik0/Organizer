from datetime import datetime

import dateutil.utils
from sqlalchemy import create_engine, Column, Integer, String, DATE, BOOLEAN, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database/database.db', echo=True)

Base = declarative_base()


class Tasks(Base):
    __tablename__ = 'tasks'
    task_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True)
    description = Column(String)
    due_date = Column(DATE)
    completed = Column(BOOLEAN)


def initialize_database():
    Base.metadata.create_all(engine, checkfirst=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def select_all_data():
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        tasks = session.query(Tasks).all()
        return tasks
    except Exception as e:
        print(f"Select error: {e}")
    finally:
        session.close()


def insert_data(title, description, date):
    Session = sessionmaker(bind=engine)
    session = Session()

    try:

        new_task = Tasks(
            title=title,
            description=description,
            due_date=datetime.strptime(date, "%Y-%m-%d"),
            completed=False
        )
        session.add(new_task)
        session.commit()

    except Exception as e:
        print(f"Insert error: {e}")
        session.rollback()

    finally:
        session.close()


def update_data(task_id, new_title, new_description, new_date, new_completed):
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Zaktualizuj dane w bazie danych
        session.execute(
            update(Tasks)
            .where(Tasks.task_id == task_id)
            .values(
                title=new_title,
                description=new_description,
                due_date=datetime.strptime(new_date, "%Y-%m-%d"),
                completed=new_completed
            )
        )
        session.commit()

    except Exception as e:
        print(f"Błąd podczas aktualizacji danych: {e}")
        session.rollback()

    finally:
        session.close()


def delete_record(id):
    Session = sessionmaker(bind=engine)
    session = Session()
    record_to_delete = session.query(Tasks).get(id)
    session.delete(record_to_delete)
    session.commit()

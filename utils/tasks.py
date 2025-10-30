import sqlite3

class Database:
    def __init__(self, database_name="tasks.db"):
        self.connect = sqlite3.connect(database_name)
        self.cursor = self.connect.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        title TEXT,
        description TEXT
        )
                        """)
        self.connect.commit()

    def create_task(self, title, description):
        self.cursor.execute("""
        INSERT INTO tasks (title, description)
        VALUES (?, ?)
                       """,
        (str(title), str(description)))
        self.connect.commit()

    def close_task(self, id):
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (id,))
        self.connect.commit()
        print(f"aqui chegou id = {id}")

    def show_tasks(self):
        self.cursor.execute("SELECT * FROM tasks")
        return self.cursor.fetchall()













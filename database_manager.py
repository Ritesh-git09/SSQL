import sqlite3

import sqlite3

class DatabaseManager:
    def __init__(self, db_name="school.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS teachers (
                id INTEGER PRIMARY KEY, 
                income INTEGER
            )
        ''')
        self.conn.commit()

    def insert_data(self, teacher_id, income):
        self.cursor.execute("INSERT INTO teachers (id, income) VALUES (?, ?)", (teacher_id, income))
        self.conn.commit()

    def execute_query(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()


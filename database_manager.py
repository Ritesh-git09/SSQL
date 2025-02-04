import sqlite3

class DatabaseManager:
    def __init__(self, db_name, dataset_type):
        self.db_name = db_name
        self.dataset_type = dataset_type
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Creates a table if it does not exist for the dataset."""
        table_definitions = {
            "school": "CREATE TABLE IF NOT EXISTS school (id INTEGER PRIMARY KEY, name TEXT, income INTEGER, section TEXT)",
            "bank": "CREATE TABLE IF NOT EXISTS bank (account_number INTEGER PRIMARY KEY, name TEXT, balance INTEGER, branch TEXT)",
            "employees": "CREATE TABLE IF NOT EXISTS employees (employee_id INTEGER PRIMARY KEY, name TEXT, salary INTEGER, department TEXT)"
        }
        query = table_definitions.get(self.dataset_type, None)
        if query:
            self.cursor.execute(query)
            self.conn.commit()

    def column_exists(self, column_name):
        """Check if a column exists in the table."""
        self.cursor.execute(f"PRAGMA table_info({self.dataset_type})")
        columns = [col[1] for col in self.cursor.fetchall()]
        return column_name in columns

    def insert_data(self, data):
        """Insert extracted data into the database."""
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?"] * len(data))
        values = tuple(data.values())

        # **Check if all extracted attributes exist in the table**
        for column in data.keys():
            if not self.column_exists(column):
                print(f"⚠️ Column '{column}' does not exist in table '{self.dataset_type}'. Skipping insertion.")
                return

        query = f"INSERT INTO {self.dataset_type} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(query, values)
        self.conn.commit()

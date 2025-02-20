import os
import sqlite3

class DatabaseManager:
    def __init__(self, db_name="voice_db.db"):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def auto_detect_schema(self, extracted_data):
        """Automatically detect and create/update table schema based on extracted attributes."""
        if not extracted_data:
            print("⚠️ No valid data extracted to determine schema.")
            return None

        table_name = "dynamic_table"  # Generic table name for all datasets
        columns = ", ".join([f"{key} TEXT" for key in extracted_data.keys()])
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, {columns})"
        
        try:
            self.cursor.execute(create_table_query)
            self.connection.commit()
            print(f"✅ Table `{table_name}` ready with schema: {list(extracted_data.keys())}")
            return table_name
        except sqlite3.Error as e:
            print(f"❌ Error creating table: {e}")
            return None

    def insert_data(self, extracted_data):
        """Insert data into the dynamically detected schema."""
        table_name = self.auto_detect_schema(extracted_data)
        if not table_name:
            return
        
        columns = ", ".join(extracted_data.keys())
        placeholders = ", ".join(["?" for _ in extracted_data])
        values = tuple(extracted_data.values())

        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        try:
            self.cursor.execute(insert_query, values)
            self.connection.commit()
            print("✅ Data inserted successfully.")
        except sqlite3.Error as e:
            print(f"❌ Error inserting data: {e}")

    def execute_query(self, query):
        """Execute a SQL query and display results."""
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            if results:
                for row in results:
                    print(row)
            else:
                print("✅ Query executed successfully, but no results found.")
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"❌ SQL Error: {e}")

    def reset_database(self):
        """Reset the database after user confirmation."""
        confirmation = input("⚠️ Are you sure you want to reset the database? This will delete all stored data. (yes/no): ").strip().lower()
        if confirmation == "yes":
            if os.path.exists(self.db_name):
                os.remove(self.db_name)
                print(f"✅ Database {self.db_name} has been reset.")
            else:
                print(f"⚠️ Database {self.db_name} does not exist.")
        else:
            print("❌ Database reset cancelled.")

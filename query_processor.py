from speech_to_text import SpeechToText
import sqlite3

class QueryProcessor:
    def __init__(self, db_manager):
        self.db_manager = db_manager
    
    def insert_data(self, extracted_data):
        if not extracted_data:
            print("⚠️ Could not extract enough information.")
            return
        
        try:
            self.db_manager.insert_data(self.db_manager.dataset_type, extracted_data)
        except Exception as e:
            print(f"❌ Error inserting data: {e}")
    
    def execute_query(self):
        print("Speak your query.")
        query_text = input("Enter your SQL query: ").strip().lower()
        
        if query_text.startswith("select"):
            self.run_query(query_text)
        elif query_text.startswith(("insert", "update", "delete")):
            confirmation = input("⚠️ This query modifies data. Do you want to proceed? (yes/no): ").strip().lower()
            if confirmation == "yes":
                self.run_query(query_text, modify=True)
            else:
                print("❌ Query execution cancelled.")
        else:
            print("⚠️ Only SELECT, INSERT, UPDATE, and DELETE queries are allowed.")
    
    def run_query(self, query_text, modify=False):
        try:
            query_result = self.db_manager.execute_query(query_text)
            if modify:
                print("✅ Query executed successfully.")
            elif query_result:
                for row in query_result:
                    print(row)
            else:
                print("⚠️ No matching records found.")
        except Exception as e:
            print(f"❌ Error executing query: {e}")

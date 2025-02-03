from database_manager import DatabaseManager
from nlp_processor import NLPProcessor
from query_processor import QueryProcessor

def main():
    db_manager = DatabaseManager()
    nlp_processor = NLPProcessor()
    query_processor = QueryProcessor(db_manager, nlp_processor)

    while True:
        print("\nChoose an option:")
        print("1. Insert Data")
        print("2. Execute Query")
        print("3. Exit")

        choice = input("Enter choice: ")
        
        if choice == "1":
            query_processor.insert_data()
        elif choice == "2":
            query_processor.execute_query()
        elif choice == "3":
            save_option = input("Do you want to save the database? (yes/no): ")
            if save_option.lower() == "no":
                db_manager.cursor.execute("DROP TABLE IF EXISTS teachers")
                db_manager.conn.commit()
                print("Database erased.")
            db_manager.close_connection()
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

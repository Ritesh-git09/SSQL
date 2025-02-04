from database_manager import DatabaseManager
from nlp_processor import NLPProcessor
from query_processor import QueryProcessor
from speech_to_text import SpeechToText

def main():
    # ✅ Choose dataset type dynamically
    dataset_type = input("Choose dataset type (school/bank/business): ").strip().lower()
    db_name = f"{dataset_type}.db"

    # ✅ Initialize required components
    db_manager = DatabaseManager(db_name, dataset_type)
    nlp_processor = NLPProcessor()
    query_processor = QueryProcessor(db_manager, nlp_processor)

    while True:
        print("\nChoose an option:")
        print("1. Insert Data")
        print("2. Execute Query")
        print("3. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            query_processor.insert_data()
        elif choice == "2":
            query_processor.execute_query()  # ✅ Now properly calling execute_query
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

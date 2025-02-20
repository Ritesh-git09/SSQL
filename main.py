from database_manager import SpeechToText
from nlp_processor import NLPProcessor  # ✅ Import NLP for text processing
import sqlite3

def main():
    speech_to_text = SpeechToText()
    nlp_processor = NLPProcessor()  # ✅ Initialize NLPProcessor

    while True:
        print("\nChoose an option:")
        print("1. Insert Data")
        print("2. Execute Query")
        print("3. Reset Database")
        print("4. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            print("Speak the details to insert.")
            for spoken_text in speech_to_text.continuous_listen():
                extracted_data = nlp_processor.extract_attributes(spoken_text)  # ✅ Process input
                if extracted_data:
                    print(f"Extracted Data: {extracted_data}")
                    # TODO: Implement auto-schema detection and insert logic
                else:
                    print("⚠️ Could not extract enough information.")

        elif choice == "2":
            print("Speak your SQL query.")
            for spoken_text in speech_to_text.continuous_listen():
                speech_to_text.execute_query(spoken_text)

        elif choice == "3":
            speech_to_text.reset_database()

        elif choice == "4":
            print("👋 Exiting program.")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

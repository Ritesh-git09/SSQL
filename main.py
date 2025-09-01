from database_manager import DatabaseManager
from intent_detector import IntentDetector
from nlp_processor import NLPProcessor
import time

def get_valid_input(prompt, speech_to_text):
    """ Keep asking for voice input until a valid response is received. """
    while True:
        print(prompt)
        response = speech_to_text.listen()
        if response:
            return response
        print("⚠️ Could not understand. Please try again.")

def main():
    print("🗄️ Voice-Activated SQL System")

    # Initialize required classes
    db_manager = DatabaseManager()  # Initialize database manager
    intent_detector = IntentDetector()  # Initialize intent detector
    nlp_processor = NLPProcessor()  # Initialize NLP processor
    
    while True:
        print("\nChoose an option:")
        print("1. Insert Data")
        print("2. Execute Query")
        print("3. Reset Database")
        print("4. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            print("🎤 Let's insert data!")
            spoken_text = get_valid_input("Speak the details to insert (name, income, etc.):", db_manager.speech_to_text)
            
            # Detect intent
            intent = intent_detector.detect_intent(spoken_text)
            if intent == "insert":
                # Extract entities (like name, income, etc.)
                extracted_data = nlp_processor.extract_entities(spoken_text)
                
                if extracted_data:
                    # Get category (school, bank, etc.) from the user
                    category = input("Enter category (e.g., school, bank, business): ").strip().lower()
                    db_manager.insert_data(category, extracted_data)
                    print("✅ Data inserted successfully.")
                else:
                    print("⚠️ Could not extract necessary data for insertion.")
            else:
                print("⚠️ Could not detect an insertion intent.")

        elif choice == "2":
            query = get_valid_input("🎤 Speak your SQL query:", db_manager.speech_to_text)
            db_manager.execute_query(query)

        elif choice == "3":
            db_manager.reset_database()

        elif choice == "4":
            print("👋 Exiting program...")
            db_manager.speech_to_text.speak("Exiting program")
            time.sleep(1)
            break

        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

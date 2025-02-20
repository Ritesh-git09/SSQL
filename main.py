from database_manager import DatabaseManager
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
    
    db_manager = DatabaseManager()  # Initialize database manager
    
    while True:
        print("\nChoose an option:")
        print("1. Insert Data")
        print("2. Execute Query")
        print("3. Reset Database")
        print("4. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            category = input("Enter category (e.g., school, bank, business): ").strip().lower()
            name = get_valid_input("🎤 Speak the name:", db_manager.speech_to_text)
            details = get_valid_input("🎤 Speak the details:", db_manager.speech_to_text)
            db_manager.insert_data(category, name, details)
        
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

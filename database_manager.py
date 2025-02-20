import speech_recognition as sr
import os
import sqlite3
import pyttsx3  # Text-to-Speech

class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 300  
        self.engine = pyttsx3.init()  # Initialize TTS

    def speak(self, text):
        """Speak out the given text."""
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        """Listen for user input via microphone."""
        with sr.Microphone() as source:
            print("\U0001F3A4 Listening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            try:
                audio = self.recognizer.listen(source, timeout=5)
                text = self.recognizer.recognize_google(audio).lower()
                print(f"✅ Recognized: {text}")
                return text
            except sr.UnknownValueError:
                print("⚠️ Could not understand the audio. Please try again.")
                self.speak("I could not understand. Please repeat.")
                return None
            except sr.RequestError:
                print("❌ Speech recognition service is unavailable.")
                return None
            except sr.WaitTimeoutError:
                print("⌛ No speech detected. Please try again.")
                return None

    def continuous_listen(self):
        """Continuously listen for commands until user says 'exit'."""
        print("🎤 Continuous listening mode activated. Say 'exit' to stop.")
        self.speak("Continuous listening activated. Say 'exit' to stop.")
        while True:
            spoken_text = self.listen()
            if spoken_text:
                if "exit" in spoken_text:
                    print("👋 Exiting continuous listening mode.")
                    self.speak("Exiting continuous listening mode.")
                    break
                yield spoken_text

class DatabaseManager:
    def __init__(self, db_name="voice_db.db"):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.speech_to_text = SpeechToText()  # Initialize speech system
        self.initialize_database()

    def initialize_database(self):
        """Create a general table if not exists."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT,
                name TEXT,
                details TEXT
            )
        ''')
        self.connection.commit()

    def insert_data(self, category, name, details):
        """Insert data into database."""
        self.cursor.execute("INSERT INTO records (category, name, details) VALUES (?, ?, ?)", 
                            (category, name, details))
        self.connection.commit()
        print(f"✅ Data inserted: {category}, {name}, {details}")
        self.speech_to_text.speak("Data inserted successfully.")

    def execute_query(self):
        """Listen for a query, process it, and read results aloud."""
        self.speech_to_text.speak("Please say your query.")
        print("🎤 Say your SQL query...")
        query = self.speech_to_text.listen()

        if not query:
            return
        
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            
            if results:
                print("🔹 Query Results:")
                for row in results:
                    print(row)
                    self.speech_to_text.speak(f"Result: {row}")
            else:
                print("✅ Query executed successfully, but no results found.")
                self.speech_to_text.speak("Query executed successfully, but no results found.")
            
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"❌ SQL Error: {e}")
            self.speech_to_text.speak(f"SQL Error: {e}")

    def reset_database(self):
        """Reset the database by deleting all records."""
        confirmation = input("⚠️ Are you sure you want to reset the database? (yes/no): ").strip().lower()
        if confirmation == "yes":
            self.cursor.execute("DROP TABLE IF EXISTS records")
            self.initialize_database()
            print("✅ Database has been reset.")
            self.speech_to_text.speak("Database has been reset.")
        else:
            print("❌ Database reset cancelled.")
            self.speech_to_text.speak("Database reset cancelled.")

    def close_connection(self):
        """Close the database connection."""
        self.connection.close()

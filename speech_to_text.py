import speech_recognition as sr
import os

class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 300  # Adjust for noise handling

    def listen(self):
        with sr.Microphone() as source:
            print("🎤 Listening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            try:
                audio = self.recognizer.listen(source, timeout=5)
                text = self.recognizer.recognize_google(audio).lower()
                print(f"✅ Recognized: {text}")
                return text
            except sr.UnknownValueError:
                print("⚠️ Could not understand the audio. Please try again.")
                return None
            except sr.RequestError:
                print("❌ Speech recognition service is unavailable.")
                return None
            except sr.WaitTimeoutError:
                print("⌛ No speech detected. Please try again.")
                return None

    def continuous_listen(self):
        print("🛑 Say 'exit' to stop listening.")
        while True:
            spoken_text = self.listen()
            if spoken_text:
                if "exit" in spoken_text:
                    print("🛑 Exiting continuous listening mode.")
                    break
                yield spoken_text

    def reset_database(self, db_name="voice_db.db"):
        confirmation = input("⚠️ Are you sure you want to reset the database? This will delete all stored data. (yes/no): ").strip().lower()
        if confirmation == "yes":
            if os.path.exists(db_name):
                os.remove(db_name)
                print(f"✅ Database {db_name} has been reset.")
            else:
                print(f"⚠️ Database {db_name} does not exist.")
        else:
            print("❌ Database reset cancelled.")

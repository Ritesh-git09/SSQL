import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def get_speech_input(self):
        with self.microphone as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        try:
            text = self.recognizer.recognize_google(audio)
            print(f"Recognized: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, could not understand the speech.")
        except sr.RequestError:
            print("Speech recognition service is unavailable.")
        return None

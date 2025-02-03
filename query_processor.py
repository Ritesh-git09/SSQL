import sqlite3
from speech_to_text import SpeechToText
from speech_to_text import SpeechToText

class QueryProcessor:
    def __init__(self, db_manager, nlp_processor):
        self.db_manager = db_manager
        self.nlp_processor = nlp_processor
        self.speech_recognizer = SpeechToText()

    def insert_data(self):
        print("Speak the details to insert. Example: 'I am a teacher, ID 101, income 50000'")
        speech = self.speech_recognizer.get_speech_input()
        if speech:
            entities = self.nlp_processor.extract_entities(speech)
            print("Extracted entities:", entities)
            if len(entities) >= 2:
                teacher_id = entities[0][0]
                income = entities[1][0]
                self.db_manager.insert_data(teacher_id, income)
                print("Data inserted successfully.")
            else:
                print("Could not extract enough information.")

    def execute_query(self):
        print("Speak your query. Example: 'Fetch details of teacher with ID 101'")
        speech = self.speech_recognizer.get_speech_input()
        if speech:
            entities = self.nlp_processor.extract_entities(speech)
            print("Extracted entities:", entities)
            if len(entities) >= 1:
                teacher_id = entities[0][0]
                result = self.db_manager.execute_query("SELECT * FROM teachers WHERE id = ?", (teacher_id,))
                if result:
                    print("Query result:", result)
                else:
                    print("No matching records found.")
            else:
                print("Could not extract enough information.")

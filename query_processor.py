from speech_to_text import SpeechToText

class QueryProcessor:
    def __init__(self, db_manager, nlp_processor):
        self.db_manager = db_manager
        self.nlp_processor = nlp_processor

    def insert_data(self):
        print("Speak the details to insert.")
        speech = SpeechToText().get_speech_input()
        if speech:
            extracted_data = self.nlp_processor.process_insert_command(speech, self.db_manager.dataset_type)
            print("Extracted Data:", extracted_data)
            
            if extracted_data:
                self.db_manager.insert_data(extracted_data)
                print("✅ Data inserted successfully.")
            else:
                print("⚠️ Could not extract enough information.")

    def execute_query(self):
        """Allows the user to ask a query using speech and retrieves matching data."""
        print("Speak your query.")
        speech = SpeechToText().get_speech_input()

        if speech:
            extracted_data = self.nlp_processor.process_query_command(speech, self.db_manager.dataset_type)
            print("Extracted Query Data:", extracted_data)

            if "id" in extracted_data:
                query = f"SELECT * FROM {self.db_manager.dataset_type} WHERE id = ?"
                result = self.db_manager.execute_query(query, (extracted_data["id"],))

                if result:
                    print("🔍 Query Result:", result)
                else:
                    print("⚠️ No matching records found.")
            else:
                print("⚠️ Could not extract enough information to perform query.")

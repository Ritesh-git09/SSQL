import spacy

class NLPProcessor:
    def __init__(self):
        # Load the small English model for spaCy NLP processing
        self.nlp = spacy.load("en_core_web_sm")

    def extract_entities(self, text):
        """ Extract entities like 'name', 'id', 'income' from the spoken text. """
        doc = self.nlp(text)
        extracted_data = {}

        # Extracting Named Entities
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                extracted_data["name"] = ent.text
            elif ent.label_ == "MONEY":
                extracted_data["income"] = ent.text
            elif ent.label_ == "CARDINAL":
                extracted_data["id"] = ent.text
        
        # If no entity found, print warning
        if not extracted_data:
            print("⚠️ Could not extract any named entities. Please speak clearly.")
        
        return extracted_data

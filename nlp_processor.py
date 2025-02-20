import spacy

class NLPProcessor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def extract_attributes(self, text):
        doc = self.nlp(text.lower())
        extracted_data = {}

        # Rule-based extraction for different attributes
        name = None
        entity_id = None
        income = None

        for ent in doc.ents:
            if ent.label_ == "PERSON":
                name = ent.text
            elif ent.label_ == "MONEY" or "income" in ent.text:
                income = ent.text
            elif ent.label_ == "CARDINAL":
                entity_id = ent.text

        # Store extracted values
        if name:
            extracted_data["name"] = name
        if entity_id:
            extracted_data["id"] = entity_id
        if income:
            extracted_data["income"] = income

        return extracted_data if extracted_data else None

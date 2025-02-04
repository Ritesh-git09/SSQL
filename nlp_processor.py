import spacy
import re

class NLPProcessor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def process_insert_command(self, speech, dataset_type):
        """Extracts structured attributes from speech input."""
        doc = self.nlp(speech)
        extracted_data = {}

        # Define dataset-specific attributes
        dataset_attributes = {
            "school": ["name", "id", "income", "section"],
            "bank": ["name", "account_number", "balance", "branch"],
            "employees": ["name", "employee_id", "salary", "department"]
        }

        # Select attributes based on dataset type
        attributes = dataset_attributes.get(dataset_type, [])

        # **Extract numbers manually (for ID, income, salary, etc.)**
        numbers = re.findall(r'\d+', speech)

        # **Extract name separately**
        name_match = re.search(r'named (\w+)', speech, re.IGNORECASE)
        if name_match:
            extracted_data["name"] = name_match.group(1)

        # **Assign numerical values to known attributes**
        num_attributes = ["id", "income", "salary", "account_number", "balance"]
        for num in numbers:
            for attr in num_attributes:
                if attr not in extracted_data:
                    extracted_data[attr] = num
                    break  # Assign each number to one attribute

        return extracted_data if extracted_data else None

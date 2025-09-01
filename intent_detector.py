import re

class IntentDetector:
    def detect_intent(self, text):
        text = text.lower()

        # Keywords indicating insertion
        insert_keywords = ["add", "insert", "register", "store", "save", "record", "i am", "my name is"]
        # Keywords indicating SQL query
        query_keywords = ["select", "show", "display", "what", "how many", "list", "retrieve", "find"]

        for keyword in insert_keywords:
            if keyword in text:
                return "insert"
        for keyword in query_keywords:
            if keyword in text:
                return "query"
        
        return "unknown"

    def detect_category(self, text):
        text = text.lower()
        if "school" in text or "teacher" in text or "student" in text:
            return "school"
        elif "bank" in text or "account" in text or "transaction" in text:
            return "bank"
        elif "business" in text or "client" in text or "project" in text:
            return "business"
        else:
            return "general"  # fallback

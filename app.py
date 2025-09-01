import streamlit as st
import sqlite3
from database_manager import DatabaseManager
from intent_detector import IntentDetector
from nlp_processor import NLPProcessor
import pyttsx3

# Initialize components
db_manager = DatabaseManager()
intent_detector = IntentDetector()
nlp_processor = NLPProcessor()
engine = pyttsx3.init()

# --- Streamlit UI ---
st.set_page_config(page_title="Voice SQL Assistant", layout="centered")
st.title("🎤 Voice-Activated SQL Assistant")

# Sidebar
st.sidebar.title("⚙️ Options")
reset = st.sidebar.button("Reset Database")

if reset:
    db_manager.reset_database()

# Input type selection
mode = st.radio("Choose input method:", ["📝 Text", "🎙️ Voice"])

query = None

if mode == "📝 Text":
    query = st.text_area("Enter your query or data instruction:")

elif mode == "🎙️ Voice":
    st.info("Voice input coming soon inside Streamlit (limitation: Streamlit doesn't directly support microphone).")
    st.write("For now, please use text input.")

# Execute query
if st.button("Run"):
    if query:
        st.write(f"👉 You said: **{query}**")

        # Detect intent
        intent = intent_detector.detect_intent(query)
        
        if intent == "insert":
            entities = nlp_processor.extract_entities(query)
            if entities:
                db_manager.insert_data("default", str(entities), query)
                st.success("✅ Data inserted successfully!")
                engine.say("Data inserted successfully")
                engine.runAndWait()
            else:
                st.warning("⚠️ Could not extract valid data from your input.")
        
        elif intent == "query":
            results = db_manager.execute_query(query)
            if results:
                st.dataframe(results)
                engine.say("Here are the results")
                engine.runAndWait()
            else:
                st.info("No results found or query executed successfully.")
        
        else:
            st.error("❌ Could not determine intent.")
    else:
        st.warning("⚠️ Please enter a query first.")

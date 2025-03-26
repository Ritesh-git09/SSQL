# Voice-Activated SQL Query System

## 📌 Overview
This project is a **voice-controlled SQL assistant** that allows users to **insert data** and **query databases** using **spoken commands**. The system supports **automatic schema detection**, **natural language processing (NLP)**, and **text-to-speech feedback**.

## 🔥 Features
- 🎤 **Speech-to-Text (STT)**: Converts spoken input into text.
- 🗃 **Automatic Schema Detection**: Dynamically detects and structures data.
- 🏛 **Multi-Domain Support**: Handles various datasets (e.g., school, bank, business).
- 📝 **NLP-Powered Query Understanding**: Extracts entities for SQL queries.
- 🔄 **Continuous Listening Mode**: Processes multiple commands until exit.
- 🔊 **Text-to-Speech (TTS)**: Reads out query results and confirmations.
- 🗑 **Database Reset & Management**: Allows resetting or retaining database records.

## 🚀 Getting Started

### 🔧 Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Required Python packages:
  ```bash
  pip install speechrecognition pyaudio sqlite3 spacy pyttsx3
  ```
- Download NLP model for entity extraction:
  ```bash
  python -m spacy download en_core_web_sm
  ```

### 🛠 Setup & Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/voice-sql-assistant.git
   cd voice-sql-assistant
   ```
2. Run the main script:
   ```bash
   python main.py
   ```
3. Follow voice instructions to **insert data** or **run queries**.
4. Say **"exit"** to stop continuous listening mode.

## 🏗 Project Structure
```
voice-sql-assistant/
│── main.py                 # Main entry point
│── database_manager.py      # Handles database operations
│── nlp_processor.py        # Extracts relevant data using NLP
│── speech_to_text.py       # Converts speech to text
│── README.md               # Documentation
```

## 🛠 Future Enhancements
- 🤖 **Advanced NLP**: Improved entity recognition for better query formation.
- 🏢 **Cloud Database Support**: Integration with PostgreSQL/MySQL/Firebase.
- 🌍 **Web Interface**: Convert project into a web-based application.
- ⚡ **AI-Optimized Queries**: Faster execution with caching and query analysis.

## 📜 License
This project is licensed under the MIT License.

---
🔹 **Contributors & Feedback**: Feel free to contribute or suggest improvements!


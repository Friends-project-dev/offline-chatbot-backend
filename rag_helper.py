import json
import sqlite3
import difflib

# Load intents from JSON
def load_intents(path="intent_rag.json"):
    with open(path, "r") as f:
        return json.load(f)

# Fuzzy match using difflib
def get_sql_for_question(user_question, intents):
    questions = [item["question"] for item in intents]
    match = difflib.get_close_matches(user_question.lower(), questions, n=1, cutoff=0.4)
    if match:
        for item in intents:
            if item["question"] == match[0]:
                return item["sql"]
    return None

# Execute SQL on SQLite
def execute_sql_query(sql):
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.close()
    return result

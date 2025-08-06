import json
import sqlite3
import difflib

def load_intents(path="intent_rag.json"):
    with open(path, "r") as f:
        return json.load(f)

def get_response_or_sql(user_question, intents):
    questions = [item["question"] for item in intents]
    match = difflib.get_close_matches(user_question.lower(), questions, n=1, cutoff=0.4)
    if match:
        for item in intents:
            if item["question"] == match[0]:
                if "response" in item:
                    return {"type": "response", "data": item["response"]}
                elif "sql" in item:
                    return {"type": "sql", "data": item["sql"]}
    return None

def execute_sql_query(sql):
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.close()
    return result

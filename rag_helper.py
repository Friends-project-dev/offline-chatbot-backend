import sqlite3
import chromadb
from chromadb.config import Settings

# Sample query-document mapping
docs = [
    {"question": "gross sales today", "sql": "SELECT SUM(total) as gross_sales FROM sales WHERE date = DATE('now');"},
    {"question": "number of orders today", "sql": "SELECT COUNT(*) FROM sales WHERE date = DATE('now');"},
    {"question": "top 5 products", "sql": "SELECT product, SUM(quantity) as qty FROM sales GROUP BY product ORDER BY qty DESC LIMIT 5;"}
]

# Initialize ChromaDB in-memory or local dir
client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory="./chroma_db"))

collection = client.get_or_create_collection("intent_to_sql")

def load_documents():
    for doc in docs:
        collection.add(
            documents=[doc["question"]],
            metadatas=[{"sql": doc["sql"]}],
            ids=[doc["question"]]
        )

def get_sql_for_question(question):
    results = collection.query(query_texts=[question], n_results=1)
    if results["metadatas"][0]:
        return results["metadatas"][0][0]["sql"]
    return None

def execute_sql_query(sql):
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.close()
    return result

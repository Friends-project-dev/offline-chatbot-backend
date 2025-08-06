import streamlit as st
from rag_helper import load_documents, get_sql_for_question, execute_sql_query

st.title("🧠 Offline Chatbot with SQL + ChromaDB")

user_input = st.text_input("Ask a question:")

# Load ChromaDB on first run
if "loaded" not in st.session_state:
    load_documents()
    st.session_state.loaded = True

if user_input:
    sql = get_sql_for_question(user_input)
    st.write(f"📜 SQL Query: `{sql}`" if sql else "No SQL found for your question.")
    
    if sql:
        result = execute_sql_query(sql)
        st.success("✅ Query Result:")
        st.write(result)


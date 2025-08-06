import streamlit as st
from rag_helper import load_intents, get_sql_for_question, execute_sql_query

st.title("🧠 Offline Chatbot (JSON + SQLite)")

user_input = st.text_input("Ask a question:")

# Load intents once
if "intents" not in st.session_state:
    st.session_state.intents = load_intents()

if user_input:
    sql = get_sql_for_question(user_input, st.session_state.intents)
    if sql:
        st.code(sql, language="sql")
        result = execute_sql_query(sql)
        st.success("✅ Result:")
        st.write(result)
    else:
        st.warning("❌ No matching question found.")

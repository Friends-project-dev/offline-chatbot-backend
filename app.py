import streamlit as st
from rag_helper import load_intents, get_response_or_sql, execute_sql_query

st.title("🧠 Offline Chatbot (JSON + SQLite)")

user_input = st.text_input("Ask a question:")

# Load intents once
if "intents" not in st.session_state:
    st.session_state.intents = load_intents()

if user_input:
    match = get_response_or_sql(user_input, st.session_state.intents)
    
    if match:
        if match["type"] == "response":
            st.success(match["data"])  # humanised message
        elif match["type"] == "sql":
            st.code(match["data"], language="sql")
            result = execute_sql_query(match["data"])
            st.success("✅ Result:")
            st.write(result)
    else:
        st.warning("❌ Sorry, I didn't understand that. Try asking in a different way.")

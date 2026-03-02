import os
import re
import pandas as pd
import streamlit as st
from langchain_community.utilities import SQLDatabase
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

# Page Setup
st.set_page_config(page_title="Text-to-SQL App",layout="centered")
st.title("📊 Talk to Your Database")
st.write("Ask questions about the student grades database in plain English.")

# Database Connection
db = SQLDatabase.from_uri("sqlite:///student_grade.db")

# Local LLM (ollama)
llm = ChatOllama(
    model="gemma3:1b",
    temperature=0,
    base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
)

# Prompt (LCEL)
prompt = ChatPromptTemplate.from_template("""
    You are a senior data analyst and SQL expert.
    Given the database schema below, write a correct SQL query that answers the user's question.
    
    Rules:
    - Use only the tables and columns in the schema
    - Do NOT explain anything
    - Return ONLY the SQL query
    
    Schema:
    {schema}
    Question: 
    {question}

""")

# LCEL Runnable Pipeline
sql_chain= (
    prompt
    | llm
    | StrOutputParser()
)
schema= db.get_table_info()

# UI Input
question = st.text_input(
    "Enter your question: ",
    placeholder= "e.g Who scored the highest in History?"
)
# Execution
if question:
    try:
        sql_query= sql_chain.invoke(
            {"schema":schema, "question":question}
        ).strip()
        # Remove markdown code blocks
        sql_query = re.sub(r"```.*?\n", "", sql_query)
        sql_query = sql_query.replace("```", "").strip()
        st.subheader("🧠 Generated SQL")
        st.code(sql_query,language="sql")
        st.subheader("📈 Result")
        df = pd.read_sql_query(sql_query,db._engine)
        st.dataframe(df)
    except Exception as e:
        st.error(f"❌ Error: {e}")
# Footer
st.markdown("---")
st.caption("Powered by LangChain 1.x • Ollama • Gemma • Streamlit")


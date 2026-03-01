
# 📊 AI Text-to-SQL App (Local LLM Powered)

A simple AI-powered **Text-to-SQL application** that allows users to ask questions about a database in plain English and automatically generates and executes SQL queries.

Built using:

* 🧠 Ollama (Local LLM – Gemma 3 1B)
* 🔗 LangChain (LCEL Pipeline)
* 🗄️ SQLite
* 🎨 Streamlit

Everything runs **fully locally** — no OpenAI API, no external cloud.

---

## 🚀 What We Built

This application:

1. Accepts natural language questions from the user
2. Converts the question into a valid SQL query using a local LLM
3. Executes the query on a SQLite database
4. Displays the result in a formatted table

Example:

**Input:**

```
Who scored the highest in Math?
```

**Generated SQL:**

```sql
SELECT name FROM grades WHERE subject = 'Math' ORDER BY score DESC LIMIT 1;
```

**Output:**

| name |
| ---- |
| Amit |

---

## 🧠 How It Works

User Question
↓
LangChain Prompt Template
↓
Local LLM (Gemma 3 1B via Ollama)
↓
Generated SQL Query
↓
SQLite Execution
↓
Formatted Result in Streamlit

---

## 📂 Project Structure

```
.
├── app.py
├── student_grade.db
├── create_db.py
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain (LCEL)
* Ollama (Gemma 3 1B)
* SQLite
* Pandas

---

## ⚙️ Setup Instructions

### 1️⃣ Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Pull required models:

```bash
ollama pull gemma3:1b
```

---

### 2️⃣ Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Create Database

```bash
python create_db.py
```

---

### 4️⃣ Run the App

```bash
streamlit run app.py
```

---

## ✨ Key Features

* ✅ Fully local LLM (no API cost)
* ✅ Natural language to SQL conversion
* ✅ Structured prompt with schema injection
* ✅ SQL output cleaning (removes markdown formatting)
* ✅ Formatted tabular results
* ✅ Error handling with Streamlit UI
* ✅ Lightweight (works on 8GB RAM)

---

## 🎯 Use Cases

* Learning Text-to-SQL systems
* AI-powered database assistants
* Internal data tools
* AI Data Analyst POC
* Local AI experimentation

---

## 💡 Why This Project Matters

This project demonstrates:

* Practical LLM integration
* LCEL pipeline usage
* Prompt engineering for structured outputs
* Local AI system architecture
* Real-world AI data tooling

---

Built as a local AI experiment combining backend engineering + LLM systems 🚀

---

# 📊 AI Text-to-SQL App (Local LLM + Docker)

A fully local **AI-powered Text-to-SQL application** that converts natural language questions into SQL queries and executes them on a database.

Built using:

* 🧠 Ollama (Gemma 3 1B – runs on host)
* 🔗 LangChain (LCEL pipeline)
* 🗄️ SQLite
* 🎨 Streamlit
* 🐳 Docker & Docker Compose

Everything runs **fully locally** — no OpenAI API, no cloud dependency.

---

## 🚀 What We Built

This application:

1. Accepts natural language questions
2. Converts them into valid SQL queries using a local LLM
3. Executes the query on a SQLite database
4. Displays formatted results in a clean UI

Example:

**Input:**

```
Who scored the highest in Math?
```

**Generated SQL:**

```sql
SELECT name FROM grades 
WHERE subject = 'Math' 
ORDER BY score DESC 
LIMIT 1;
```

**Output:**

| name |
| ---- |
| Amit |

---

## 🧠 System Architecture

```
User (Browser)
      ↓
Streamlit (Docker Container)
      ↓
LangChain LCEL Pipeline
      ↓
Ollama (Running on Host)
      ↓
Gemma 3 1B Model
      ↓
SQLite Database
      ↓
Formatted Result
```

---

## 📂 Project Structure

```
.
├── app.py
├── init_db.py
├── student_grade.db
├── Dockerfile
├── docker-compose.yml
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
* Docker

---

# ⚙️ Setup Instructions

---

## 1️⃣ Install Ollama (Host Machine)

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Pull required model:

```bash
ollama pull gemma3:1b
```

Make Ollama accessible to Docker:

Edit:

```bash
sudo nano /etc/systemd/system/ollama.service
```

Add:

```ini
Environment="OLLAMA_HOST=0.0.0.0"
```

Then:

```bash
sudo systemctl daemon-reload
sudo systemctl restart ollama
```

Verify:

```bash
ss -tulnp | grep 11434
```

Should show:

```
*:11434
```

---

## 2️⃣ Build and Run with Docker

```bash
docker compose up --build
```

Open in browser:

```
http://localhost:8501
```

---

## ✨ Key Features

* ✅ Fully local LLM (no API cost)
* ✅ Dockerized application
* ✅ Ollama host integration
* ✅ Natural language → SQL conversion
* ✅ Schema-aware prompting
* ✅ SQL markdown cleaning
* ✅ Formatted tabular results
* ✅ Error handling in UI
* ✅ Lightweight (runs on 8GB RAM)

---

## 🎯 Use Cases

* Learning Text-to-SQL systems
* AI-powered database assistants
* Local AI experimentation
* Backend + LLM integration practice
* AI Data Analyst prototype

---

## 💡 What This Project Demonstrates

* Practical LLM integration
* LCEL pipeline usage
* Prompt engineering for structured output
* Docker networking (host ↔ container)
* Linux service configuration
* Real-world AI app architecture

---

Built as a local AI engineering experiment combining:

Backend Development + Docker + LLM Systems 🚀

---

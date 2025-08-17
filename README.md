# 🛠️ Natural Language to SQL Generator

This project is a **Natural Language to SQL Query Generator** built with **FastAPI** and **LangChain**.  
It allows users to input queries in plain English (e.g., *"Show me employees with salary greater than 40,000"*) and automatically converts them into valid SQL queries, executes them on a connected database, and returns the results.

---

## 🚀 Features

- 📝 Convert natural language queries into SQL using **LangChain + LLMs (Groq / OpenAI / HuggingFace)**  
- ⚡ Fast and efficient API with **FastAPI**  
- 🔍 Semantic search with **FAISS vector store** for contextual accuracy  
- 📊 Execute SQL queries directly on your database (MySQL / PostgreSQL / SQLite etc.)  
- 🔐 Easy integration with frontend or other backend services  

---

## 📂 Project Structure

```
sql-generator/
│── vactor.py               # Handles FAISS vector DB for similarity search
│── text_to_sql_generator.py # Converts NL queries to SQL using LLMs
│── main.py                  # FastAPI app with endpoints
│── requirements.txt         # Dependencies
│── README.md                # Project documentation
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/sql-generator.git
cd sql-generator
```

### 2️⃣ Create and activate a virtual environment
```bash
python -m venv myenv
# On Windows
myenv\Scripts\activate
# On Linux/Mac
source myenv/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Run the FastAPI server
```bash
uvicorn main:app --reload
```

### Access the API
- Interactive Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  

---

## 📌 Example API Request

**POST** `/ask/`

Request Body:
```json
{
  "query": "Show me employees whose salary is less than 30000"
}
```

Response:
```json
{
  "natural_language_query": "Show me employees whose salary is less than 30000",
  "generated_sql": "SELECT name FROM employee WHERE salary < 30000;",
  "sql_results": [
    ["John"],
    ["Alice"]
  ],
  "semantic_context_matches": [
    "Employee data with salary and department details."
  ]
}
```

---

## 🛠️ Tech Stack

- **FastAPI** → REST API framework  
- **LangChain** → NL → SQL generation pipeline  
- **FAISS** → Semantic search for context  
- **MySQL / SQLite / PostgreSQL** → Database backend  
- **Groq / HuggingFace / OpenAI LLMs** → Query generation  

---

## 📌 Future Improvements
- ✅ Add authentication & role-based access  
- ✅ Improve SQL validation & security  
- ✅ Support multiple databases dynamically  
- ✅ Add Docker support  

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.  

---

## 📜 License
This project is licensed under the MIT License.  
"# langchain-sql-agent" 

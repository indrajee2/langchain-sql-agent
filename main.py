from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from database import Base, engine, SessionLocal
from schemas import QueryRequest, EmployeeCreate
from models import Employee
from text_to_sql_generator import generate_sql_query,model
from vactor_db import vactor_store, vactor_similarity_search

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Dependency: Database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1. Endpoint: Create an employee
@app.post("/employees/")
def create_employee(emp: EmployeeCreate, db: Session = Depends(get_db)):
    new_emp = Employee(
        name=emp.name,
        age=emp.age,
        salary=emp.salary,
        department=emp.department
    )
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return {"message": "New employee created successfully."}

# 2. Endpoint: Upload documents to FAISS vector store
@app.post("/upload-docs/")
async def upload_docs(db:Session=Depends(get_db)):
    try:
        employees=db.query(Employee).all()
        docs = []

    # Example: Convert Employee table rows to sentences
   
        for emp in employees:
            text = f"{emp.name} is {emp.age} years old, works in department{emp.department}, and earns a salary of {emp.salary}."
            docs.append(text)
        vactor_store(docs)
        return {"message": "Vector store created successfully."}
    except Exception as e:
        return {"error": str(e)}

# 3. Endpoint: Ask question (NL → SQL + Execute + Vector Search)
@app.post("/ask/")
async def ask_question(request: QueryRequest):
    nl_query = request.query

    try:
        sql_query = generate_sql_query(nl_query)
        print(f"[DEBUG] Generated SQL: {sql_query}")
    except Exception as e:
        return {
            "error": "Failed to generate SQL query.",
            "details": str(e),
            "input_query": nl_query
        }

    try:
        with engine.connect() as conn:
            result = conn.execute(text(sql_query))
            rows = [dict(row._mapping) for row in result]
    except Exception as e:
        return {
            "error": "Failed to execute SQL query.",
            "details": str(e),
            "generated_sql": sql_query
        }

    try:
        similar_docs = vactor_similarity_search(nl_query)
        context = [doc.page_content for doc in similar_docs]
    except Exception as e:
        context = [f"Vector search failed: {str(e)}"]

    try:
        prompt = f"""
         You are a helpful assistant. Use the SQL result and context to answer the question.

         Context:
             {context}

        SQL Result:
        {rows}

        Question: {nl_query}

        Answer in a clear, friendly way:
        """

        result=model.invoke(prompt).content
    except Exception as e:
        result=f"error occured for dynamic response {str(e)}"
    return {
        "natural_language_query": nl_query,
        "generated_sql": sql_query,
        "sql_results": rows,
        "semantic_context_matches": result
    }

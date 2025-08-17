import os
import getpass
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()
grok_key=os.getenv("GROQ_API_KEY")
model = init_chat_model("llama3-8b-8192", model_provider="groq")
def generate_sql_query(user_input):
    prompt="""
    1.you are connected to the mysql database.
    TABLE: Employee
    COLUMNS-id,name,age,salary,department.
    2.you are a sql query expert.
    3. dont user markdown.
    4. No need to explain the query.
    """
    response = model.invoke(f"{prompt},user query:{user_input}")
    return response.content

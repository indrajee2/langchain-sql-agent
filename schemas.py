from pydantic import BaseModel

class QueryRequest(BaseModel):
    query: str
    
class EmployeeCreate(BaseModel):
    name: str
    age: int
    salary: int
    department: str
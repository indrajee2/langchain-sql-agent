from sqlalchemy import Column,Integer,String
from database import Base

class Employee(Base):
    __tablename__ = "employee"
    
    id= Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    salary=Column(Integer)
    age=Column(Integer)
    department = Column(String(50))
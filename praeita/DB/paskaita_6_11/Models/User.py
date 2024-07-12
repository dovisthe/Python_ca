from sqlalchemy import Column, Integer, String, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship
import datetime
from database import Base
from Models.associations import role_user_associasion




class User(Base):
    __tablename__ = 'Users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    
    users = relationship("Roles", secondary= role_user_associasion , back_populates= "Users")
    invoices = relationship("Invoices", back_populates="User")
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f"{self.id}|{self.name}|{self.age}"
    
from sqlalchemy import Column, ForeignKey, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from Models.associations import role_user_associasion


class Invoice(Base):
    __tablename__ = 'Invoices'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)   
    user_id = Column(Integer, ForeignKey('Users.id'))
    
    user = relationship("User", back_populates= "Invoices")
    
    
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f"{self.id}|{self.name}"
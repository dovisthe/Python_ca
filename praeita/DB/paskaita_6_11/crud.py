from requests import session
from database import get_db
from Models.User import User
from Models.Role import Role

session = get_db()

#----------User CRUD

def create_user(name, age):
    user = User(name, age)
    
    session.add(user)
    session.commit()
    
def get_all_user():
    users = session.query(User).all()
    for user in users:
        print(user)  
    
    
#--------ROLE CRUD----------------------------------------

def create_role(name):
    role = Role(name)
    
    session.add(role)
    session.commit()
    
    
def get_all_role():
    roles = session.query(Role).all()
    for role in roles:
        print(role)
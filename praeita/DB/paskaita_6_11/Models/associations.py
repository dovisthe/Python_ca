from sqlalchemy import Column, Integer, Table, ForeignKey
from database import Base
  

role_user_associasion = Table(
    'role_user',
    Base.metadata,
    Column('role_id', Integer, ForeignKey('Roles.id')),
    Column('user_id', Integer, ForeignKey('Users.id'))
) 

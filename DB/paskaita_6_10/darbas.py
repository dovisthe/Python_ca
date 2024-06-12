from Classes.User import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///Vartotojai_Database.db')

SessionMaker = sessionmaker(bind=engine)

session = SessionMaker()


while True:
    
    pasirinkimas = input(
        '''
1. Atspausdink visus vartotojus
2. Sukurk nauja vartotoja      
3. Surask pagal id
4. Pakeisti vartotoja  
5. Pasalinti vartotoja

Iveskite: '''
    )
    
    if pasirinkimas == "1":
        users = session.query(User).all()
        for user in users:
            print(user)
            
    if pasirinkimas == "2":
        vardas = input("Iveskite vartotojo varda: ")
        amzius = int(input("Iveskite amziui: "))
        
        user = User(vardas, amzius)
        
        session.add(user)
        session.commit()
        
    if pasirinkimas == "3":
        id = int(input("Iveskite vartotojo id: "))
        
        user = session.get(User,id)
        print(user)
        
    if pasirinkimas == "4":
        id = int(input("Iveskite vartotojo id: "))
        
        user = session.get(User,id)
        
        pasirinkimas_keisti = int(input(
'''
Ka noretumet keisti?    

1. Varda
2. Amziu

Iveskite: 
'''))
        
       
        
        if pasirinkimas_keisti == 1:
            naujas_vardas = input("Iveskite nauja vartotojo varda: ")
            user.name = naujas_vardas
            
        if pasirinkimas_keisti == 2:
            naujas_amzius = int(input("Iveskite nauja vartotojo amziu: "))
            user.age = naujas_amzius
            
        session.commit()
        
    if pasirinkimas == "5":
        id = int(input("Iveskite vartotojo id: "))
        
        user = session.get(User,id)
        
        session.delete(user)
        session.commit()
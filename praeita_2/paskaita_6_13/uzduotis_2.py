class User:
    def __init__(self, password):
        self._password = password
        
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        if len(value) >= 8:
            self._password = value
        
    @property
    def ar_saugus(self):
        if any(char.isdigit() for char in self._password):
            return "taip"
        else:
            return "NE"
    


user = User("miaumiau")
print(user.password) 
print(user.ar_saugus)  

user.password = "miaumiau88888"
print(user.password)  
print(user.ar_saugus)  
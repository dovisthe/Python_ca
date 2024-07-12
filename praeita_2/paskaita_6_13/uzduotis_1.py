class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius 

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._fahreinheit = value


temp = Temperature(25)
print(f"Celsijaus temperatūra: {temp.celsius}")
print(f"Farenheito temperatūra: {temp.fahrenheit}")

temp.celsius = 30
print(f"Nauja Celsijaus temperatūra: {temp.celsius}")
print(f"Nauja Farenheito temperatūra: {temp.fahrenheit}")
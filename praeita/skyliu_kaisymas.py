# skaicius = 15.48958
# for i in range(0,50):
#     print('-'*21)
#     print(f'{i:>{10}.4f}|{i:<{10}.4f}')
#     print('-'*21)




# my_list = [5,7,9,8,9,4,2,4,5,1,1,1,2,2,2,3,3,3]
# tekstas = "Sveiki, mano vardas Sveiki, kaip jums Vardas sekasi, Justas, Man MAN Man Man Man Man"
# my_set = set(tekstas.split())
 
# print(my_set)




# mano_tuple_sarasas = [(4,6,8),(1,7,9),(9,4,4),(5,15,8),(10,19,9)]
 
# for a,b,c in mano_tuple_sarasas: # a = mano_tuple_sarasas[0][0] b = mano_tuple_sarasas[0][1] ... a = mano_tuple_sarasas[1][0] b = mano_tuple_sarasas[1][1]...
#     print(f"{a}+{b}+{c}={sum((a,b,c))}")
    
    
    
    
# for ind, skaicius in enumerate(skaiciai):
#     print(f"skaicius {skaicius} yra {ind} sarase")



# skaiciai2 = [4,9,5,1,2,3]
# skaiciai3 = [5,7,8,5,4,2,8]
# for skai in zip(skaiciai,skaiciai2):
#     print(skai)
 
# vardai = ["Jonas","antanas","Mantas","Karolis"]
 
# amziai = [15,54,21,23]
 
# zodynas = dict(zip(vardai,amziai))
 
# print(zodynas)
 
# antano_amzius = zodynas["antanas"]



# a,b,c = ["Stalas","kede","lova"]
 
# print(a)


# mano_sarasas = [num for num in range(0,6)] # num = 0 mano_sarasas.append(0)... num = 1 mano_sarasas.append(1)
 
# for num in range(0,6):





# skaiciai = [5,7,9,10]
# mano_sarasas = [num*2 for num in skaiciai if num % 2 ==0] # num = 0 mano_sarasas.append(0)... num = 1 mano_sarasas.append(1)
 
# for num in skaiciai:
#     if num % 2 ==0:
#         mano_sarasas.append(num*2)
 
# print(mano_sarasas)




# zodziai = ["labas",'Kaip',"sekasi"]
# print('----'.join(zodziai))



# class MyClass():
#     def __init__(self) -> None:
#         pass
#     def suma(self):
#         raise NotImplementedError("Dar neigyvendinta")
   
#     def dalyba(self,a,b):
#         if(b == 0):
#             raise ZeroDivisionError("DALYBA IS NULIO")
#         else:
#             return a/b
# klase = MyClass()
 
 
# try:
#     print(klase.dalyba(7,0))
   
#     print("Suveikiau tinkamai")
 
# except Exception as e:
#     print(f"ivyko klaida {e}")

# skaiciai = [8,4,3]
 
# def cubed(x):
#     return x **3
 
# skaiciai_3 = map(lambda x: x**3,skaiciai) # x = skaiciai[0].... return result = x ** 3 skaiciai_3 append(result) (Pakartojama len(skaiciai))
 
# print(list(skaiciai_3))
 
# skaiciai = [8,4,3]
 
# def cubed(x):
#     return x **3
 
# skaiciai_3 = map(cubed,skaiciai) # x = skaiciai[0].... return result = x ** 3 skaiciai_3 append(result) (Pakartojama len(skaiciai))
# skaiciai_3 = map(lambda x: x**3,skaiciai) # x = skaiciai[0].... return result = x ** 3 skaiciai_3 append(result) (Pakartojama len(skaiciai))
 
# print(list(skaiciai_3))
 
# def suma(a,b):
#     return a+b
 
# print(suma(4,9))
 
 
# lambda a,b: a+b # - suma
 
# mano_metodas = lambda a,b: a+b
 
# print(mano_metodas(5,9))
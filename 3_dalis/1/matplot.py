import matplotlib.pyplot as plt
import numpy as np

orai = np.random.randint(-20,30, (12,30))

# print(f"Orai metams, menesiu vidurkiai: \n{orai}")
men = 0
for day in orai:
    men += 1
    print(f"2024:{men} temp: {day}")

orai[0,0] = 50
# print(orai)

# print(f"Orai su pakeistu sausiu: \n{orai}")
men = 0
for vid in orai:
    men += 1
    vid1 = np.mean(vid)
    print(f"2024:{men} vidurkis: {vid1}")

# print(f"Vidutine temp: \n{vid}")

men = 0
for nukrp in orai:
    men += 1
    nukrypy = np.std(nukrp)

    print(f"2024:{men} nukrypimas vid: \n {nukrypy}")
        
        
# plt.plot(orai)
# plt.show() 

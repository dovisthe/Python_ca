import views.views as views


def programa():
    while True:
        views.pasirinkimai()
        pasirinkimas = input("Pasirinkite veiksmą: ")
        if pasirinkimas == "1":
            views.pasirinkimas1()

        elif pasirinkimas == "2":
            views.pasirinkimas2()
            
        elif pasirinkimas == "3":
            views.pasirinkimas3()

        elif pasirinkimas == "4":
            views.pasirinkimas4()
            
        elif pasirinkimas == "5":
            views.pasirinkimas5()
            
        elif pasirinkimas == "6":
            views.pasirinkimas6()
            
        elif pasirinkimas == "7":
            views.pasirinkimas7()   

        elif pasirinkimas == "0":
            break

        else:
            print("Neteisingas pasirinkimas. Bandykite dar kartą.")
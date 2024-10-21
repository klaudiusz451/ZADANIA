a=float(input("Podaj pierwszą: "))#konwersja na typ zmiennoprzecinowy ze stringa
b=float(input(("Podaj drugą: ")))
if a<0 and b<0:#sprawdzanie czy liczby są ujemne
    print("Obie liczby są mniejsze od 0 -> KONIEC PROGRAMU")
    quit()
elif a<0:
    a=-1*a
elif b<0:
    b=-1*b
elif b==0:
    print("nie dzielimy przez 0")
    quit()

"""
wykonywanie
działań
"""
print(f"dodawanie : {a+b}")
print(f"odejmowanie : {a-b}")
print(f"dzielenie : {a/b}")
print(f"mnożenie : {a*b}")
print(f"potęgowanie : {a**2}")
print(f"potęgowanie : {b**2}")
print(f"pierwiastkowanie : {a**0.5}")
print(f"pierwiastkowanie : {b**0.5}")
if a*b==10:
    print("Yey!")

    


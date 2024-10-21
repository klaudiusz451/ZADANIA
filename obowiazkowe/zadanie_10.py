import random
while 1:
    a=int(input("Podaj pierwszą liczbę: "))
    b=int(input("Podaj drugą liczbę: "))
    print("+ dodawanie")
    print("- odejmowanie")
    print("* mnożenie")
    print("/ dzielenie")
    print("# pierwiastkowanie")
    print("^ potęgowanie")
    print("x losowanie liczby z zakresu")
    action=input("Co chcesz zrobić :")
    if action=="+":
        print("Suma :"+str(a+b))
    elif action=="-":
        print("Różnica :"+str(a-b))
    elif action=="*":
        print("Iloczyn :"+str(a*b))
    elif action=="/":
        if b==0:
            print("błąd")
        else:
            print("Iloraz :"+str(a/b))
    elif action=="#":
        if b<0:
            print("błąd")
        else:
            print("Pierwiastek stopnia "+str(a)+" z "+str(b)+" to "+str(b**(1/a)))
    elif action=="^":
        print("Potęgowanie : "+str(a**b))
    elif action=="x":
        if a<b:
            print("Wylosowana liczba z zakresu to : "+str(random.randint(a, b)))
        elif a>b:
            print("Wylosowana liczba z zakresu to : "+str(random.randint(b, a)))
    else:
        print("brak operacji")
    m=input("Czy chcesz wprowadzić nowe dane? T/N :")
    if m=="N":
        print("KONIEC")
        quit()
    elif m!="N" and m!="T":
        print("brak operacji")
        quit()

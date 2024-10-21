saldo=1000
pin="1234"
print("WITAJ W BANKU!!!")
print("1 - wpłata")
print("2 - wypłata")
print("3 - saldo konta")
x=int(input("Co chcesz zrobić?: "))
while 1>0:
    if(x==1):
        pin2=input("Podaj pin: ")
        if pin2==pin:
            a=int(input("Podaj kwotę do wpłaty: "))
            saldo=saldo+a
        else:
            print("Niepoprawny pin")
    elif(x==2):
        pin2=input("Podaj pin: ")
        if pin2==pin:
            a=int(input("Podaj kwotę do wypłaty: "))
            if(a>saldo):
                print("BŁĄD!!! ZA MAŁO ŚRODKÓW")
            else:
                saldo=saldo-a
        else:
            print("Niepoprawny pin")
    elif(x==3):
        pin2=input("Podaj pin: ")
        if pin2==pin:
            print(f"Twoje saldo: {saldo} ")
        else:
            print("Niepoprawny pin")
    else:
        print("Nie ma takiej operacji")
    print("1 - wpłata")
    print("2 - wypłata")
    print("3 - saldo konta")
    print("4 - zakończ ")
    x=int(input("Co chcesz zrobić w kolejnym kroku?: "))
    if(x==4):
        print("DZIĘKUJEMY")
        quit()

a=float(input("Podaj współczynnik a :"))
if a==0:
    print("BŁĄD")
else:
    b=float(input("Podaj współczynnik b :"))
    c=float(input("Podaj współczynnik c :"))
    delta=b**2-(4*a*c)
    if delta<0:
        print("Program nie obsługuje liczb zespolonych")
    elif delta==0:
        x0=(-1*b)/(2*a)
        print("Pierwiastek : "+str(x0))
    else:
        x1=(-1*b-delta**0.5)/(2*a)
        x2=(-1*b+delta**0.5)/(2*a)
        print("Pierwiastki to : "+str(x1)+" "+str(x2))

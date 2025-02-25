
try:
    m=int(input("Podaj koniec zakresu : "))
    if m<1 or m>10000:
        print("BŁĄD ZAKRESU")
    else:
        y=1
        list=[]
        for i in range(1,m+1):
           x=i*y
           print(f"{i}! = {x}")
           list.append(x)
           y=x
           if i>1:
                print(f"{list[i-1]}-{list[i-2]}={list[i-1]-list[i-2]}")
except ValueError:
    print("BŁĄD")

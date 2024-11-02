def fact(N):
    x=1
    for i in range(1,N+1):
        x=i*x
    return x


list=[]
try:
    m=int(input("Podaj koniec zakresu : "))
    if m<1 or m>10000:
        print("BŁĄD ZAKRESU")
    else:
        for i in range(1,m+1):
            k=fact(i)
            print(f"{i}! = {k}")
            list.append(k)
        print("RÓŻNICE")
        for i in range(1,m):
            print(f"{list[i]}-{list[i-1]}={list[i]-list[i-1]}")
except ValueError:
    print("BŁĄD")        
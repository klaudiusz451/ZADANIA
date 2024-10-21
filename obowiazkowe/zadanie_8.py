import random
h=int(input("Podaj wysokość choinki: "))

macierz = [["*" for _ in range(2*h-1)] for _ in range(h)]

"""for i in range(0,h):
    for j in range(0,2*h-1):
        print(macierz[i][j],end="")
    print(" ")"""
#wypełnienie
for i in range(0,h):
    for j in range(0,2*h-1):
        if(j<h-1):
            if(i+j<h-1):
                macierz[i][j]=" "
        if(j>h-1):
            if(j-i>=h):
                macierz[i][j]=" "
macierz[0][h-1]="X"

#bombki
for i in range(0,h*2):
    y1 = random.randint(1,h-1)
    x1 = random.randint(0,2*h-2)  
    if macierz[y1][x1]=="*":
        macierz[y1][x1]="o"
        

#wypisanie
for i in range(0,h):
    for j in range(0,2*h-1):
        print(macierz[i][j],end="")
    print(" ")
for i in range(0,h-1):
    print(" ",end="")
print("U")
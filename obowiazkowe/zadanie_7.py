a=int(input("Wprowadź początek: "))
b=int(input("Wprowadź koniec: "))
x=a-b
if x<0:
    x=-1*(a-b)#ilosc liczb: x+1
if x>=20:
    if a-b<=0:
        if x%2==0:#nieparzysta ilosc liczb
            med=int((a+b)/2)
            for i in range(med-3,med+4):
                if i!=med:
                    print(f"{i}, ")
            print("inna pętla")
            i=med-3
            while i<=med+3:
                if i!=med:
                    print(f"{i}, ")
                i=i+1
        else:#parzysta ilosc liczb
            med=int((a+b)/2)#ucina to co po przecinku
            for i in range(med-2,med+4):
                print(f"{i}, ")
            print("inna pętla")
            i=med-2
            while i<=med+3:
                print(f"{i}, ")
                i=i+1
    else:
        if x%2==0:#nieparzysta ilosc liczb 
            med=int((a+b)/2)
            for i in range(med+3,med-4,-1):
                if i!=med:
                    print(f"{i}, ")
            print("inna pętla")
            i=med+3
            while i>=med-3:
                if i!=med:
                    print(f"{i}, ")
                i=i-1
        else:#parzysta ilosc liczb
            med=int((a+b)/2)
            for i in range(med+3,med-3,-1):
                    print(f"{i}, ")
            print("inna pętla")
            i=med+3
            while i>=med-2:
                print(f"{i}, ")
                i=i-1
else:
    if a-b<=0:
        for i in range(a,b+1):
            print(f"{i}, ")
        print("inna pętla: ")
        i=a
        while i<=b:
            print(f"{i}, ")
            i=i+1
    else:
        for i in range(a,b-1,-1):
            print(f"{i}, ")
        print("inna pętla: ")
        i=a
        while i>=b:
            print(f"{i}, ")
            i=i-1
    
    
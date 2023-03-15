c=[]

def degerSakla(x):
    for a in range(x):
        degerTut=input("Değer gir:")
        c.append(degerTut)
    print(c)
    # return c
    

cevapDeger=int(input("Kaç tane değer girmek istiyorsun?: "))

degerSakla(cevapDeger)


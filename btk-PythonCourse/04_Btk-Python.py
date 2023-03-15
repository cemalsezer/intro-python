# def txtPrinter(txt,counter):
#     print(txt*counter)
    
# txtPrinter('Cemal\n',10)

# def cnvrList(*args):
#     liste=[]
    
#     for param in args:
#         liste.append(param)
    
#     return liste

# result = cnvrList(10,20,30)

# print(result)

########--------------

# urunler=[]

# responseAnsw = int(input('Kaç adet ürün gireceksin: '))
      
# def urunYazdir(adet):
#     i=0
#     while i<adet:
#         name=input('Ürün ismi:')
#         price=input('Ürün fiyati: ')
#         urunler.append({'name':name,'price':price})
#         i+=1
    
#     dispUser(urunler)

# def dispUser(*args):
#     for idx,param in enumerate(*args):
#         print(f'{idx}:{param}')
        
        
# urunYazdir(responseAnsw)



valueFind = int(input('Enter the number: '))

def numDef(x):
    numList=[]
    
    for i in range(2,x):
        if (x%i==0):
            numList.append(i)
    
    numList.append(f'Kendisi: {x}')
    return numList

print(numDef(valueFind))
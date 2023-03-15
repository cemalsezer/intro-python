sayilar=[1,3,5,7,9,12,19,21]

# i=0
# while(i < len(sayilar)):
#     print(sayilar[i])
#     # print(i)
#     i+=1

"""Baslangic ve sonuc sayisini kullanicinin belirlediği 
tek sayıları getir"""

# startPoint=int(input('Start Point: '))
# endPoint=int(input('End Point: '))
# counter=1

# while startPoint<=endPoint:
#    if startPoint%2==1:
#        print(f'{counter}. number: {startPoint}')
#    startPoint+=1
#    counter+=1
   
   
"""Kullanıcıdan beş sayı alıp bunları sıralı şekilde yazıdırma"""
# x=0
# answer=[]
# while(x<5):
#     answer.append(int(input('Number: ')))
#     x+=1
    
# answer.sort()
# print(answer)
    
    
"""Kullanıcıdan aldığın ürün sayısına göre ürünler listesi içinde sakla
    *ürün sayısını kullanıcı belirtecek
    *dic liste yapısı (name, price) şeklinde olsun
    *ürün ekleme işlemi bittiğinde ürünleri ekrana while 
    ile yazdir
"""
# i=0
# c=0
# counter=1
# urunler=[]

# adet = int(input('Kaç adet ürün gireceksin: '))


# while(i<adet):  
#     name=input('Ürün ismi: ')
#     price=input('Ürün fiyati: ')
#     urunler.append({'name':name,'price':price})
#     i+=1


# for products in urunler:
#     print(f'{counter}. Product Name: {products["name"]}, Product Price: {products["price"]}')
#     counter+=1

# x=0
# result=0
# while x < 100:
#     x+=1
#     if x%2==0:
#         continue
#     result+=x
    # # print(x,result)
    
# print(result)
    

urunler=[]
def dispUser(**args):
    for key,value in args.items():
        print(f'{key}:{value}')

    

dispUser(name=input('Ürün ismi:'),
         price=input('Ürün fiyati: '))
    

square = lambda x:x**2

print(square(2))
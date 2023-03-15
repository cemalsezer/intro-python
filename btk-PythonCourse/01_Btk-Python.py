sayilar=[1,3,5,7,9,12,19,21]

# hangi sayılar üçün katıdır
# for i in sayilar:
#     if i%3==0:
#         print(i)


"""
sayilar listesindeki sayiların toplamı

"""
# toplam=0
# for i in sayilar:
#     toplam+=i

# print(f'Toplamı: {toplam}')


"""Tek sayıların karesi"""


# for i in sayilar:
#     if i%2==1:
#         print(i,':',i**2)


"""
    Şehirlerden hangisi en fazla 5 karakterlidir.
"""


citys=['izmir','istanbul','ankara','manisa']

# for sepCitys in citys:
#     x=sepCitys.split(',')
#     for sehirH in x:    
#         if len(sehirH) <= 5:
#             print(sehirH)

# for sepCitys in citys:  
#     if len(sepCitys) <= 5:
#         print(sepCitys)

urunler=[
    {'name':'samsung S6', 'price':'3000'},
    {'name':'samsung S7', 'price':'4000'},
    {'name':'samsung S8', 'price':'5000'},
    {'name':'samsung S9', 'price':'6000'},
    {'name':'samsung S10', 'price':'7000'},
    ]

"""ürünlerin fiyatlarının toplamı"""
# toplam=0

# for urun in urunler:
#     x=int(urun['price'])
#     toplam+=x

# print(toplam)

"""ürünlerin fiyatlardan en fazla 5k olanları getir"""

for urun in urunler:
    x=int(urun['price'])
    if x <= 5000:
        print('Fiyati en fazla 5k olan ürünler',urun['name'],x)

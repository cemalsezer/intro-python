# 1'den 10 a kadar olan sayıların karesi

# newdict={num: num*num for num in range(1,11)}
# print(newdict)


# {'milk': 0.7752, 'coffee': 1.9, 'bread': 1.9}

dolar_to_tl=18

dolar_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}


convertMoney={urun: deger*dolar_to_tl for (urun,deger) in dolar_price.items()}

print(convertMoney)
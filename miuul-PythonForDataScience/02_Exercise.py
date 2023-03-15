 ## (maas*zam/100)+maas zamlı maas hesaplama formülü

# maas zammını hesaplayan fonksiyon
def rateCalculate(salary, rate):
    return int((salary*rate/100)+salary) 

employee=[2000,1500,5000,6000,7000]
#maaslari bir listeye aldım


#maaslarin icinde dolaşıp zam oranlarına göre yazdiran döngü
for maas in employee:
    #fonksyionu cagir
    if maas>=3000:
        print(rateCalculate(maas,15))
    else:
        print(rateCalculate(maas,10))
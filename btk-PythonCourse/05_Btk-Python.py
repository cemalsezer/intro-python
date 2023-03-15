square=lambda x: x**2

def funCall():
    numbers=[]
    i=0

    queryCounter=int(input('How many enter: '))
    
    while i<queryCounter:
        numbers.append(int(input('Enter the number: ')))
        i+=1
        result=list(map(square,numbers)) 
    
    return result
    
    
print(funCall())



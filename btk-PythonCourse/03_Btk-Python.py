# group=[[],[]]
# numbs=[group[0].append(x**2) if x%2==0 else group[1].append(x**3)
#        for x in range(10)]        
# print(group)



# sayi=3
# tree=''
# for x in range(sayi+1):
#     for j in range(x):
#         tree+='* '
#         print(tree)

group=[[],[]]
numbs=[group[0].append({y})if x<=0 else group[1].append({x,y})  
       for x in range(3) for y in range(3)] 

for i,txt in enumerate(group):
    print(i,txt)
    

x=range(10)
new_dict={}

# for i in x:
#     if i%2==0:
#         new_dict[i]=i**2
        
# print(new_dict)


x={i: i**2 for i in x if i%2==0 }
print(x)
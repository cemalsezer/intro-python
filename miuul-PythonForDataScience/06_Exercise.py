"""
    maas listesinden maasi çekip zam yaptıran fonk
"""

# salaries=[3000,3500,4000]
# rates=[10,15]

# def salariesCal(sal,rate):
#     x=[]
#     for index in sal:
#         if index > 3000:
#             x=int((index*rate[1]/100)+index)
#             print(x)
#         else:
#             x=int((index*rate[0]/100)+index)
#             print(x)
            

# salariesCal(salaries,rates)


salaries=[3000,3500,4000]
null_salaries=[]


def salariesCal(maas,zam):
    return maas*zam/100+maas

# for maasList in salaries:
#     if maasList > 3000:
#         null_salaries.append(salariesCal(maasList,15))
#     else:
#         null_salaries.append(salariesCal(maasList,10))

# print(null_salaries)



null_salaries=[salariesCal(maasList,15) if maasList > 3000 else salariesCal(maasList,10) for maasList in salaries]

print(null_salaries)

#list comprehensions
# salaries=[2000,3000]
# rates=[10,15]
# x=list(map(lambda salarie,rate: salarie*rate/100+salarie,salaries,rates))
# print(x)


# kareKok=lambda x:x*x
# print(kareKok(3))

students=["Denise", "Arsen", "Tony", "Audrey"]
for student in students:
    if len(student)% 2 == 0:
        print(student[0].upper())
    else:
        print(student[0].lower())

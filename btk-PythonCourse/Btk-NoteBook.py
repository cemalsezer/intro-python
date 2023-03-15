cars=["Bmw","Mercedes","Opel","Mazda"]

result=len(cars) # Liste kaç elemanlıdır

result=cars[-1] # Listenin son elemanı hangisidir.

result=cars[-1]='Toyota'
# print(cars)

result='Mercedes' in cars

result=cars[-2]

result=cars[0:3]

result=cars[2:]=['Toyota','Mazda']

result=cars.append('Nissan')
del cars[-1]
cars.sort()
cars.reverse()
# print(cars)

names=["İrem","Cemal","Tarçın"]
years=[1800,1900,2000]

result=names.append('Aysar')
result=names.insert(0,'Umay')

del names[0]
result='Cemal' in names
result=years.count(2000)

# print(result)
# result=names.clear()

cars=[]
result='Mustang,Ford'
cars.append(result.strip(','))

# print(cars)


# brand=[]
# for i in range(3):
#     result=str(input('Marka: '))
#     brand.append(result)


# print(brand)



# key=employee.keys()
# if 'cemalsezer' in key:
#     print('yes')




# students[number]={
#     'name':name,
#     'surname':surname,
#     'age':age
# }



students={}

number=int(input('Enter the number of student: '))
name=input('Enter the name of student: ')
surname=input('Enter the surname of student: ')
age=int(input('Enter the name of student: '))


students.update({
    number:{
        'name':name,
        'surname':surname,
        'age':age
    }
})


# print(students)

resultNo=int(input('Student Number: '))

for resultNo in students.keys():
    print(f' Aradığın no: \n{students[number]}')


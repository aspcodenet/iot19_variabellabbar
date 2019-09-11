import datetime

birthYear = int(input("Ange födelseår:"))
age = 2019 - birthYear

print("Du är ", age , " år")


today =  datetime.datetime.now()
year = today.year

age = year - birthYear
print("Du är ", age , " år")

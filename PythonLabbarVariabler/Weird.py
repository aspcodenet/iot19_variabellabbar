



n = int(input("Mata in ett tal"))

if n %2 == 0:
    if n <=2 and n <=5:
        print("Not Weird")
    elif n >=6 and n <=20:
        print("Weird")
    elif n > 20: 
        print("Not Weird")
else:
    print("Weird")



n = int(input())
check = {True: "Not Weird", False: "Weird"}

print(check[
        n%2==0 and (
            n in range(2,6) or 
            n > 20)
    ])





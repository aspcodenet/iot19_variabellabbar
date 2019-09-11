age = 47

if age % 2 == 1:
    print("Odd")

#if age < 48:
#    print("Du är ung")
#else:
#    print("Du är gammal")

name = "Stefan"

if name == "Stefan":
    print(f"Ja du heter {name}")


age="Kalle"
if age < 48:
    print("Du är ung")
    print("men inte så länge till")
if age > 47 and age < 65:
    print("ganska gammal")
if age > 64:
    print("Du är jättegammal")
print("radwen efter")


if age < 48:
    print("Du är ung")
    print("men inte så länge till")
elif age > 47 and age < 65:
    print("ganska gammal")
else:
    print("Du är jättegammal")
print("radwen efter")
















sum = int(input("Ange en summa"))
moms = sum * 0.25
sum = sum + moms
print("Pris med moms:", sum)

skrivUt = f'pris {sum} med moms:  {tal1+tal2}'
print(skrivUt)
print(f'pris {sum} med moms:  {tal1+tal2}')
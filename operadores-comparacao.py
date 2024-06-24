x = y = z = False
n1 = n2 = 0

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

x = n1 == n2
print(f"São iguais? {x}")

z = n1 > n2
print(f"{n1} é maior que {n2}? {z}")

y = n1 != n2
print(f"{n1} é diferente de {n2}? {y}")
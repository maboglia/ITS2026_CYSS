"""Recap of the previous lessons."""

# variabili e tipi di dati
x = 5
y = 3.14
name = "Alice"
is_student = True

# operatori
sum = x + y
difference = x - y
product = x * y
quotient = x / y

# strutture di controllo
if is_student:
    print(f"{name} is a student.")
else:
    print(f"{name} is not a student.")

for i in range(5):
    print(i)

x = 5
while x > 0:
    print(x)    
    x -= 1

# tipi di dato primitivi e complessi
type(x)  # int
type(y)  # float
type(name)  # str
type(is_student)  # bool 

numbers = [1, 2, 3, 4, 5]
number_set = {1, 2, 3, 4, 5}
person = {"name": "Alice", "age": 30, "is_student": True}
tupla = (1, 2, 3)

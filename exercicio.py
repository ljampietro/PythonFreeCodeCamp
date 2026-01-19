import re
# name = str(input("digite seu nome: "))
# age = int(input("digite sua idade: "))
# student_status = True
#
# print(f"Hello, {name}! You are {age} years old.")
#
#
# # This section prints the variable and its type
# print(f"Name: {name}, Type: {type(name)}")
# print(f"Age: {age}, Type: {type(age)}")
# print(f"Student Status: {student_status}, Type: {type(student_status)}")
#
# print("\n")
# print("\n")
#
# int1 = 2
# int2 = 5
# flt1 = 6.7
#
# print(int1 + int2)
# print(int1 - int2)
# print(int1 * int2)
# print(int1 / int2)
# print(int1 // int2)
# print(int1 % int2)
# print(int1 ** int2)
# print(int1 + flt1)
# print("\n")
# print("\n")
#
# int3 = int(input("digite um numero inteiro: "))
# print(f' int: {int3}, float: {float(int3)}')
#
# flt2 = float(input("digite um numero: "))
# print(f' float: {flt2}, int: {int(flt2)}')
#
# number = str(input("digite um numero: "))
# print(int(number) + 10)
# print(int3 + int(number))
# print(int3 - int(number))
# print(int3 * int(number))
# print(int3 / int(number))
# print(int3 // int(number))
# print(int3 % int(number))
# print(int3 ** int(number))

# length = int(input('digite o comprimento: '))
# width = int(input('digite a largura: '))
#
#
# def calculate_rectangle_area(length, width):
#     return length * width
#
# print(calculate_rectangle_area(length, width))

valor = 10

valor += 5
print(valor)
valor += 5
valor -= 8
print(valor)

valor2 = 4

valor2 *= 2
print(valor2)

print("helo" 'world ' * 2)
# class test():
#     id = 0
#     def __init__(self, id):
#         self.id = id
#         id = 2


# print(t.id)
# def a(a, b, c): pass
a = 7
a.__str__()
print()
text = "abc123def456ghi"
patt = r"(?:abc)\d+"
match = re.findall(patt, text)
print(match)
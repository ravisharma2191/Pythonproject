#
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
# operations
c = a + b
d = a - b
e = a * b
f = a / b
print(f"Addition: {int(c)}")
print(f"Subtraction: {int(d)}")
print(f"Multiplication: {int(e)}")
print(f"Division: {int(f) if f.is_integer() else f}")


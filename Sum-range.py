
value = 0
num1 = int(input("Enter an integer First number: "))
num2 = int(input("Enter an integer  Second number: "))
for i in range(num1, num2):
    value += i
print(f"The sum of integers from {num1} to {num2} is: {value}")

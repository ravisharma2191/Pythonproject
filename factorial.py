def factorial(n):
    if n < 0:
        return "does not exist because of negative numbers"
    elif n < 2:
        return 1
    else :
     return n * (factorial (n-1))
n = int(input("Enter the value for factorial :"))
print(f"The factorial of {n} is {factorial(n)}")

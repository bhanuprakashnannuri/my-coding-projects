a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = input("Enter a valid operator: ")

if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    if b != 0:
        print(a / b)
    else:
        print("Cannot divide by zero!")
else:
    print("Enter a valid operator.")

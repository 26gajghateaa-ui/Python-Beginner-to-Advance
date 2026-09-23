a = float(input("Enter first number= "))
b= float(input("Enter second number= "))


print("Select operation: +, -, *, /")
o = input("Enter operator: ")


if o == '+':
    print(f"Result: {a} + {b} = {a + b}")
elif o == '-':
    print(f"Result: {a} - {b} = {a - b}")
elif o == '*':
    print(f"Result: {a} * {b} = {a * b}")
elif o == '/':
    if num2 != 0:
        print(f"Result: {a} / {b} = {a / b}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator! Please enter +, -, *, or /")

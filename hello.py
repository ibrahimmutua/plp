num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

if op == "+":
    print(num1, "+", num2, "=", num1 + num2)
elif op == "-":
    print(num1, "-", num2, "=", num1 - num2)
elif op == "*":
    print(num1, "*", num2, "=", num1 * num2)
elif op == "/":
    print(num1, "/", num2, "=", num1 / num2)
else:
    print("Invalid operation")

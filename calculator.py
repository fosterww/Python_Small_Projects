from calculatorclass import Calcurator # type: ignore
    
print("Calculator module loaded successfully.")

calc = Calcurator("MyCalculator")
result = 0
first_num = input("Enter first number: ")
second_num = input("Enter second number: ")
choose = input("Choose operation (+, -, *, /, **, sqrt): ")

if choose == "+":
    result = calc.add(float(first_num), float(second_num))
elif choose == "-":
    result = calc.substract(float(first_num), float(second_num))
elif choose == "*":
    result = calc.multiply(float(first_num), float(second_num))
elif choose == "/":
    result = calc.divide(float(first_num), float(second_num))
elif choose == "**":
    result = calc.exponentiation(int(first_num), int(second_num))
elif choose == "sqrt":
    result = calc.square_root(float(first_num))
else:
    print("Invalid operation selected.")


print(result)

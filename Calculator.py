def calculator():
    operand1 = float(input("\nPlease input first operand: "))
    operand2 = float(input("Please input second operand: "))
    operator = input("Please input operator: ")
    if operator == "+":
        return operand1 + operand2
    if operator == "-":
        return operand1 - operand2
    if operator == "*":
        return operand1 * operand2
    if operator == "/":
        return operand1 / operand2
    if operator == "//":
        return operand1 // operand2
    if operator == "**":
        return operand1 ** operand2
    return "Please enter valid values and operator"
print(calculator())

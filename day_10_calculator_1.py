def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What's the first number?: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))
calc_function = operations[operation_symbol]
answer = calc_function(num1, num2)
     
print(f"{num1} {operation_symbol} {num2} = {answer}")

operation_symbol = input("Pick an operation from the line above: ")
num3 = int(input("What's the third number?: "))
calc_function = operations[operation_symbol]
second_answer = calc_function(answer, num2)

print(f"{num1} {operation_symbol} {num2} = {second_answer}")

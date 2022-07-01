#from replit import clear
#from art import logo
# Calculator

#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

#Dict Operations
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}
def calculator():  
  num1 = int(input("What is your first number? "))
  for sym in operations:
    print(sym)
  should_continue = True

  while should_continue:
    operation_sym = input("Pick a operator from above: ")
    num2 = int(input("What is your second number? "))
    calculation = operations[operation_sym]
    answer = calculation(num1, num2)
  
    print(f"{num1} {operation_sym} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator()
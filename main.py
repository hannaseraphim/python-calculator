import sys

# Math
def addition():
  print("\n================")
  num1 = int(input("What's the first number? "))
  num2 = int(input("What's the second number? "))
  return print(f"\nResult: [{num1 + num2}]\n")

def subtraction():
  print("\n================")
  num1 = int(input("What's the first number? "))
  num2 = int(input("What's the second number? "))
  return print(f"\nResult: [{num1 - num2}]\n")

def multiplication():
  print("\n================")
  num1 = int(input("What's the first number? "))
  num2 = int(input("What's the second number? "))
  return print(f"\nResult: [{num1 * num2}]\n")

def division():
  print("\n================")
  num1 = int(input("What's the first number? "))
  num2 = int(input("What's the second number? "))
  return print(f"\nResult: [{num1 / num2}]\n")

def oddeven():
  print("\n================")
  num1 = int(input("What's the number to verify? "))
  if(num1 % 2 == 0):
    return print(f"\nResult: {num1} is [EVEN]\n")
  else: 
    return print(f"\nResult: {num1} is [ODD]\n")

def potentiation():
  print("\n================")
  num1 = int(input("What's the first number? "))
  num2 = int(input("What's the second number? "))
  return print(f"\nResult: [{num1 ** num2}]\n")

def quotient():
  print("\n================")
  num1 = int(input("What's the first number? "))
  num2 = int(input("What's the second number? "))
  return print(f"\nResult: Quotient is [{num1 // num2}]\n")
# ====================

# Finish the program
def exit():
  sys.exit()
# ====================

# Homepage
def main():
  print("\n================")
  print("Which operator do you want to use?")
  print("1 - Addition")
  print("2 - Subtraction")
  print("3 - Multiplication")
  print("4 - Division")
  print("5 - More...")
  print("0 - Exit ")
  print("================")
  opt = int(input("\nType an option: "))

  match opt:
    # Addiction
    case 1:
      addition()
      decision()

    # Subtraction
    case 2:
      subtraction()
      decision()
    
    # Multiplication
    case 3:
      multiplication()
      decision()

    # Division
    case 4:
      division()
      decision()

    # Even or odd
    case 5:
      secondpage()

    # Exit
    case 0:
      print("\nExiting...")
      exit()
    
    # Default
    case _:
      print("\nNot a valid number...")
      main()
# ====================

# Second page
def secondpage():
  print("\n================")
  print("Which operator do you want to use?")
  print("1 - Odd or even")
  print("2 - Potentiation")
  print("3 - Quotient")
  print("0 - Back ")
  print("================")
  opt = int(input("\nType an option: "))

  match opt:
    # Odd or even
    case 1:
      oddeven()
      decision()

    # Subtraction
    case 2:
      potentiation()
      decision()

    case 3:
      quotient()
      decision()

    # Go back
    case 0:
      main()

    # Default
    case _:
      print("\nNot a valid number...")
      secondpage()
# ====================

# After math
def decision():
  print("\n================")
  print("What to do now?")
  print("1 - Go back")
  print("2 - Exit")
  print("================")

  dec = int(input("\nType an option: "))
  
  match dec:
    case 1:
      main()
    case 2: 
      exit()
    case _: 
      print("Not a valid option")
      decision()
# ====================

# Calls the homepage/start function
main()
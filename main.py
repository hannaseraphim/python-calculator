import sys

# Math
def addition(n1, n2):
  return n1 + n2
def subtraction(n1, n2):
  return n1 - n2
def multiplication(n1, n2):
  return n1 * n2
def division(n1, n2):
  return n1 / n2

# Finish the program
def exit():
  sys.exit()


def main():
  print("\n================")
  print("Which operator do you want to use?")
  print("1 - Addition")
  print("2 - Subtraction")
  print("3 - Multiplication")
  print("4 - Division")
  print("0 - Exit ")
  print("================")
  opt = int(input("\nType an option: "))

  match opt:
    # Addiction
    case 1:
      print("\n================")
      num1 = int(input("What's the first number? "))
      num2 = int(input("What's the second number? "))
      print(f"\nResult: [{addition(num1, num2)}]\n")
      print("================")
      decision()

    # Subtraction
    case 2:
      print("\n================")
      num1 = int(input("What's the first number? "))
      num2 = int(input("What's the second number? "))
      print(f"\nResult: [{subtraction(num1, num2)}]")
      print("================")
      decision()
    
    # Multiplication
    case 3:
      print("\n================")
      num1 = int(input("What's the first number? "))
      num2 = int(input("What's the second number? "))
      print(f"\nResult: [{multiplication(num1, num2)}]")
      print("================")
      decision()

    # Division
    case 4:
      print("\n================")
      num1 = int(input("What's the first number? "))
      num2 = int(input("What's the second number? "))
      print(f"\nResult: [{division(num1, num2)}]")
      print("================")
      decision()

    # Exit
    case 0:
      print("\nExiting...")
      exit()
    
    # Default
    case _:
      print("\nNot a valid number...")
      main()

# After doing a math
def decision():
  print("\nWhat to do now?\n")
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


main()





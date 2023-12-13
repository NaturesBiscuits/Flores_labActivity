print("John Vincent Flores")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))


def calculate():
  if num1 == num2 and num2 == num3:
    print(f"{num1} * {num2} * {num3} = {num1 * num2 * num3}")
  elif num1 == num2:
    print(f"{num1} * {num2} + {num3} = {num1 * num2 + num3}")
  elif num1 == num3:
    print(f"{num2} + {num3} * {num1} = {num2 + num3 * num1}")
  elif num2 == num3:
    print(f"{num1} + {num2} * {num3} = {num1 + num2 * num3}")
  else:
    print(f"{num1} + {num2} + {num3} = {num1 + num2 + num3}")


print("Result is")
calculate()

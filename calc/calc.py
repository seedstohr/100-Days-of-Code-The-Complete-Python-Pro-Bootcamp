import art

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def div(n1, n2):
    return n1 / n2

def mult(n1, n2):
    return n1 * n2

operations = {
    "+": add,
    "-": sub,
    "/": div,
    "*": mult,
}

def calc():
   print(art.logo)
   user_choice = True
   num1 = float(input("first number "))

   while user_choice:
        print("+\n"
              "-\n"
              "*\n"
              "/\n")
        operator = input("pick and operation ")
        num2 = float(input("second number "))
   #     result = operations[operator](num1, num2)

        if operator == "/" and num2 == 0:
            result = "infinity"
        else:
            if num1 == "infinity" or num2 == "infinity":
                result = "infinity"
            else:
                result = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {result}")
        option = input(f"press y to calculate with {result} or n to start over ")
        if option == "y":
            num1 = result
        else:
            user_choice = False
            print("\n" * 100)
            calc()

calc()


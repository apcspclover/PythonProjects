
#Simple calculator


#init

#functions
def add(num1, num2):
    result = num1 + num2
    print(result)
def subtract(num1, num2):
    result = num1 - num2
    print(result)
def multiply(num1, num2):
    result = num1 * num2
    print(result)
def divide(num1, num2):
    result = num1 / num2
    print(result)
#main
def simple_calculator():
    print("Welcome to Simple Calculator")

    print("""1. Addition
    2. Subtract
    3. Multiply
    4. Divide
    5. Quit""")
    while True:
        print("Please choose an operation")
        option = int(input("1-5: "))
        if option == 1:
            num1 = int(input("Please enter the first number"))
            num2= int(input("Please enter the second number"))
            add(num1,num2)

        if option == 2:
            num1 = int(input("Please enter the first number"))
            num2= int(input("Please enter the second number"))
            subtract(num1,num2)

        if option == 3:
            num1 = int(input("Please enter the first number"))
            num2= int(input("Please enter the second number"))
            multiply(num1,num2)

        if option == 4:
            num1 = int(input("Please enter the first number"))
            num2= int(input("Please enter the second number"))
            divide(num1,num2)
        if option == 5:
            print("Thank you for using Simple Calculator")
            break

simple_calculator()




# def calculator():
#     try:
#         number1 = float(input("Please enter the first number: "))
#         operation = input("Please enter the operation to perform (+,-,*,/,**): ")
#         number2 = float(input("Please enter the second number: "))
#     except:
#         print("invalid input")



#     if operation == "+":
#         result = number1 + number2
#     elif operation == "-":
#         result = number1 - number2
#     elif operation == "*":
#         result = number1 * number2
#     elif operation == "/":
#         result = number1 / number2
#     elif operation =="**":
#         result = number1 ** number2
#     else:
#         return "invalid operation"
#     return result

# print(calculator())

#--------another way to do it---------

def show_menu():
    print("\n----calculator----")
    print("1. addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")
    print("5. quit")

def add():
    num1 = float(input("enter your first number: "))
    num2 = float(input("enter your second number: "))
    result = num1 + num2 
    print(result)

def sub():
    num1 = float(input("enter your first number: "))
    num2 = float(input("enter your second number: "))
    result = num1 - num2 
    return result 

def multi():
    num1 = float(input("enter your first number: "))
    num2 = float(input("enter your second number: "))
    result = num1 * num2
    return result

def divi():
    num1 = float(input("enter your first number: "))
    num2 = float(input("enter your second number: "))
    result = num1 / num2
    return result





def main():
    while True :
        show_menu()
        choice = input("choose an operation: ")
        

        if choice == "1":
            add()
        elif choice == "2":
            sub()
        elif choice == "3":
            multi()
        elif choice == "4":
            divi()
        elif choice == "5":
            print("goodbye")
            break
        else:
            print("invalid choice, enter your choice again:")
            continue

main()






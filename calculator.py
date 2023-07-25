print("enter the choice")
print("1 addition")
print("2 subtraction")
print("3 division")
print("4 multiplication")
while True:
    choice = input("enter the choice:")
    num1 = int(input("enter the first number:-"))
    num2 = int(input("entre the second number:-"))
    def addition(num1,num2):
        ss = (num1 + num2)
        print(ss)
    def subtraction(num1,num2):
        ss = (num1 - num2)
        print(ss)
    def division(num1,num2):
        ss = (num1 / num2)
        print(ss)
    def multiplication(num1,num2):
        ss = (num1 + num2)
        print(ss)
    if choice == '1':
        addition(num1,num2)
    elif choice == '2':
        subtraction(num1,num2)
    elif choice == '3':
        division(num1,num2)
    elif choice == '4':
        multiplication(num1,num2)
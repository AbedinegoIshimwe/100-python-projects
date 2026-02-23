print("1- Addition")
print("2- Subtraction")
print("3- Multiplication")
print("4- Division")
operation = int (input("Choose an operation: "))

if operation in [1,2,3,4]:
    num1= int(input("Enter first number: "))
    num2= int(input("Enter second number: "))

    if(operation == 1):
        result = num1 + num2
    elif(operation == 2):
        result = num1 - num2
    elif(operation == 3):
        result = num1 * num2
    elif(operation == 4):
        result = num1 // num2
else:
    print("Invalid operation entered")

print( "The result is {}".format(result))
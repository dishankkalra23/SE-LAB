import addition
import sub
import multiply
import divide
import mod

print("1.Addition\n2.Subtraction\n3.Division\n4.Multiplication\n5.Modulus")
command = int(input("\nEnter your choice(number): "))

def takingInput():
    num1 = float(input("\nEnter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1,num2

if command== 1:
    num1,num2 = takingInput()
    result = addition.add(num1,num2)
    print("Sum: ",result)

elif command== 2:
    num1,num2 = takingInput()
    result = sub.subtraction(num1,num2)
    print("Subtraction: ",result)

elif command== 3:
    num1,num2 = takingInput()
    result = divide.divide(num1,num2)
    print("Division: ",result)

elif command== 4:
    num1,num2 = takingInput()
    result = multiply.multiply(num1,num2)
    print("Multiplication: ",result)

elif command== 5:
    num1,num2 = takingInput()
    result = mod.mod(num1,num2)
    print("Remainder: ", result)
    
else:
    print("Invalid Command")

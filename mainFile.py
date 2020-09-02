import addition
import sub
import multiply
import divide
import mod

print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus")
command = int(input("\nEnter your choice(number): "))

num1 = int(input("\nEnter the first number: "))
num2 = int(input("Enter the second number: "))

if command== 1:
    result = addition.add(num1,num2)
    print("Sum: ",result)

elif command== 2:
    result = sub.subtraction(num1,num2)
    print("Subtraction: ",result)

elif command== 3:
    result = divide.divide(num1,num2)
    print("Division: ",result)

elif command== 4:
    result = multiply.multiply(num1,num2)
    print("Multiplication: ",result)

elif command== 5:
    result = mod.mod(num1,num2)
    print("Remainder: ", result)
    
else:
    print("Invalid Command")
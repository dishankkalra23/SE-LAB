import addition
import sub
import multiply
import divide
import mod shrey

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Enter - 1. to  add, 2. to subtract, 3. to divide, 4. to multiply, 5. to mod")

command = int(input("Enter the command to do add,subtract,divide,multiply,mod"))

if command== 1:
    result = addition.add(num1,num2)
    print("Sum of num1 and num2: ",result)

elif command== 2:
    result = sub.subtraction(num1,num2)
    print("Subtract of num1 and num2: ",result)

elif command== 3:
    result = divide.divide(num1,num2)
    print("Division of num1 and num2: ",result)

elif command== 4:
    result = multiply.multiply(num1,num2)
    print("Multiplication of num1 and num2: ",result)

elif command== 5:
    result = mod shrey.mod(num1,num2)
    print("Multiplication of num1 and num2: ",result)
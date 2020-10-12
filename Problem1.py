#Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, 
#also create a lambda function that multiplies argument x with argument y and print the result.

addition = lambda x: x + 15
multiplication = lambda x, y: x * y

print(addition(int(input("Insert value to be added by 15! "))))
x = int(input("Insert one of the value to be multiplied with! "))
y = int(input("Insert the other value to be multiplied with! "))
print(multiplication(x, y))
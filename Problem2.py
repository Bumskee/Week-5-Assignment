#Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
import random
value = lambda x: x * (random.randint(0, 1000))
print(value(int(input("Insert a number to be multiplied with a mistery number! "))))
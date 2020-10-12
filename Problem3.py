#Write a Python program to sort a list of tuples using Lambda.
"""I dont really understand the question (What kind of tuple inside the list? so i am just assuming that the we need to sort the tuples based on 
the sum of the elements inside the tuple)"""

list = [(0, 2), (2, 18), (100, 300), (0, 0, 0), (2, 9, 18)]
list.sort(key = lambda x: sum(x))

print(list)
#Write a Python program to create Fibonacci series upto n using Lambda

def fibseq(count):
    if count <= 0:
        sequence = "nothing"
    elif count == 1:
        sequence = [0]
    else:
        sequence = [0, 1]
        any(map(lambda _: sequence.append(sum(sequence[-2:])), range(2, count))) 
    return sequence

sequence = fibseq(int(input("Insert the limit for the fibonacci sequence generator! ")))
print(sequence)
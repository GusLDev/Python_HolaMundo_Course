n1 = input("Introduce the first number: ")
n2 = input("Introduce the second number: ")
#WE CAN CONVERT THE STRINGS TO INTEGERS WITH THIS SETENCE
n1 = int(n1)
n2 = int(n2)

add = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2

message = f"""
For the numbers introduced {n1} and {n2},
The result from addition is {add}
The result from subtraction is {sub}
The result from multiplication is {mult}
The result from division is {div}
"""
print(message)
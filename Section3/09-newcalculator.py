
print("Welcome to the calculator\nFor exit write \"exit\" In operation\n"+
      "The operations are add, mult, div, sub")
n1 = 0
while True:
    if n1 == 0:
        n1 = input("Introduce a number: ")
    operation = input("Introduce an operation: ")
    if operation.lower() == "exit":
        break
    n2 = input("Introduce a number: ")
    n1 = int(n1)
    n2 = int(n2)
    if operation.lower() == "add":
        result = n1 + n2
    elif  operation.lower() == "mult":
        result = n1 * n2
    elif  operation.lower() == "div":
        result = n1 / n2
    elif  operation.lower() == "sub":
        result = n1 - n2
    print("Operation Sucessfull this is the result: ",result)
    n1 = result
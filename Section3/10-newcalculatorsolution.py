print("Welcome to the calculator")
print("For exit write \"exit\"")
print("For the operations write add, sub, mult, div")

result = ""
while True:
    if not result:
        result = input("Introduce a number: ")
        if result.lower() == "exit":
            break
        result = int(result)
    op = input("Introduce operation: ")
    if op.lower() == "exit":
        break
    n2 = input("Introduce the next number: ")
    if n2.lower() == "exit":
        break
    n2 = int(n2)
    if op.lower() == "add":
        result += n2
    elif op.lower() == "sub":
        result -= n2
    elif op.lower() == "mult":
        result *= n2
    elif op.lower() == "div":
        result /= n2
    else:
        print("The operation is not valid")
        break
    print("The result from the operation is: ",result)

def long(text):
    result = 0
    for _ in text:
        result += 1
    return result
    
print("Test")  #We need a breakpoint for the debugger
l = long("Hello World")
print(l)
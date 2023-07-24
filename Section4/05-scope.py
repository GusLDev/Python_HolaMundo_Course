greeting = "Hello Global"    #Global Context
                             #Global Varibales are a bad practice

def  greetings():
    global greeting
    greeting = "Hello World"
    print(greeting)

def helloBudy():
    greeting = "Hello Budy"
    print(greeting)
    
print(greeting)
greetings()
print(greeting)


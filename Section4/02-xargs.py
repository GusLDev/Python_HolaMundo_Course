def add(*numbers):
    result = 0
    for number in numbers:
        result += number
    print(result)

add(5,5,1.1)
add(5,5,5)
add(5,5,5,5)
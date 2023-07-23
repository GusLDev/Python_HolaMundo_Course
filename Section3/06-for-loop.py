find = 10
for number in range(5): #Range is an  iterable you can use an array or a string
    print(number)
    if number == find:
        print("Founded",find)
        break
else:
    print("It wasnt Found")

for char in "Ultimate Python":
    print(char)
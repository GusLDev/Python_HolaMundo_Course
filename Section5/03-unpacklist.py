numbers = [1,2,3]

#UGLY!
#firstNumber = numbers[0]
#secondNumber = numbers[1]
#thirdNumber = numbers[2]

#first,second,third = numbers
#print(first,second,third)

numbers = [1,2,3,4,5,6,7,8,9]
first,second,*others,last = numbers
print(first,second,others,last)
def oddEven(digit):
    if digit % 2 == 0:
        print "Number is", num, ". This is an even number"
    else:
        print "Number is", num, ". This is an odd number"

num = 45
oddEven(num)

def multiply(numbers, times):
    for i in range(len(numbers)):
        numbers[i] *= times
    print numbers
    return numbers

numbers = [2,4,6,10]
times = 5
multiply(numbers, times)

def layeredMultiples (numbers, times):
    z = multiply(numbers, times)
    print z
    bigList = []
    for i in range(len(z)):
        bigList.append(z[i]*(1,))
    print bigList

numbers = numbers = [2,4,6,10]
times = 3
layeredMultiples(numbers,times)

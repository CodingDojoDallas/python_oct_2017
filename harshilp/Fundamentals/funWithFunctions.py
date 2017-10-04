#Odd even function
def odd_even():
    for i in range(1,2001):
        if i % 2 == 0:
            print "Number is " + str(i) + ". This is an even number." 
        else:
            print "Number is " + str(i) + ". This is an odd number."

odd_even()

#Multiply function
def multiply (arr, mult):
    for i in range(len(arr)):
        arr[i] = arr[i] * mult
    return arr

print multiply([1,2,3,4], 5)

#Hacker
def hacker(arr):
    y=[]
    for i in range(len(arr)):
        y.append([1]*arr[i])
    return y
print hacker(multiply([1,2,3,4], 2))
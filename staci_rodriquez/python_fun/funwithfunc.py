def odd_even():
    for i in range(1,2001):
        if i%2 == 0:
            print "Number is " + str(i) + ". This is an even number."
        else:
            print "Number is " + str(i) + ". This is an odd number."


def multiply(list, multiple):
    b = [a * multiple for a in list]   
    return b


def layered_multiples(arr):
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(x):
            val_arr.append(1)
        new_array.append(val_arr)

    return new_array

a = [2,4,10,16]   

odd_even()
print (multiply(a, 5))
x = layered_multiples(multiply([2,4,5],3))
print x
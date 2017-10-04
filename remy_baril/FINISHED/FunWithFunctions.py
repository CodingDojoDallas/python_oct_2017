def odd_even ():
    for i in range (1,2001):
        if (i % 2 == 0):
            print 'Number is', i, 'This is an even number.'
        else:
            print 'Number is', i, 'This is an odd number.'

odd_even()

def multiply(a,b):
    c = []
    c = [i*5 for i in a]
    print c

multiply([1,2,3],5)
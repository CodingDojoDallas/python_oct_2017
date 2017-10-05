for i in range (100 , 100001):
    prime = True
    sq = False
    for j in range(2, i):
        if i%j == 0:
            prime = False
        if j * j == i:
            sq = True
    if prime == False and sq == False:
        print str(i) + "foobar"
    elif prime == True:
        print str(i) + "foo"
    elif sq == True:
        print str(i) + "bar"
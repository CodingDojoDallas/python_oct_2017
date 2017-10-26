import random
print "Starting the Program"
for i in range(0, 5001, 1):
    print i
    new_list = []
    new_list.append(i)
    print new_list
    print "Attempt #"
    print i
    print "Throwing a coin..."
    random_var = random.randint(1, 2)
    print random_var
    x = 0
    y = 0
    if random_var == 1:
        print "It's a head! ... Got"
        print x
        print "head(s) so far and"
        print y
        print "tail(s) so far"
        x += 1
        print x
    else:
        print "It's a tail! ... Got"
        print x
        print "head(s) so far and"
        print y
        print "tail(s) so far"
        y += 1
        print y

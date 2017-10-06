def typeList(arr):
    stg = ''
    sum = 0
    for i in range(len(arr)):
        if isinstance(arr[i], float) or isinstance(arr[i], int):
            sum += arr[i]
        elif isinstance(arr[i], basestring):
            stg += arr[i] + " "
    if sum == 0:
        print "This list is purely of type string."
        print "String: " + stg
    elif len(stg) == 0:
        print "This list is purely numbers."
        print "Sum: " + str(sum)
    else:
        print "This list is a mixed list."
        print "String: " + stg
        print "Sum: " + str(sum)

l = ['magical unicorns',19,'hello',98.98,'world']
typeList(l)
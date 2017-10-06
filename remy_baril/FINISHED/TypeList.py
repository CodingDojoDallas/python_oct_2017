def typelist(input):
    rtype = 0
    rsum = 0
    rstring = ""
    for x in range(0,len(input)):
        if type (input[x]) == int or type(input[x]) == float:
            rsum += input[x]
        if type (input[x]) == str:
            rstring += input[x] + " "
    if rsum > 0 and len(rstring) > 0:
        print "The list you typed is mixed."
    elif rsum > 0 and len(rstring) == 0:
        print "The list you type is numbers-only."
    elif rsum == 0 and len(rstring) > 0:
        print "The list you typed is words-only."
    print "The strings are:", rstring
    print "The sum is:", rsum


typelist(["Pugs",1,2,1,2,"Ice cream"])
        

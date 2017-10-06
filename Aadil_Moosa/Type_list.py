# l = ['magical unicorns',19,'hello',98.98,'world']
 
# for x in l:
#     if type(x) == str:
#         print "is string"
#     elif type(x) == int:
#         print "is integer"
#     elif type(x) == float:
#         print "is decimal"

ListA = ['magical unicorns',19,'hello',98.98,'world']
ListB = [2,3,1,7,4,12]
ListC = ['magical','unicorns']

def typeList(Output):
    InitialString = ""
    InitialSum = 0
    IsInteger = False

    for x in Output:
        if type(x) == int:
            InitialSum += x
            IsInteger = True
        elif type(x) == float:
            InitialSum += x
            IsInteger = True
        else:
            InitialString += x + " "

    
    
    if len(InitialString) > 0 and IsInteger != True:
        print "The list you have entered is of string type."
    elif IsInteger == True and InitialString == "":
        print "The list you have entered is of Integer type."
    elif IsInteger == True and InitialString == "":
        print "There is nothing"
    else:
        print "The list you have entered is of mixed type"
    


    if len(InitialString) > 0:
        print InitialString
    if IsInteger == True:
        print InitialSum


print "ListA:"
typeList(ListA)

print "ListB:"
typeList(ListB)

print "ListC:"
typeList(ListC)


# Bruh this took forever
a = ['magical unicorns',19,'hello',98.98,'world']
b = [2,3,1,7,4,12]
c = ['magical','unicorns']
d = []

def typelist(pist):
    total = 0
    isint = False
    newstring = ""
    for element in pist:
        if type(element) == int:
            total += element
            isint = True
        elif type(element) == float:
            total += element
            isint = True
        else:
            newstring = newstring + element + " "

    if len(newstring) > 0 and isint != True:
        print "The list you entered is of string type"
    elif isint == True and newstring == "":
        print "The list you entered is of integer type"
    elif isint != True and newstring == "":
        print "You didn't enter anything! Please go back and put something!"
    else:
        print "The list you entered is of mixed type"

    if len(newstring) > 0:
        print newstring
    if isint == True:
        print total

typelist(a)
typelist(b)
typelist(c)
typelist(d)
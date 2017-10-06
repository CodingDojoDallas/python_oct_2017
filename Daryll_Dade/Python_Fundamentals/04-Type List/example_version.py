list = ["pegasus", 88, "unicorn", 10.4]
sum = 0
string = ""

for x in list:
    if isinstance(x, basestring):
        string += " " + x
    elif isinstance(x, int):
        sum += x

"""MAKE THIS RUN THROUGH ENTIRE LIST BEFORE PRINTING
firstitem = list[0]
for x in list:
    if (type(x) != type(firstitem)):
        print "This is a mixed-type list."
    elif //(isinstance(firstitem, basestring)):
        print "This is a list of strings."
    elif (isinstance(firstitem, int)):
        print "This is a list of integers."
"""

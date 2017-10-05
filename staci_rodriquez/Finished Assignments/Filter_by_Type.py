sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

def testValue(value):
    if type(value) == int:
        if value >= 100:      #Integer
            print "That's a big number!"
        else:
            print "That's a small number"
    if type(value)==str:
        if value >=50:      #String
            print "Long sentence"
        else:
            print "Short sentence"
    if type (value) == list:
        if value >=10:      #List
            print "Big list"
        else:
            print "Short list"

testValue(sI)
testValue(mI)
testValue(bI)
testValue(eI)
testValue(spI)
testValue(sS)
testValue(mS)
testValue(bS)
testValue(eS)
testValue(aL)
testValue(mL)
testValue(lL)
testValue(eL)
testValue(spL)


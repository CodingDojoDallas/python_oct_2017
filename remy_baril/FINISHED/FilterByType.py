def filter(input): 
    if input >= 100 and isinstance(input,int):
        print "That's a big number!"
    elif input < 100 and isinstance(input, int):
        print "That's a small number"
    elif len(input) >= 50 and isinstance(input, str):
        print "Long sentence"
    elif len(input) < 50 and isinstance(input,str):
        print "Short sentence"
    elif len(input) >= 10 and isinstance(input,list):
        print "Big list!"
    elif len(input) < 10 and isinstance(input,list):
        print "Short list"

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

filter(sI)
filter(mI)
filter(bI)
filter(eI)
filter(spI)
filter(sS)
filter(mS)
filter(bS)
filter(eS)
filter(aL)
filter(mL)
filter(lL)
filter(eL)
filter(spL)
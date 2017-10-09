

def tupIn(myDict):
    newString = []
    for key,value in myDict.items():
        temp = (key,value)
        newString.append(temp)
    print newString

myDict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

tupIn(myDict)

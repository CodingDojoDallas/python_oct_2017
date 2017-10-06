myDict = {"name":"Harshil", "age":22, "country of birth":"USA", "favorite language":"Python"}
def dictionary(myDict):
    for key,data in myDict.iteritems():
        print "My " + key + " is " + str(data)
dictionary(myDict)
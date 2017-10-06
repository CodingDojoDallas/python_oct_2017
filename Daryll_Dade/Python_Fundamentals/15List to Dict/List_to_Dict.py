name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

"""def make_dict(arr1, arr2):
    new_dict = {}
    compare = [len(arr1),len(arr2)]
    if (max(compare) == compare[0]):
        keyslist = arr1
    else:
        keylist = arr2
    if (min(compare) == compare[1]):
        valueslist = arr1
    else:
        valueslist = arr2
    for x in range (0,len(keyslist)):
        new_dict += keyslist[x]:valueslist[x]
    return new_dict"""

def make_dict(arr1, arr2):
    newdict = {}
    if len(arr1) >= len(arr2):
        newdict = dict.fromkeys(arr1,arr2)
    if len(arr2) < len(arr1):
        newdict = dict.fromkeys(arr2,arr1)
    print newdict
    i = 0
    for c in newdict:
        newdict[c] = arr2[i]
        i += 1
    print newdict


make_dict(name, favorite_animal)

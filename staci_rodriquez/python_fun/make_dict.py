def makeDict(lst1,lst2):
    new_dict = {}
    new_dict = dict(zip(lst1,lst2))
    print new_dict
    return new_dict

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

makeDict(name,favorite_animal)
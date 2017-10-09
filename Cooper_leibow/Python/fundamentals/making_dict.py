def make_dict(name, favorite_animal):
    new_dict = zip(name, favorite_animal)
    dict(new_dict)
    print new_dict
    return new_dict

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

make_dict(name, favorite_animal)

def dicaroo(name, favorite_animal):
    if len(name) > len(favorite_animal):
        make_dict(name, favorite_animal)
    elif len(name) < len(favorite_animal):
        new_dict = zip(favorite_animal, name)
        dict(new_dict)
        print new_dict
    else :
        make_dict(name, favorite_animal)

name = ["Anna", "Eli", "Pariece", "Brendan"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks"]

dicaroo(name, favorite_animal)

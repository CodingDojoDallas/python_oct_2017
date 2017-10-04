name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(keys, vals):
    return dict(zip(keys, vals))

print make_dict(name,favorite_animal)

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "dogs"]

def make_dict_challenge(arr1, arr2):
    if len(arr1) > len(arr2):
        return dict(zip(arr1[:len(arr2)], arr2))
    else:
        return dict(zip(arr2[:len(arr1)], arr1))

print make_dict_challenge(name, favorite_animal)
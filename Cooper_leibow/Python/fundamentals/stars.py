def drawStars(numbers):
    for i in range(len(numbers)-1):
        newString = ""
        newString += ("*" * numbers[i])
        print

numbers = [4, 6, 1, 3, 5, 7, 25]
drawStars(numbers)



def starsAndWords(words):
    for i in range(len(words)-1):
        if type(words[i]) == int:
            print ("*" * words[i])
        elif type(words[i]) == str:
            letter = (words[i][0])
            print (letter * len(words[i])).lower()


words = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
starsAndWords(words)

word_list = ['hello','world','my','name','is','Anna']
char = 'o'

def findO(wl, ch):
    newList = []
    for element in wl:
        for elem in element:
            if ch == elem:
                newList.append(element)

    print newList

findO(word_list, char)


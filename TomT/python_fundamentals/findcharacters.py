word_list = ['hello','world','my','name','is','Anna']
char = 'o'
char2 = 'a'

def findcharacter(wl, ch):
    new_list = []    
    for element in wl:
        for elem in element:
            if elem==ch:
                new_list.append(element)
    print new_list

findcharacter(word_list, char)
findcharacter(word_list, char2)
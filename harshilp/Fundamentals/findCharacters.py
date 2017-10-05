def findChar (str, char):
    newStr =[]
    for i in range(len(str)):
        if str[i].find(char) != -1:
            newStr.append(str[i])

    print newStr

word_list = ['hello','world','my','name','is','Anna']
char = 'o'

findChar(word_list,char)
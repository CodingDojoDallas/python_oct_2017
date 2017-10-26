def find_characters(word_list, char):
    new_list = ""
    for i in range(len(word_list)):
        for x in range(len(word_list[i])):
            if word_list[i][x] == char:
                new_list += " {}".format(word_list[i])
    print new_list

word_list = ['hello','world','my','name','is','Anna']
char = "o"
find_characters(word_list, char)

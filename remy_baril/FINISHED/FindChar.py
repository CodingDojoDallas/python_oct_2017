word_list = ['hello','world','my','name','is','Anna']
for i in range (0, len(word_list), 1):
    if any (x == 'o' for x in word_list[i]):
        print word_list[i]
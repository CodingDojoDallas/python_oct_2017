def integer(num):
    if num >= 100:
        print "Thats a big number!"
    else:
        print "Thats a small number!"

num = 15
integer(num)

def fifty(string):
    if len(string) >= 50:
        print "Long sentence"
    else :
        print "Short sentence"

string = "tybb"
fifty(string)


def list(data_set):
    print type(data_set)
    if type(data_set) == int:
        if data_set >= 10:
            print "Thats a big number!"
        else:
            print "Thats a small number!"
    elif type(data_set) == str:
        if len(data_set) >= 10:
            print "Long sentence"
        else:
            print "Short sentence"
    else:
        print "Idk"

sI = 45
text = "r"
list(sI)

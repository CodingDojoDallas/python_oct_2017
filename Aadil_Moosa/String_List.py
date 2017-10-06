string = "It's thanksgiving day. It's my birthday,too!"
print string.find("day")
string = string.replace("day", "month", 1)
print string


x = [2,54,-2,7,12,98]
print x
print max(x)
print min(x)


x2 = ["hello",2,54,-2,7,12,98,"world"]
print x2
print x2[0]
print x2[len(x2)-1]
x2_5 = [x2[0], x2[-1]]
print x2_5


x3 = [19,2,54,-2,7,12,98,32,10,-3,6]
print x3
x3.sort()
print x3
List_One = x3[:len(x3)/2]
print List_One
List_Two = x3[len(x3)/2:]
print List_Two
List_Two.insert(0, List_One)
print List_Two
# List_Two[0:0] = List_One
# print List_Two
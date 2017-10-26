

str = "If monkeys like bananas, then I must be a monkey!"
print str.replace("monkeys", "Alligator", 1)

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

y = ["hello",2,54,-2,7,12,98,"world"]
print y[0],y[7]

z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort()
print z
w = z[0:5]
print w
z.pop(0)
z.pop(1)
z.pop(2)
z.pop(3)
z.pop(4)
z.pop(5)
print z
z.insert(0,w)
print z
#my_list = z.slice[0:5]
#print my_list

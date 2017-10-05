words = "It's thanksgiving day. It's my birthday, too!"
print words.find ('day')
print words.replace ('day', 'month')

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

y = ['hello',2,54,-2,7,12,98,'world']
first_item = y[0]
last_item = y[len(y)-1]
print first_item + " " + last_item
new_list = [first_item, last_item]
print new_list

z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort()
print z
newZ = z[0:len(z)/2]
newZ2 = z[len(z)/2-1:]
newZ2[0] = newZ
print newZ2

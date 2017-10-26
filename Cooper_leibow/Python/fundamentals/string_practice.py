words = "It's thanksgiving day. It's my birthday, too!"
position = words.find("day")
print position

x = [2,54,-2,7,12,98]
lowest = min(x)
print lowest

highest = max(x)
print highest

y = ["hello",2,54,-2,7,12,98,"world"]
print y[0]
print y[len(y)-1]

only = [y[0],y[len(y)-1]]
print only

z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort()
print z
smaller = z[:len(z)/2]
print smaller
bigger = z[(len(z)/2)-1:]
print bigger
final = bigger
final[0]=smaller
print final

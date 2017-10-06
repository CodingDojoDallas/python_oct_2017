#Find and Replace
words = "It's thanksgiving day. It's my birthday, too!"
word = "day"
replace = "month"
print words.find(word)
print words.replace(word, replace)

#Min and Max
x = [2,54,-2,7,12,98]
print min(x)
print max(x)

#First and Last
x = ["hello",2,54,-2,7,12,98]
print x[0]
print x[len(x)-1]
y=[]
y.append(x[0])
y.append(x[len(x)-1])
print y

#New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
y= [0] + x[((len(x)-1)/2):]
y[0] = x[:((len(x)-1)/2)]
print x
print y
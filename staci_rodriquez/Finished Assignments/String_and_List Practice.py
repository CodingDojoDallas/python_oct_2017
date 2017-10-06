#Find and Replace
words = "It's thanksgiving day. It's my birthday,too!"
print words.find('day')
print words.replace('day','month',1)

#Min and Max
x = [2,54,-2,7,12,98]
print max(x)

x = [2,54,-2,7,12,98]
print min(x)

#First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0],x[7]

#New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
length=len(x)
firstset=x[0:length/2]
lastset=x[length/2:len(x)]
lastset.insert(0,firstset)
print lastset


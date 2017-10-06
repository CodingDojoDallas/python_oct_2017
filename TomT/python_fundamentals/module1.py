#Find and Replace
words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day")
newstring = words.replace("day", "month") 
newstring = words.replace("day", "month",1)

#Min and Max
x = [2,54,-2,7,12,98]
minimum=x[0]
for count in x:
    minimum=min(count,minimum)
    print minimum

x = [2,54,-2,7,12,98]
maximum=x[0]
for i in range(len(x)):
    maximum = max(x[i], maximum)
    print maximum

#First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
first = x[0]
last = x[len(x)-1]
print first + " " +last
newlist = first + last

#New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
length=len(x)
firstel=x[0:length/2]
lastel=x[length/2:len(x)]
lastel.insert(0,firstel)
print lastel

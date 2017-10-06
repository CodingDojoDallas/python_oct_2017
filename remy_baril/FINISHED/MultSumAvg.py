''' MULTIPLES '''
for x in range(1,1000):
    if x % 2 != 0:
        print x

''' MULTIPLES OF 5 '''
for x in range (5,1000000,5):
    print x
    
''' SUM '''
a = [1,2,5,10,255,3]
count = 0
for x in range(0,len(a)):
    count += a[x]
    print count

''' AVG '''
avg = sum(a)/len(a)
print avg

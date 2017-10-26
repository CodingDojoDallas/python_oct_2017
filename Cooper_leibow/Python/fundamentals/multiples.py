for count in range(0,1000):
    if count % 2 !=0:
        print count

for count in range(5,1000001):
    if count % 5 == 0:
        print count

a = [1,2,4,10,255]
total = 0
for i in range(0,5):
    total += a[i]
print total

def average(a):
    total = 0
    for i in range (len(a)):
        total += a[i]
    total /= len(a)
    return total

a = [1,2,5,10,255,3]

print average (a)

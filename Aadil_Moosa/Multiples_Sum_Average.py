# All even numbers
# for x in range(0, 1000):
#     if (x % 2 == 0):
#         # print x

# # All odd numbers
# for x in range(0, 1000):
#     if (x % 2 != 0):
#         # print x

# # All multiples of 5
# for x in range(0, 1000000):
#     if (x % 5 == 0):
#         # print x

for x in range(0, 1000):
    if (x % 2 ==0):
        print x

for x2 in range(0, 1000000):
    if (x2 % 5 == 0):
        print x2



a = [1, 2, 5, 10, 255, 3]
s = 0
for x in a:
    s += x
print s



a2 = [1, 2, 5, 10, 255, 3]
s = 0
for x in a2:
    s += x
s /= len(a2)
print s
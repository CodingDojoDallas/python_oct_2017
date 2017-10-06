"""This module does stuff."""
for x in range(1, 1000, 2):
    print x

# for y in range(5, 1000000, 5):
#     print y


A = [1, 2, 5, 10, 255, 3]

smofa = 0

for s in A:
    smofa = smofa + s

print smofa

avofa = smofa / len(A)

print avofa
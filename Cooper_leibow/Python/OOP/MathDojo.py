import md

print md.add(2,5)
print md.add(2,3)
print md.subtract(5,8)

class Numbers(object):
    def __init__(self):
        self.result = 0

    def add(self, a1, *a):
        self.result += a1
        print self.result
        return self.result

numbers1 = Numbers(1,4,7,19)
numbers1.add()

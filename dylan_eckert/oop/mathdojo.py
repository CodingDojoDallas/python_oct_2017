class MathDojo(object):
    """docstring for MathDojo."""
    def __init__(self, number):
        self.number = number

    def dispNum(self):
        print "Starting Number: {}".format(self.number)
        return self

    def add(self, num1, *nums):
        self.num1 = num1
        self.number += self.num1.join(nums)
        return self

md = MathDojo(1)
md.add(1, 2, 3).dispNum()

# I suck at math stuff and this assignment doesn't teach me anything new it just makes me do math which I suck at so look at all of the other assignments in this course if you really want to see me understand how OOP works. 

class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *args):
        for i in args:
            if type(i) == list or type(i) == tuple:
                for k in i:
                    self.result += k
            else:
                self.result += i
        return self

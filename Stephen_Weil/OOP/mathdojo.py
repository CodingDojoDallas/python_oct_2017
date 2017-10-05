# Part I - create class MathDojo with methods add and subtract
class MathDojo(object):
    
    def __init__(self, start):
        self.result = start
    
    def add(self, *nums):
        self.result += sum(nums)
        return self

    def subtract(self, *nums):
        self.result -= sum(nums)
        return self

md = MathDojo(0)
print md.add(2).add(2,5).subtract(3,2).result

# Part II - modify to take at least one integer(s) and/or list(s) as parameter
class MathDojoTwo(object):

    def __init__(self, start):
        self.result = start
    
    def add(self, *nums):
        for item in nums:
            if isinstance(item, int) or isinstance(item, float):
                self.result += item
            elif isinstance(item, list):
                self.result += sum(item)
            else:
                print "Invalid data type - only numbers or lists please."
        return self

    def subtract(self, *nums):
        for item in nums:
            if isinstance(item, int) or isinstance(item, float):
                self.result -= item
            elif isinstance(item, list):
                self.result -= sum(item)
            else:
                print "Invalid data type - only numbers or lists please."
        return self

md2 = MathDojoTwo(0)
print md2.add([1], 3, 4).add([3, 5, 7, 8], [2, 4, 3, 1.25]).subtract(2, [2, 3], [1, 1, 2, 3]).result

# Part III - support tuples of values in addition to lists

class MathDojoThree(object):
    
    def __init__(self, start):
        self.result = start
    
    def add(self, *nums):
        for item in nums:
            if isinstance(item, int) or isinstance(item, float):
                self.result += item
            elif isinstance(item, list) or isinstance(item, tuple):
                self.result += sum(item)
            else:
                print "Invalid data type - only numbers or lists please."
        return self

    def subtract(self, *nums):
        for item in nums:
            if isinstance(item, int) or isinstance(item, float):
                self.result -= item
            elif isinstance(item, list) or isinstance(item, tuple):
                self.result -= sum(item)
            else:
                print "Invalid data type - only numbers or lists please."
        return self

md3 = MathDojoThree(0)
print md3.add(1, [2, 3], (4, 5, 6)).subtract(4, (1, 2), [1]).result
class MathDojo(object):
    def __init__(self):
        self.sum = 0

    def add(self, *num):
        for i in num:
            if isinstance(i, list) or isinstance(i, tuple):
                self.sum += sum(i)
            elif isinstance(i, int) or isinstance(i, float): #ignores strings and dicts
                self.sum += i
        return self
    
    def subtract(self, *num):
        for i in num:
            if isinstance(i, list) or isinstance(i, tuple):
                self.sum -= sum(i)
            elif isinstance(i, int) or isinstance(i, float):
                self.sum -= i
        return self

    def result(self):
        print self.sum
        return self

md = MathDojo()
md.add(2).add(2,5).subtract(3,2).result()
md2 = MathDojo()
md2.add([1], 3,4).add((3,5,7,8), [2,4.3,1.25]).subtract(2, (2,3), [1.1,2.3]).add(2.2).result()
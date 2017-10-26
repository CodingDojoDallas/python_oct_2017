class mathdojo(object):
    def __init__(self):
        self.result=0
    def add(self, *nums):
        for num in nums:
            if type(num) == list or type(num) == tuple:
                for k in num:
                    self.result += k
            else:
                self.result += num
        return self
    def subtract(self, *nums):
        for num in nums:
            if type(num) == list or type(num) == tuple:
                for k in num:
                    self.result += k
            else:
                self.result += num
        return self

# md = mathdojo()
print mathdojo().add(1,4).add(1,3).subtract(1, 1).result

# md.mathdojo().add(2).add(2,5).subtract(3,2).result

class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *nums):
        for num in nums:
            if type(num) == list or type (num)== tuple:
                for number in num:
                    self.result += number
                else:
                    self.result += number
                return self
    def subtract(self, *nums):
        for num in nums:
            if type(num) == list or type(num) == tuple:
                for number in num:
                    self.result -= number
            else:
                self.result -= number
        return self

print MathDojo().add(5,20).result

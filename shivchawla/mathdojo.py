class MathDojo(object):
    def __init__(self):
        self.sum = 0

    def add(self,*arg): #If you have multiple arguments, it becomes a tuple
        for x in arg:
            if type(x) == tuple:
                for i in x: #This is where you loop through the tuple that's created using "i" which takes each value in the tuple (like a list)
                    self.sum += i #This is essentially adding each arg (set as i in the loop) to the greater sum
            elif type(x) == list:
                for i in x: #This is where you loop through the tuple that's created using "i" which takes each value in the tuple (like a list)
                    self.sum += i
            elif type(x) == int:
                self.sum += x
            elif type(x) == float:
                self.sum += x
        return self

    def subtract(self,*arg):
        for x in arg:
            if type(x) == tuple:
                for i in x: 
                    self.sum -= i 
            elif type(x) == list:
                for i in x: 
                    self.sum -= i
            elif type(x) == int:
                self.sum -= x
            elif type(x) == float:
                self.sum -= x
        return self

    def result(self):
        print self.sum
        return self

md = MathDojo()
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()
    


class MathDojo(object):

    def __init__(self):
        self.result = 0

    def add(self, *args):

        for arg in args:
            if isinstance(arg, list or tuple):
                for item in arg:
                    self.result += item
            else:
                self.result += arg
        return self

    def subtract(self, *args):
        for arg in args:
            if isinstance(arg, list or tuple):
                for item in arg:
                    self.result -= items
            else:
                self.result -= arg
        return self

print 'C'

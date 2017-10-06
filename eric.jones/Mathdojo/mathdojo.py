class MathDojo(object):

    def __init__(self):
        self.result = 0

    def add(self, arg1, *arg2):
        self.result += arg1
        for idx in list(self.recursetree(arg2, (list, tuple))):
            self.result += idx
        return self

    def subtract(self, arg1, *arg2):
        self.result -= arg1
        for idx in list(self.recursetree(arg2, (list, tuple))):
            self.result -= idx
        return self

    def recursetree(self, tuplemix, datatypes):
        if isinstance(tuplemix, datatypes):
            for value in tuplemix:
                for subvalue in self.recursetree(value, datatypes):
                    yield int(subvalue)
        else:
            yield int(tuplemix)

md = MathDojo()
print md.add(5, (6,7), [1, 4, 9, (3, [5, 7, (11, 18)])]).subtract(8, [-1, -4, (3, 5)]).result
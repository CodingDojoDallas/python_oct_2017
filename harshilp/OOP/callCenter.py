class Call(object):
    def __init__(self, id, name, number, time, reason):
        self.id = id
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason

    def display(self):
        print "ID: " + str(self.id)
        print "Name: " + self.name
        print "Number: " + str(self.number)
        print "Time: " + str(self.time)
        print "Reason: " + self.reason
        print "~~~~~~~~~~~~~~~~"
        return self

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.size = 0

    def add(self, call):
        self.calls.append(call)
        self.size += 1
        return self
    
    def remove(self):
        self.calls = self.calls[1:]
        self.size -= 1
        return self
    
    def info(self):
        print "The current queue is " + str(self.size) + " call(s) long!"
        for i in self.calls:
            print i.name + " " + str(i.number)
        return self

    def removeCall(self, call):  #ninja level
        for i in self.calls:
            if i.number == call.number:
                self.calls.remove(i)
                self.size -= 1
        return self

    def sort(self):  # hacker level
        self.calls = sorted(self.calls, key = lambda k: k.time)
        return self

call1 = Call(1, "Ade", 200, 1200, "For fun")
call2 = Call(2, "Lee", 206, 100, "Support")

cc = CallCenter()
cc.add(call1).info()
cc.add(call2).info()
#cc.removeCall(call1).info()
cc.sort().info()

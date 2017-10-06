class Call():
    def __init__(self,ID,caller_name,time,reason):
        self.ID = ID
        self.caller = caller_name
        self.time = time
        self.reason = reason
    def display(self):
        print "ID: " + self.ID
        print "Caller Name:" + self.caller
        print "Time of call: " + self.time
        print "Reason for call: " + self.reason

Call("01","Bob","9:00 PM","Flat Tire.").display()

class callCenter():
    def __init__(self,call):
        self.call = call
        self.queue = len(self.call)
    def add(self):
        self.call.append(self.call[len(self.call)-1]+1)
        return self
        #Why doesn't this work?
    def remove(self):
        self.call.remove(self.call[0])
        return self
        #why doesn't this work?
    def info(self):
        print str(self.queue) + " calls in the queue."
        return self

callCenter([1,2,3]).remove().info()

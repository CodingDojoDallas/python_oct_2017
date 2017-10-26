class Call():
    def __init__(self, id1, name, phone_number, time, reason):
        self.id1 = id1
        self.name = name
        self.phone = phone_number
        self.time = time
        self.reason = reason

    def display(self):
        print "ID:" + self.id1
        print "Name:" + self.name
        print "Phone:" + self.phone
        print "Time of Call" + self.time
        print "Reason for call:" + self.reason
#        print len(self.call)
# Call("01", "Sean", "55555555555", "7:00 AM", "Flat Tire").display()

class CallCenter():
    def __init__(self):
        self.queue = []
#        print len(self.call)

    def add(self, call):
        print "Adding a call to queue"
        if len(self.queue) < 2: # 2 = maximum capacity
            self.queue.append(call)
            print "You are call {} in queue.".format(len(self.queue))
        else:
            print "All Lines are busy now."
        return self


    def remove(self, call):
        print "Removing a call from queue"
        self.queue.remove(self.queue[0])
        return self

    def info(self):
        print str(len(self.queue)) + " call/s in queue."
        return self



call1 = Call("01", "Sean", "55555555555", "7:00 AM", "Flat Tire")
call2 = Call("02", "Max", "66666666666", "10:00 AM", "Radiator")
call3 = Call("03", "Manny", "7777777777", "12:00 AM", "Gas")

# CallCenter([1,2,3]).remove().info()
# CallCenter(Call).call().display()
# CallCenter().call
# call1 = CallCenter(Call).call
# print call1
ccenter = CallCenter()
ccenter.add(call1).add(call2).add(call3).remove(call1).info()

# using a global counter to ensure unique IDs so that each __init__ can change it
global idcounter
idcounter = 0

class Call(object):
    
    def __init__(self, id, name, phone_number, time, reason):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.time = time
        self.reason = reason
        # need to re-declare global in order to modify the global variable
        global idcounter
        idcounter += 1
    
    def display(self):
        print "Returning call info..."
        print "**********************"
        print "Call ID:", self.id
        print "Caller Name:", self.name
        print "Caller Phone Number:", self.phone_number
        print "Call Time:", self.time
        print "Reason for Call:", self.reason
        return self

first = Call(idcounter, "Stephen Weil", "770-789-7038", 13.55, "Complaints")
first.display()
second = Call(idcounter, "Joe Shmoe", "888-888-4444", 14.15, "Just wanted someone to talk to")
second.display()
third = Call(idcounter, "Jane Doe", "555-555-5555", 14.28, "Returns")
fourth = Call(idcounter, "Some Name", "111-222-333", 12.30, "To Argue")

class CallCenter(object):

    def __init__(self):
        self.calls = []
        self.queue_size = 0
    
    def add_call(self, call):
        self.calls.append(call)
        self.queue_size = len(self.calls)
        return self

    def remove_call(self):
        self.calls.pop(0)
        self.queue_size = len(self.calls)
        return self

    def remove_specific(self, number):
        for call in enumerate(self.calls):
            if call[1].phone_number == number:
                self.calls.pop(call[0])
                self.queue_size = len(self.calls)
        return self

    def sort(self):
        self.calls = sorted(self.calls, key=lambda k: k.time)
        return self

    def info(self):
        print "Getting queue info...."
        print "**********************"
        print "Queue length:", str(self.queue_size)
        for call in self.calls:
            print "**********************"
            print "Call", call.id
            print "Caller Name: ", call.name
            print "Caller Phone Number: ", call.phone_number
        return self

call_center = CallCenter()
call_center.add_call(first).add_call(second).add_call(third).info()
call_center.remove_specific("888-888-4444").info()
call_center.remove_call().info()
call_center.add_call(fourth).info().sort().info()


class Call(object):
    def __init__(self, ID, name, phone_number, time, reason):
        self.ID = ID
        self.name = name
        self.phone_number = phone_number
        self.time = time
        self.reason = reason

    ##def __str__(self):
    #    return "Hey this worked"

    def display(self):
        print self.ID
        print self.name
        print self.phone_number
        print self.time
        print self.reason

call1 = Call(5689, "Donny", "972-200-0999", 1100, "emergency")
call2 = Call(432, "Jane", "972-897-7638", 1200, "nothing")
call1.display()

class CallCenter(object):

    def __init__(self):
        self.call_list = []
        self.queue_size = len(self.call_list)

    def add(self, call):
        self.call_list.append(call)
        #print self.call_list
        return self

    def remove(self, call):
        del(self.call_list[0])
        return self

    def info(self):
        for item in self.call_list:
            item.display()

    def ridCall(self, check_number):
        for values in self.call_list:
            if values.phone_number == check_number:
                self.call_list.remove(values)
        return self


callCenter1 = CallCenter()
callCenter1.add(call1).add(call2).info()
print "break"
##callCenter1.remove(call1).info()
callCenter1.ridCall("972-897-7638").info()

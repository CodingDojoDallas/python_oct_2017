class Call(object):

    def __init__(self, idnum, name, number, time, reason):
        self.idnum = idnum
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason

    def display(self):
        print "ID: {}\nName: {}\nNumber: {}\nTime: {}\nReason: {}\n".format(self.idnum, self.name, self.number, self.time, self.reason)


class CallCenter(object):

    def __init__(self, calls):
        self.calllist = calls
        self.queue = len(calls)

    def add(self, idnum, name, number, time, reason):
        self.calllist.append(Call(idnum, name, number, time, reason))
        self.queue += 1
        return self

    def remove(self):
        self.calllist.pop(0)
        self.queue -= 1
        return self

    def info(self):
        print "Queue length: {}\n".format(self.queue)
        for callnum, call in enumerate(self.calllist):
            print "Call {}\nName : {}\nNumber: {}\n".format(callnum, call.name, call.number)


calllist = [Call(1, "Joan", "214-530-4323", "08:15", "Needs service"), Call(2, "Josh", "817-601-7322", "08:27", "Has a complaint")]
callcenter = CallCenter(calllist)
callcenter.add(3, "Jack", "817-917-9111", "09:30", "Wants to order").remove().info()
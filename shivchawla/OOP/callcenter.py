''' global CID #The Stephen solution. Works but, then calls keep incremeneting regardless of call center. Not ideal
CID = 0

class Call(object): #create new class inheriting from the god object
    
    def __init__(self,callerName,callerPhoneNumber,timeOfCall,reasonForCall): #pass in those attributes
        self.callerName = callerName #assign callername passed in to the instance of when initialized
        self.callerPhoneNumber = callerPhoneNumber # assign the phone number passed in to the instance of when initialized
        self.timeOfCall = timeOfCall # assign the date/time
        self.reasonForCall = reasonForCall #assign the reason 
        
        global CID #wtf
        self.CID = CID #wtf
        CID += 1 '''

class Call(object): #create new class inheriting from the god object
    CID = 0 #setting a new variable to number calls (unique ID). This is the Nick solution
     @classmethod
     def newID(cls):
         cls.CID += 1
         return cls.CID

    def __init__(self,callerName,callerPhoneNumber,timeOfCall,reasonForCall): #pass in those attributes
        self.callerName = callerName #assign callername passed in to the instance of when initialized
        self.callerPhoneNumber = callerPhoneNumber # assign the phone number passed in to the instance of when initialized
        self.timeOfCall = timeOfCall # assign the date/time
        self.reasonForCall = reasonForCall #assign the reason
        self.CID = self.__class__.CID #wtf What is Call. mean? 
        self.__class__.CID += 1
        

    def display(self): #Print a bunch of shit about instances of call when called
        print "UniqueID: {}".format(self.CID)
        print "Caller Name: {}".format(self.callerName)
        print "Caller Phone Number: {}".format(self.callerPhoneNumber)
        print "Time of Call: {}".format(self.timeOfCall)
        print "Reason for Call: {}".format(self.reasonForCall)
        return self

class CallCenter(object):
    def __init__(self): #remember, shit in the init will only run ONCE! 
        self.calls = [] #Then why was this not a variable outside like the unique ID?
        self.queuesize = len(self.calls) #how do I get this to show the len of the calls list?
    
    def add(self,call): #adds a call to the end of the call list
        self.calls.append(call)
        return self

    def remove(self): #removes the call from the beginning of the list (index 0)
        self.calls.pop(0)
        return self

    def info(self): #Supposed to print all the calls in list. Make a loop if other shit works first
        print self.queuesize


call1 = Call("Shiv",3253201056,"1:30","break")
call2 = Call("Shiv",3253201056,"1:30","break")
call3 = Call("Shiv",3253201056,"1:30","break")
call3.display()
callcenter1 = CallCenter()
callcenter1.add(call1)
callcenter1.add(call2)
callcenter1.info()


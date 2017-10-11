class Patient(object):

    def __init__(self,name, allergies, bedNumber = "none"):
        self.name = name
        self.allergies = allergies
        self.bedNumber = bedNumber

    def display(self):
        print self.name
        print self.allergies
        print self.bedNumber
        return self

class Hospital(object):
    
    def __init__(self,name,capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
        self.listOfBeds = []
        self.openBeds()

    def admit(self,patient):
        if self.capacity == len(self.patients):
            print "go away dude"
        else:
            self.patients.append(patient) #adds a patient to the list
            patient.bedNumber = self.listOfBeds.pop()
            print "i'll fix you"
    
    def openBeds(self):
        for i in range(self.capacity):
            self.listOfBeds.append(i)
        return self

    def discharge(self,patient):
        self.patients.remove(patient)
        self.listOfBeds.append(patient.bedNumber)
        patient.bedNumber = "none" #because you've ALREADY passed in the patient, just change their shit here without calling "self"

patient1 = Patient("Shiv","none",1)
patient2 = Patient("James","chicken",1)
hospital = Hospital("Grey's", 4)
hospital.admit(patient1)
patient1.display()
print patient1
hospital.discharge(patient1)
print hospital.patients 
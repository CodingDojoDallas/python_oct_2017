class Patient(object):
    def __init__(self, id, name, allergies):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bedNum = None

class Hospital(object):
    def __init__(self, name, capacity=10):
        self.name = name
        self.capacity = capacity
        self.patients = [] #Keeps track of all active patients
        self.beds = self.initialize() #Keeps track of all beds and thier availability

    #Initializes a list of beds holding dicts that refer to the bed number and availability
    def initialize(self):
        beds = []
        for i in range(1, self.capacity+1):
            beds.append({"id": i, "Free": True})
        return beds

    #Admit a patient to the hospital. Assigned to a free bed.
    def admit(self, patient):
        if len(self.patients) < self.capacity:
            self.patients.append(patient)
            for i in range(0, len(self.beds)):
                if self.beds[i]["Free"]:     # If a free bed is found. Admit the patient and update bedNum info
                    patient.bedNum = self.beds[i]["id"]
                    self.beds[i]["Free"] = False
                    break
            print "Patient " + patient.name + " has been admitted to bed number " + str(patient.bedNum)
        else:
            print "Sorry there was no free space in this hospital!"
    
    #Discharges a specific patient and opens up the bed to a new patient to be admitted
    def discharge(self, pat_id):
        for i in self.patients:
            if pat_id == i.id:
                self.patients.remove(i)
                for j in self.beds:   # Remove patient and free up bed space
                    if j["id"] == i.bedNum:
                        j["Free"] =  True
                        i.bedNum = None
                        return "Patient " + str(pat_id) + " was discharged from bed " + str(j["id"])
        return "Patient not found"

#Testing
pat1 = Patient(42, "Harshil", "none")
pat2 = Patient(43, "A", "none")
pat3 = Patient(44, "B", "none")
pat4 = Patient(45, "C", "none")
pat5 = Patient(46, "D", "none")
pat6 = Patient(47, "E", "none")
pat7 = Patient(48, "F", "none")
pat8 = Patient(49, "G", "none")
pat9 = Patient(50, "H", "none")
pat10 = Patient(51, "I", "none")
pat11= Patient(52, "J", "none") #Shoudnt be admitted

hos = Hospital("Hos")
hos.admit(pat1)
hos.admit(pat2)
hos.admit(pat3)
hos.admit(pat4)
hos.admit(pat5)
hos.admit(pat6)
hos.admit(pat7)
hos.admit(pat8)
hos.admit(pat9)
hos.admit(pat10)
hos.admit(pat11)
print hos.discharge(44)
print hos.discharge(47)
hos.admit(pat11) #Should be admitted to a free bed with the lowest id
print hos.discharge(44) #Already been discharged so doesnt exist




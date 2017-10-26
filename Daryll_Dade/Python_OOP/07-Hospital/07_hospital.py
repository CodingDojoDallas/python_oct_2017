class Patient():
    def __init__(self,ID,Name,Allergies,Bed=None):
        self.ID = ID
        self.Name = Name
        self.Allergies = Allergies
        self.Bed = Bed

class Hospital():
    def __init__(self):
        self.Patients = []
        self.Name = "Raccoon City Quarantine Center"
        self.Capacity = 7
    def Admit(self,Pat):
        if (len(self.Patients) >= self.Capacity):
            print "Sorry, this hospital is full. Good luck. You will need it."
        else:
            self.Patients.append(Pat)
            print "Patient admitted."
            print self.Patients
        return self
    def Discharge(self,Pat):
        self.Patients.remove(Pat)
        print "Patient Discharged."
        print self.Patients
        Pat.Bed = None
        print Pat.Bed


PatA = Patient(100,"Franklin Goatnob",["Chickweed", "Plastic", "Water", "Goat urine", "florists"])
PatB = Patient(200,"Jimmy Kibblebutler",["Gasoline", "Pitchforks", "Mushrooms", "Dimeatapp", "morgues"])

print PatA.Name + " and " + PatB.Name + " walk up to an large rusty building."

Hospital().Admit(PatA).Admit(PatB).Discharge(PatB)

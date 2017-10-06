global idcounter
idcounter = 0

class Patient(object):

    def __init__(self, id, name, allergies=["None"], bed_num="none"):
        self.id = id
        global idcounter
        idcounter += 1
        self.name = name
        self.allergies = allergies
        self.bed_num = bed_num
    
class Hospital(object):

    def __init__(self, name, capacity, patients=[]):
        self.patients = patients
        self.name = name
        self.capacity = capacity
        # making open_beds a list of possible #s from 1 to capacity
        self.open_beds = []
        for i in range (1, self.capacity+1):
            self.open_beds.append(i)
    
    def admit(self, patient):
        if len(self.patients) + 1 > self.capacity:
            print "Sorry, this hospital is currently at capacity.", patient.name, "may not be admitted."
        else:
            self.patients.append(patient)
            # picks first available bed out of open_beds, assigns to patient, removes that number from list
            patient.bed_num = self.open_beds.pop(0)
            print "Patient", patient.name, "has been admitted and assigned bed #", str(patient.bed_num)
        return self

    def discharge(self, patient):
        for search in enumerate(self.patients): # enumerates so we can get both patient object and index position (for popping)
            if search[1].name == patient.name:
                self.patients.pop(search[0])
                self.open_beds.append(patient.bed_num) # adds patient's bed number back to list of available options
                patient.bed_num = "None"
                print "Patient", patient.name, "has been discharged."
        return self
    
    def display_info(self):
        print "There are currently", str(len(self.patients)), "patients in", self.name, "Hospital."
        print "*******************"
        for search in self.patients:
            print "Name:", search.name
            print "Patient ID:", str(search.id)
            print "Allergies:", search.allergies
            print "Bed #:", str(search.bed_num)
            print "*******************"
        return self

bob = Patient(idcounter, "Bob", ["Penicilin", "Latex"])
jane = Patient(idcounter, "Jane")
timmy = Patient(idcounter, "Timmy", ["Ibuprofen"])
jackie = Patient(idcounter, "Jackie")

hospital = Hospital("St. John's", 3)

hospital.admit(bob).admit(jane).admit(timmy).admit(jackie).display_info().discharge(bob).display_info().admit(jackie).display_info()
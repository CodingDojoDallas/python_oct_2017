class Patient(object):
    def __init__(self, identification, name, allergies, bed_number = 4 ):
        self.identification = identification
        self.name = name
        self.allergies = allergies
        self.bed_number = bed_number

    def display(self):
        print self.identification
        print self.name
        print self.allergies
        print self.bed_number

patient1 = Patient(123, "John", "feelings")
class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
        self.list_of_beds = []
        for i in range(self.capacity):
            self.list_of_beds.append(i)

    def admit(self, patient):
        if self.capacity == len(self.patients):
            print "its full dude"
        elif self.capacity > len(self.patients):
            self.patients.append(patient)
            patient.bed_number = self.list_of_beds.pop()

    def beds(self):
        self.list_of_beds = []
        for i in range(self.capacity):
            self.list_of_beds.append(i)
        print self.list_of_beds[2]


hospital1 = Hospital("Mercy General", 3)
hospital1.admit(patient1)
patient1.display()

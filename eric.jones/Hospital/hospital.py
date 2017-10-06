class Patient(object):

    def __init__(self, idnum, name, allergies, bednum=None):
        self.idnum = idnum
        self.name = name
        self.allergies = allergies
        self.bednum = bednum


class Hospital(object):

    def __init__(self, name, capacity):
        self.patients = []
        self.bedsopen = []
        self.name = name
        self.capacity = capacity
        for idx in range(0, self.capacity):
            self.bedsopen.append(True)

    def admit(self, patient):
        if len(self.patients) >= self.capacity:
            print "Cannot admit. Hospital is full"
        else:
            self.patients.append(patient)
            for idx in range(0, len(self.bedsopen)):
                if self.bedsopen[idx]:
                    self.bedsopen[idx] = False
                    self.patients[len(self.patients) - 1].bednum = idx
                    print "Admission complete."
                    break
        return self

    def discharge(self, idnum):
        for idx, patient in enumerate(self.patients):
            if idnum == patient.idnum:
                self.bedsopen[patient.bednum] = True
                patient.bednum = None
                self.patients.pop(idx)
                print "Patient discharged."
        return self

    def displaypatients(self):
        print "\n{}".format(self.name)
        for patient in self.patients:
            print "Name: {}\nBed: {}\n".format(patient.name, patient.bednum)


pat1 = Patient(1, "Joe", "Aspirin")
pat2 = Patient(2, "Bob", "Penicillin")
pat3 = Patient(3, "Sandy", "Shellfish")
hosp = Hospital("Mercy General", 2)
hosp.admit(pat1).admit(pat2).admit(pat3)
hosp.displaypatients()
hosp.discharge(1).admit(pat3)
hosp.displaypatients()

class Hospital(object):
	def __init__(self, name, capacity):
		self.beds = [None]*capacity
		self.name = name
		self.capacity = capacity
	def admit(self, patient):
		#find the first empty bed. put the patient there
		for num in range(len(self.beds)):
			if self.beds[num] == None:
				self.beds[num] = patient
				patient.bed = num
				print("Admission complete")
				break
		else:
			#cant admit
			print("Patient cannot be admitted, the Hospital is full")
		return self

	def discharge(self,name_or_id):
		if type(name_or_id) == str:
			name_or_id = name_or_id.lower()
		for num in range(len(self.beds)):
			person = self.beds[num]
			if person != None and (person.id == name_or_id or person.name.lower() == name_or_id):
				person.bed = None
				self.beds[num] = None
		return self
	
	
	def info(self):
		print("{}\nmax capacity: {}\n------".format(self.name, self.capacity))
		for patient in self.beds:
			if patient != None:
				patient.info()
				print()
			else:
				print("empty bed\n")



class Patient(object):
	unique_id = 0
	def __init__(self, name, allergies):
		Patient.unique_id += 1
		self.id = Patient.unique_id
		self.name = name
		self.allergies = allergies
		self.bed = None
	def info(self):
		print("Name: {} \nId: {} \nAllergies: {} \nBed: {}".format(self.name, self.id, self.allergies, self.bed))
		
h = Hospital("Holy Hospital", 3)
h.info()
harry = Patient("Harry", "none")
h.admit(harry).admit(Patient("Ron", "carrots")).admit(Patient("Hermoine", "none")).info()
print()
h.discharge("harry").info()
print()
h.discharge(3).info()
print("-------")
harry.info()
from mathdojo import MathDojo
from hospital import Patient
from hospital import Hospital
from car import Car
from callcenter import Call
from callcenter import CallCenter
from bike import Bike
from animals import Animal
from animals import Dog
from animals import Dragon

md = MathDojo(0)
print md
hosp = Hospital("Great Hospital", 6)
print hosp
patient = Patient(1, "Bob")
print patient
car = Car(5000, "75mph", "Full", "25mpg")
print car
call = Call(1, "Stephen", "770-789-7038", 8.30, "For Fun")
print call
call_center = CallCenter()
print call_center
bike = Bike(150, "15mph")
print bike
fox = Animal("Fox")
print fox
pitbull = Dog("Pitbull")
print pitbull
trogdor = Dragon("Trogdor the Burninator")
print trogdor
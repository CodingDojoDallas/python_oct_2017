import random
def scores():
    for i in range(1,11):
        grade = random.randint(60,100)
        letter = ""
        if grade >= 90:
            letter = "A"
        elif grade >= 80:
            letter ="B"
        elif grade >= 70:
            letter = "C"
        else:
            letter = "D"
        print "Score: " + str(grade) + "; your grade is " + str(letter)
    print "End of program. Buh-bye :)"

scores()
import random
def grade_scale(grades):
    print "Scores and Grades"
    for i  in range(0,grades):
        score = random.randint(60,101)#randint is a a method that picks a radon integer between the 2 numbewrs you want to start wwith
        if score >= 60 and score <=69:
            print "score:",score,"; Your grade is a D"
        elif score >=70 and score<=79:
            print "score:",score,"; Your grade is a c"
        elif score >=80 and score<=89:
            print "score:",score,"; Your grade is a B"
        elif score >=90 and score<=100:
            print "score:",score,"; Your grade is a A"
        else:
            print "YOU FAILED!"
    print "end of program"

grade_scale(12)# the number of grades you want print out.

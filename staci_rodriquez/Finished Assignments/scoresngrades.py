def scoresngrades():
    for i in range(10):
        import random
        random_num = int(round((random.random()*40)+60))
        if random_num > 89:
            print "Score: " + str(random_num) + "; Your grade is A"
        elif random_num > 79:
            print "Score: " + str(random_num) + "; Your grade is B"
        elif random_num > 69:
            print "Score: " + str(random_num) + "; Your grade is C"
        else:
            print "Score: " + str(random_num) + "; Your grade is D"            

scoresngrades()



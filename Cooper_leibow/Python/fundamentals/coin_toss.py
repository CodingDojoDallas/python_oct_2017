import random

def coinToss(toss):
    attempt = 0
    heads = 0
    tails = 0
    for i in range(toss):
        value = random.randint(0,100)
        if value >=50:
            heads += 1
            attempt += 1
            print "Attempt #",attempt, ": Throwing a coin... It's a heads! ... Got", heads, "head(s) so far and", tails, "tail(s) so far"
        elif value <=50:
            tails += 1
            attempt += 1
            print "Attempt #",attempt, ": Throwing a coin... It's a tails! ... Got", heads, "head(s) so far and", tails, "tail(s) so far"
        if attempt == 5000:
            print "Ending the program. Thank you!"

toss = 5000
coinToss(toss)

import random
def coinToss():
    print "Start the program..."
    heads = 0
    tails = 0
    for i in range(1,501):
        num = round(random.random())
        if num == 0: #heads
            heads+=1
            print "Attempt #:" + str(i) + " Throwing a coin... It's a head! ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"
        else: #tails
            tails+=1
            print "Attempt #:" + str(i) + " Throwing a coin... It's a tail! ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"
    print "End of program. Buh-byee :)"

coinToss()
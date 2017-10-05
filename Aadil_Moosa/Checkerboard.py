# StarSpace = "* "
# SpaceVar = " "
# int index = 0
# int counter = 0


# while (index <= 7 )
#     if (index % 2 != 0)
#         while(counter <=7)
#             # console.log(StarSpace)
#             counter++
# What am i doing




def checkerboard(a):
    for i in range(0, 8):
        if i%2 == 0:
            print "* " * 4
        else:
            print " *" * 4
    print a

something = " "

checkerboard(something)

def draw_stars(xlist):
    for element in xlist:
        if type(element) == int:
            print "*"*element
        else:
            print element[0].lower()*len(element)
            
x = [4, 6, 1, 3, 5, 7, 25]
x2 = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)
draw_stars(x2)
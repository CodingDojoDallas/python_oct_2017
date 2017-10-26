def draw_stars(list):
    for i in list:
        if (isinstance(i, int)):
            print "*" * i
        if (isinstance(i, basestring)):
            print i[0] * len(i)
        else:
            continue


draw_stars([1,2,3, "Banana", 1.3, "Purple"])

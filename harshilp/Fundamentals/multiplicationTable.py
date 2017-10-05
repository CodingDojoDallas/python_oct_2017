for i in range(13):
    if i == 0:
        y = "x"
    else:
        y = str(i)
    for j in range(1,13):
        if i != 0:
            j = j * i
        y += " " + str(j)
    print y


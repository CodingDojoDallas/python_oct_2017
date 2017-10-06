def checkerboard():
    rows=8
    columns=8
    rowstring=""
    for elem in range(rows):
        for element in range(columns):
            if (element+elem)%2==0:
                rowstring+="*"
            else:
                rowstring+=" "
            if (element%7==0):
                print '\n'
    print rowstring

checkerboard()

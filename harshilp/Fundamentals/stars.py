#Part I
def draw_stars(arr):
    for i in range(len(arr)):
        print "*" * arr[i]
#draw_stars([4, 6, 1, 3, 5, 7, 25])

#Part II
def draw(arr):
    for i in range(len(arr)):
        if isinstance(arr[i], int):
            print "*" * arr[i]
        else:
            print arr[i][0].lower() * len(arr[i])

draw([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])
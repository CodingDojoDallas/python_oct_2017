def compareList(l_one, l_two):
    if l_one == l_two:
        print "These lists are identical"
    else:
        print "These lists are not identical"

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
compareList(list_one, list_two)

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
compareList(list_one, list_two)

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
compareList(list_one, list_two)

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
compareList(list_one, list_two)


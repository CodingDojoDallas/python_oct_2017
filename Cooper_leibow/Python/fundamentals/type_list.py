
def type_list(data_set):
    print type(data_set)
    string_runner = ""
    number_runner = 0
    for i in range (len(data_set)):
        if type(data_set[i]) == str:
            string_runner += " {}".format(data_set[i])
        elif type(data_set[i]) == int or type(data_set[i]) == float:
            number_runner += data_set[i]
    print number_runner
    print string_runner
    if string_runner != "" and number_runner > 0:
        print "The list is of mixed types"
    elif string_runner != "" and number_runner == 0:
        print "The list you entered is of string type"
    elif string_runner == "" and number_runner > 0:
        print "The list you entered is of number type"
    else:
        print "idk"


data_set = ['magical unicorns',19,'hello',98.98,'world']
type_list(data_set)

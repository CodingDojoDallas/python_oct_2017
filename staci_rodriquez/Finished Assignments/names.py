#Part 1
def printnames(stuff):
    for element in stuff:
        print element["first_name"] + " " + element["last_name"]


students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


#Part2
def printnestednames(stuff):
    for key, element in stuff.items():
        print key
        for x, value in enumerate(element):
            print str(x+1) + " - " + value["first_name"] + " " + value["last_name"] + " - " + str(len(value["first_name"]) + len(value["last_name"]))


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

printnames(students)
printnestednames(users)



def combo(students):
    for student in students:
        print student['first_name']+" "+student['last_name']

        # for value in ta:
        #     print "first_name", "last_name"
"""
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

combo(students)

"""

def partTwo(users):
    for keys,values in users.items():
        print keys
        count = 1
        for data in values:
            print str(count)+"-"+data['first_name']+" "+data['last_name']+"-"+str(len(data['first_name'])+len(data['last_name']))
            count += 1


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


partTwo(users)

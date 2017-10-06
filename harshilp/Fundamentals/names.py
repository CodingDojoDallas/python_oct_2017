#Part I
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def showStudents (students):
    for i in range(len(students)):
        print students[i]["first_name"] + " " + students[i]["last_name"]

showStudents(students)

#Part II
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
def showUsers(users):
    for key in users:
        print key
        count = 0
        for person in users[key]:
            count += 1
            print str(count) + " - " + person["first_name"].upper() + " " + person["last_name"].upper() + " - " + str(len(person["first_name"] + person["last_name"]))

showUsers(users)
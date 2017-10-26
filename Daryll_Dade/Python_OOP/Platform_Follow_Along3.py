class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = False


user1 = User("John Doe", "John@doe.com")
print user1.name
print user1.logged
print user1.email

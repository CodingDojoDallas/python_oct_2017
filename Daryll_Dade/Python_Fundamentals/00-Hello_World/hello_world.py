print "Hello World"
x = "Hello Python"
print x
y = 42
print y
# commenting a single line
# we can even comment out code
# print "this will not print!"
print "read below for more on multi-line comments in python!" #this would execute
# This line and below would not execute
'''
Triple quotations allow us to comment across multiple lines as long as
the triple quoted comment is not the first thing in your file.
You can use double or single quotes!
'''
print "this is a sample string"
name = "Zen"
print "My name is", name

first_name = "Zen"
last_name = "Coder"
print "My name is {} {}".format(first_name, last_name)

hw = "hello %s" % 'world'
print hw
# the output would be:
# hello world

x = "Hello World"
print x.upper()
# output:
"HELLO WORLD"

ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []

drawer = ['documents', 'envelopes', 'pens']
#access the drawer with index of 0 and print value
print drawer[0]  #prints documents
#access the drawer with index of 1 and print value
print drawer[1] #prints envelopes
#access the drawer with index of 2 and print value
print drawer[2] #prints pens

x = [99,4,2,5,-3];
print x[:]
#the output would be [99,4,2,5,-3]
print x[1:]
#the output would be [4,2,5,-3];
print x[:4]
#the output would be [99,4,2,5]
print x[2:4]
#the output would be [2,5];

my_list = [1, 'Zen', 'hi']
print len(my_list)
# output
3

my_list = [1,5,2,8,4]
my_list.append(7)
print my_list
# output:
# [1,5,2,8,4,7]

# if statement:
if <condition>:
  # do something
# if-else statement:
elif <condition>:
  # do something
else:
  # do this instead

  age = 15
if age >= 18:
  print 'Legal age'
else:
  print 'You are so young!'

  if age >= 18:
  print 'Legal age'
elif age == 17:
  print 'You are seventeen.'
else:
  print 'You are so young!'

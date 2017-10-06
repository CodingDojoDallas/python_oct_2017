x = "python is fun"
print x.capitalize()
print x.upper()
print x.lower()
print x.find("is")
print x.index("y")
print x.split("n")
y = "-"
print y.join(x)
print x.replace("is", "was")
print x.format("x")

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]

print len(list1)
print len(list2)
print len(list3)

print max(list1)
print max(list2)
print max(list3)

print min(list1)
print min(list2)
print min(list3)

print "Index for 1997 :", list1.index(1997)
print "Index for 4 is :", list2.index(4)
print "Index for a is :", list3.index("a")

list1.append("2002")
print list1
list2.append("6")
print list2
list3.append("f")
print list3

list1.pop()
print list1
list2.pop()
print list2
list3.pop()
print list3

list1.remove(2000)
print list1
list2.remove(3)
print list2
list3.remove("d")
print list3

list1.insert(0, "Insertion")
print list1
list2.insert(4, 11)
print list2
list3.insert(2, "x")
print list3

list1.sort()
print list1
list2.sort()
print list2
list2.sort()
print list3

list1.reverse()
print list1
list2.reverse()
print list2
list3.reverse
print list3

list1.extend(list2)
print list1
list2.extend(list3)
print list2
list3.extend(list1)
print list3

list2.list()
print list2

l = ['magical unicorns',19,'hello',98,'world', ['sdad'], [2,43,5]]
count=0
total_sum=0
total_string=''
total_list=[]
while count < len(l):

    if type(l[count]) == int:

        total_sum=total_sum + l[count]
        check1=True
    if type(l[count]) == str:
        total_string+=(l[count])
        check2=True
    if type(l[count]) == list:
        total_list.append(l[count])
        check3=True
    count+=1


print total_sum
print total_string
print total_list

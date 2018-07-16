list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
list3 = ["a", "b", "c", "d"]

print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])
print ("list2[1:5]: ", list2[:4])
print ("list2[1:5]: ", list2[2:])
print ("list2[1:5]: ", list2[-2:])
print ("list2[1:5]: ", list2[-3:6])

#############################################################

list = ['physics', 'chemistry', 1997, 2000]
print ("Value available at index 2 : ", list[2])

list[2] = 2001
print ("New value available at index 2 : ", list[2])

##############################################################

list = ['physics', 'chemistry', 1997, 2000]

print (list)
del list[2]
print ("After deleting value at index 2 : ", list)

#############################################################

stringg = ["hi"]
list = stringg*4
print(list)

string_new =["lol"]
list2 = stringg +string_new
print(list2) 

case = "lol" in list2
print("is lol there in list:",case)
case2 = "oppo" in list2
print("is oppo there in list:",case2)

print("length of list2:",len(list2))

#############################################################

#explain diff between methods and functions-this

list =[1,2,3]
list2 =[1,2,3,4]
list3 = list

print(min(list))
print(max(list2))

##############################################################

list.append(5)
list.append(3)
print(list)
print(list.count(3))
print(list.index(5))

list.insert(3,4)
print(list)

list.reverse()
print(list)

list.sort()
print(list)

##############################################################

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )

print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2
print (tup3)

tup = ('physics', 'chemistry', 1997, 2000)

print (tup)
del tup

###################################################

#min,max,len
a=[1,2]
b=tuple(a)
print(b)

###################################################

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School" # Add new entry

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

#########################################################

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del dict['Name'] # remove entry with key 'Name'
dict.clear()     # remove all entries in dict
del dict         # delete entire dictionary

##############################################################

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dict.items())
print(dict.keys())
print(dict.values())

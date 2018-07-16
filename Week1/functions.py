def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return

##############################################################################################################

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4] # This would assi new reference in mylist
   print ("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)

###############################################################################################################

def printinfo( name, age ):
    "This prints a passed info into this function"
    print ("Name: ", name)
    print ("Age ", age)
    return

# Now you can call printinfo function
printinfo( age = 50, name = "miki" )

##############################################################################################################

def printinfo2( name, age = 35 ):
    "This prints a passed info into this function"
    print ("Name: ", name)
    print ("Age ", age)
    return

# Now you can call printinfo function
printinfo2( age = 50, name = "miki" )
printinfo2( name = "miki" )

##############################################################################################################

# Function definition is here
def printinfo3( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return

# Now you can call printinfo function
printinfo3( 10 )
printinfo3( 70, 60, 50 )
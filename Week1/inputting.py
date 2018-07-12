#taking inputs
name = input("What's your name? ")
print("Nice to meet you " + name + "!")
age = input("Your age? ")
print("So, you are already " + str(age) + " years old, " + name + "!")

#raw_inputs are only in python 2.7
#input() in python 3 is -> eval(input())
#raw_input() in python 3 is -> input()
name = raw_input("What's your sister's name? ")
print("Say hi to " + name + "!")
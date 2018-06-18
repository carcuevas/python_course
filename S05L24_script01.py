

# for testing methods

a = "hello"
b = "happy biRthday"

print("original a:" "{}".format(a))
print("original b:" "{}".format(b))

# Example of methods

#index method, will return the starting position of the pattern inside the string
print(b.index("biRthday"))
  #if the pattern wont be found it will return ValueError
#print(b.index("tirhtrhtkjrtre"))


#find method, it will nearly the same as index, but instead of giving an error whenver the patter is not found it will return a -1
print(b.find("jfkdjfkdj"))



#strip method is deleting from the strip the specified pattern So if we hae

y = "000000happyBirthday0000000"
print("y = " "{}".format(y))
print("b = " "{}".format(b))
print('y.strip("0") = ' "{}".format(y.strip("0")))
print('b.strip() = ' "{}".format(b.strip()))





# lstrip and rstrip is removing the specified pattern as strip, but from the left and the right respectively
print('y.lstrip("0") = ' "{}".format(y.lstrip("0")))
print('y.rstrip("0") = ' "{}".format(y.rstrip("0")))

## Different ways to add items to lists

A = [5,12,72,55,89]

print("We have A = ""{}".format(A))

# Concatenation


A = A + [1]
print("After we do A = A + [1] we have A = " "{}".format(A))

A = A + ['BCD']
print("\nNow we add BCD into the list A, so we have A = ""{}".format(A))


# .list(list) method will add the elements of a list into the other list
# but we can do something nice too

B = [5,12,72,55,89,1]

print("\nWe have B = ""{}".format(B))
B = B + list("BCD")
print('We do B = B + list("BCD") so B is = ' "{}".format(B))
# see the difference
print("\n\nSee the difference \nA = " "{}" "\nB = " "{}".format(A,B))

##Also we can add a list inside a list
A = [5,12,72,55,89]
print("\n\nWe reset A = ""{}".format(A))
A = A + [[5,6,7,8]]
print("Now we do A=A+[[5,6,7,8]] so we have A = " "{}".format(A))
## Actually we could the same using append method
B = [5,12,72,55,89]
B.append([[5,6,7,8]])
print("\n\nWe reset B= ""{}".format(B))
print("Now we do B.append([[5,6,7,8]] and we have the same B = " "{}".format(B))
print("\n\nBut what would happen if we do B = B.append([0,1]) now??")
B = B.append([0,1])
print("B = " "{}" " and the type of B = " "{}".format(B,type(B)))

# Now .insert(index,element) method, will insert an element in the given index, and shift the rest of them
A = [5,12,72,55,89]
print("\n\nWe reset A = ""{}".format(A))
A.insert(2,100)
print("Now we do A.insert(2,100) and we have A = " "{}".format(A))
# print even we can insert a list inside the list
A.insert(3,["a","b","c"])
print('\nWe can inster a list inside a list as A.insert(3,["a","b","c"]) and we have A = ' "{}".format(A))

###########################################
##@@ VERY IMPORTANT THING
############################################

#Strings are NOT mutable so if we have

S = "123"
# We cannot do S[0] = 0 it will give an error

# But lists are mutable so if we have

L = [2,2,3]
# we can do
L[0] = 1
print("L will be " "{}".format(L))







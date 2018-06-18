## Lists

our_list = [27,46,-5,17,99]
print(our_list)


# We can mix elements with different data type inside of a list
our_list_2 = [ "a","b","c","deedoo",1,2,True ]
print(our_list_2)
print("2nd Element: " "{}".format(our_list_2[1]))

# we can even do slices of the elements
print("The first 3 elements:" "{}".format(our_list_2[0:3:1]))


# Even we can have a list inside another list

our_list_3 = [ 1,2,our_list_2, 6, 7, 8]
print(our_list_3)
print("\n can be seen that the whole index 2 it's our our_list_2, so if we do our_list_3[2] = ""{}".format(our_list_3[2]))
print("\nWe can also access to the elements inside the second list with our_list_3[2][3] = {}".format(our_list_3[2][3]))

## We ca use all the slicing techniques we learn in the S05 ;-)

## All this is used a lot for the Tables as for example:

our_table = [ [1,2,3], [4,5,6], [7,8,9] ] 

#so it's a way to represent this as:
#   1   2   3
#   4   5   6
#   7   8   9
print("\nOur table will be:""{}".format(our_table))
print("\nElement 0,2 from our table would be:""{}".format(our_table[0][2]))
print("Also even slices our_table[1][1:] =""{}".format(our_table[1][1:]))


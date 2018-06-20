#Packing and unpacking Arguments

## For unpacking we will see it easy with the function print.

print('''If we use "print(1,2,3,4,5)" we'll have:  ''',1,2,3,4,5)
a = [1,2,3,4,5]
print('''If we define a = [1,2,3,4,5] and we print(a)" we'll have:  ''',a)
print('''but if we do: print(*a)" we'll have:  ''',*a)

# *a is unpacking the list which is in a and show it as they were 5 parameters.




## For packing we will see also easily if we define some function

def add(x,y):
    return x + y
#  we could do add(10,10) and we will receive the 20 as result but we will have limit to just use 2 parameters but we can do:


def add2(*args):
    # all the numbers we receive will be packed into a Tuple called args
    total = 0
    for number in args:
        total = total + number

    return total

# so with add2 we assure that it will compatible for any number of arguments passed to the function


########### What we can do also is packing & unpacking keyword arguments

## Unpacking
## For example we have our function


def about(name,age,likes):  # name,age and likes are parameters of the function
    sentence = "Meet {} ! he is {} yo and he likes {}".format(name,age,likes)
    return sentence


# We can define a dictionary like

dictionary = {"name": "carlos", "age": 39, "likes": "ice-cream"}

#So we send our dictionary unpacked to our function using '**' as:
print(about(**dictionary))

## Packing
## If we have the function:

def foo(**kwargs):   #kwargs KeyWordAFor sureRGumentS
    for key, value in kwargs.items():  # kwarg.items will return a set of tuples with a key and a value each one
        print("{} : {}".format(key,value))

# So if we pass the folowing keywords to the function, it would take as a dictionary
foo(carlos = "male", kamila = "female")






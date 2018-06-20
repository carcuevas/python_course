#Keyword Arguments and default parameters

def about(name,age,likes):  # name,age and likes are parameters of the function
    sentence = "Meet {} ! they are {} old and they like {}".format(name,age,likes)
    return sentence

print(about("carlos",39,"ice-cream")) # carlos,39, ice-cream are arguments

print(about(name = "carlos", likes = "ice-cream", age = 39)) # We can do it like this using Keyword Arguments

# but always for the function about we will need to pass the arguments for the three parameters name,age,likes

#If we define the function about2 as:


def about2(name,age,likes = "sleep"):  # name,age and likes are parameters of the function
    sentence = "Meet {} ! they are {} old and they like {}".format(name,age,likes)
    return sentence

# we have the default parameter likes with the argument "sleep", so if we don't use any it would take this value as default as for example:

print(about2("luis",33))

#but we can modify the default value
print(about2("Michael",44,"football"))


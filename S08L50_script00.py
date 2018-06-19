#for loops examples 2

# for the example, we'll use a dictionary of students with two keys, male and female, and each key will contain a list of users

students = {
    "male": [ "Tom", "Charlie", "Harry", "Frank"],
    "female" : [ "Sarah", "Huda", "Samantha", "Emily", "Ella" ]
    }



# so now we will do a loop through all keys existing in students dictionaries (male, female)
for key in students.keys():
    #print(students[key]) # that would print the two lists with all names
    for name in students[key]:
        if "a" in name:
            print(name)

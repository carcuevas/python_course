# Dictionaries of lists and dictionaries of dictionaries

# Dictionary of list
students = {
            "Alice": ["ID0001", 26,"A"],
            "Bob": ["ID0003", 27,"B"],
            "Claire":["ID0003", 17,"C"],
            "Dan": ["ID0004", 21,"D"],
            "Emma":["ID0005", 22,"E"],
            }

print('We can print out all the data from students["Claire"] :' "{}".format(students["Claire"]))
print('We can even use slices for getting part of the info like students["Dan"][1:] :' "{}".format(students["Dan"][1:]))

#Dictionaries of dictionaries

students_dict = {
            "Alice": { "id":"ID0001", "age": 26, "grade":"A"},
            "Bob": { "id":"ID0002", "age": 27, "grade":"B"},
            "Claire":{ "id":"ID0003", "age": 17, "grade":"C"},
            "Dan": { "id":"ID0004", "age": 21, "grade":"D"},
            "Emma":{ "id":"ID0005", "age": 22, "grade":"E"},
            }
print('''If using a dictionaries of dictionaries, and we want Dan's age is very easy, we just type: students_dict["Dan"]["age"] :''' "{}".format(students_dict["Dan"]["age"]))
